"""Run one arm of the control, one question per fresh Claude Code session.

Every arm runs the same prompts, in the same order, with the same model,
the same effort, the same tools and the same sandbox. The only difference
between arms is what sits in the working directory and the one extra line
in the system prompt that points at it:

    cold       empty working directory, no extra line
    treatment  the five-file folder with reference/, one line: read README.md first

Each question is answered in a fresh session from a throwaway working
directory under /srv/comp14-runs, so the model never sees this repo,
questions.md or the answer key. Output per question: the raw event stream (qN.jsonl), the
final result object (qN.json), and a readable transcript.md for the run.
Nothing is edited after the fact. A failed or timed-out question is
recorded as such and the run continues.

Usage:
    python3 tools/run_arm.py cold 1 --jobs 8
    python3 tools/run_arm.py treatment 1 --jobs 8
    python3 tools/run_arm.py treatment 3 --questions outside-check/questions.md --out outside-check/treatment

The runner never overwrites an existing run directory.
"""
import argparse
import datetime as dt
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import scrub  # noqa: E402  (redacts the sandbox's own throwaway proxy credentials, nothing else)

ROOT = pathlib.Path(__file__).resolve().parents[1]

MODEL = "claude-opus-5-5"
EFFORT = "high"
TIMEOUT_S = 900

BASE_SYSTEM_PROMPT = "Answer the user's question."
ARM_LINE = {
    "cold": "",
    "treatment": "Read README.md first and follow it.",
}
ARM_FILES = {
    "cold": [],
    "treatment": [
        ("README.md", "README.md"),
        ("identity.md", "identity.md"),
        ("rules.md", "rules.md"),
        ("examples.md", "examples.md"),
        ("reference/methodology.md", "reference/methodology.md"),
        ("reference/data/data-dictionary.md", "reference/data/data-dictionary.md"),
        ("reference/data/monthly-adjusted-close.csv", "reference/data/monthly-adjusted-close.csv"),
        ("reference/data/fetch-log.txt", "reference/data/fetch-log.txt"),
    ],
}
ARM_DEFAULT_OUT = {"cold": "control", "treatment": "treatment"}

# The same tools in every arm. No web search, no web fetch, no subagents.
# Read and Write are scoped to the working directory by the allow rules.
TOOLS = "Bash,Read,Write,Glob,Grep"
ALLOWED = "Bash,Read(./**),Write(./**),Glob,Grep"

# Bash runs in Claude Code's sandbox: no network, writes confined to the
# working directory, and no reads of the home directory or the projects tree
# where this repo lives. Checked by tools/check_sandbox.py before any scored
# run; the check's output is kept in tools/sandbox-check.log.
SANDBOX_SETTINGS = {
    "sandbox": {
        "enabled": True,
        "failIfUnavailable": True,            # never fall back to unsandboxed commands
        "allowUnsandboxedCommands": False,
        "autoAllowBashIfSandboxed": True,
        "network": {"allowedDomains": [], "strictAllowlist": True, "allowUnixSockets": [], "allowLocalBinding": False},
        "filesystem": {
            "allowWrite": ["."],
            "denyRead": ["/root", "/home", "/mnt", "/tmp", "/var/tmp"],
        },
    },
    "permissions": {"blockReadsOutsideWorkingDirectories": True},
}

# Throwaway working directories live here, outside /tmp (which is denied
# above, so a session cannot find another session's files or anything else
# lying around the machine). Each session gets its own directory and the
# sandbox allows reads of the current directory itself.
WORK_PARENT = pathlib.Path("/srv/comp14-runs")


def load_prompts(path: pathlib.Path) -> list[tuple[str, str]]:
    """Return [(label, prompt)] from a questions file: '## Q1. ...' headings and 'Prompt: `...`' lines."""
    prompts, label = [], None
    for line in path.read_text().splitlines():
        m = re.match(r"^## ([QX]\d+)\.", line)
        if m:
            label = m.group(1)
        m = re.match(r"^Prompt: `(.+)`\s*$", line)
        if m:
            prompts.append((label or f"Q{len(prompts) + 1}", m.group(1)))
    if not prompts:
        raise SystemExit(f"no prompts found in {path}")
    return prompts


def stage_workdir(arm: str) -> pathlib.Path:
    WORK_PARENT.mkdir(parents=True, exist_ok=True)
    work = pathlib.Path(tempfile.mkdtemp(prefix=f"{arm}-", dir=WORK_PARENT))
    for src, dst in ARM_FILES[arm]:
        target = work / dst
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / src, target)
    return work


def claude_version() -> str:
    try:
        return subprocess.run(["claude", "--version"], capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception as exc:  # noqa: BLE001
        return f"unknown ({exc})"


def git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except Exception:  # noqa: BLE001
        return "unknown"


def run_question(cmd: list[str], prompt: str, work: pathlib.Path, jsonl_path: pathlib.Path) -> tuple[dict, list]:
    """Run one fresh session; stream events to jsonl; return (summary dict, parsed events)."""
    started = time.time()
    events = []
    status = "ok"
    try:
        proc = subprocess.run(cmd + [prompt], cwd=work, capture_output=True, text=True, timeout=TIMEOUT_S)
        raw = proc.stdout
        stderr = proc.stderr
        if proc.returncode != 0:
            status = f"exit {proc.returncode}"
    except subprocess.TimeoutExpired as exc:
        raw = (exc.stdout or b"").decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = (exc.stderr or b"").decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        status = f"timeout after {TIMEOUT_S}s"
    raw, redacted = scrub.scrub_text(raw)
    stderr, _ = scrub.scrub_text(stderr)
    jsonl_path.write_text(raw)
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            events.append({"type": "unparsed", "text": line})
    result = next((e for e in events if e.get("type") == "result"), None)
    init = next((e for e in events if e.get("type") == "system" and e.get("subtype") == "init"), {})
    summary = {
        "status": status,
        "sandbox_proxy_credentials_redacted": redacted,
        "model_reported_at_init": init.get("model"),
        "seconds": round(time.time() - started, 1),
        "stderr_tail": stderr[-2000:] if stderr else "",
        "result_text": (result or {}).get("result"),
        "is_error": (result or {}).get("is_error"),
        "num_turns": (result or {}).get("num_turns"),
        "duration_ms": (result or {}).get("duration_ms"),
        "duration_api_ms": (result or {}).get("duration_api_ms"),
        "usage": (result or {}).get("usage"),
        "model_usage": (result or {}).get("modelUsage"),
        "total_cost_usd": (result or {}).get("total_cost_usd"),
        "permission_denials": (result or {}).get("permission_denials"),
        "session_id": (result or {}).get("session_id"),
        "tool_calls": [],
    }
    for e in events:
        if e.get("type") == "assistant":
            for block in e.get("message", {}).get("content", []):
                if block.get("type") == "tool_use":
                    inp = block.get("input", {})
                    summary["tool_calls"].append({
                        "tool": block.get("name"),
                        "file": inp.get("file_path") or inp.get("path") or inp.get("pattern"),
                        "command": inp.get("command"),
                        "asked_to_leave_sandbox": bool(inp.get("dangerouslyDisableSandbox")),
                    })
    return summary, events


def render_transcript(arm: str, run: int, info: dict, per_q: list[dict], events_by_q: dict) -> str:
    lines = [
        f"Arm: {arm}",
        f"Run: {run}",
        f"Started: {info['started_at']}",
        f"Finished: {info['finished_at']}",
        f"Model: {info['model']}  Effort: {info['effort']}  Claude Code: {info['claude_code_version']}",
        f"Tools: {info['tools']}  Sandbox: {json.dumps(info['sandbox_settings'])}",
        f"Working directory contents: {info['workdir_files'] or 'empty'}",
        f"Repo commit when run: {info['repo_commit']}",
        "System prompt (verbatim):",
        "```",
        info["system_prompt"],
        "```",
        "",
        "Nothing below is edited. Tool calls and tool results are shown as the event stream delivered them.",
        "",
    ]
    for q in per_q:
        lines += [f"## {q['label']}", "", f"**Prompt (verbatim):** {q['prompt']}", ""]
        for e in events_by_q[q["label"]]:
            if e.get("type") == "assistant":
                for block in e.get("message", {}).get("content", []):
                    if block.get("type") == "text":
                        lines += [block["text"], ""]
                    elif block.get("type") == "tool_use":
                        lines += [f"[tool call: {block.get('name')}] {json.dumps(block.get('input'), ensure_ascii=False)}", ""]
            elif e.get("type") == "user":
                for block in e.get("message", {}).get("content", []):
                    if isinstance(block, dict) and block.get("type") == "tool_result":
                        content = block.get("content")
                        if isinstance(content, list):
                            content = "\n".join(c.get("text", "") for c in content if isinstance(c, dict))
                        lines += ["[tool result]", "```", str(content), "```", ""]
        s = q["summary"]
        lines += [
            f"Status: {s['status']}; turns: {s['num_turns']}; seconds: {s['seconds']}; "
            f"tokens in/out: {(s['usage'] or {}).get('input_tokens')}/{(s['usage'] or {}).get('output_tokens')}; "
            f"files read: {[c['file'] for c in s['tool_calls'] if c['tool'] == 'Read']}; "
            f"bash calls: {sum(1 for c in s['tool_calls'] if c['tool'] == 'Bash')}; "
            f"asked to leave sandbox: {sum(1 for c in s['tool_calls'] if c.get('asked_to_leave_sandbox'))}",
            "",
        ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("arm", choices=list(ARM_FILES))
    parser.add_argument("run", type=int)
    parser.add_argument("--questions", default="questions.md")
    parser.add_argument("--out", default=None, help="run directory parent, relative to the repo root")
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--effort", default=EFFORT)
    parser.add_argument("--only", default=None, help="comma-separated labels, for smoke tests (e.g. Q1,Q8)")
    parser.add_argument("--jobs", type=int, default=1, help="questions run concurrently, each in its own session and working directory (1 = one after another)")
    args = parser.parse_args()

    out_parent = ROOT / (args.out or ARM_DEFAULT_OUT[args.arm])
    run_dir = out_parent / f"run-{args.run}"
    if run_dir.exists():
        raise SystemExit(f"{run_dir} exists; the runner never overwrites a run")
    run_dir.mkdir(parents=True)

    prompts = load_prompts(ROOT / args.questions)
    if args.only:
        wanted = set(args.only.split(","))
        prompts = [p for p in prompts if p[0] in wanted]

    system_prompt = BASE_SYSTEM_PROMPT + (" " + ARM_LINE[args.arm] if ARM_LINE[args.arm] else "")
    (run_dir / "system-prompt.txt").write_text(system_prompt + "\n")
    settings_path = run_dir / "settings.json"
    settings_path.write_text(json.dumps(SANDBOX_SETTINGS, indent=2) + "\n")

    cmd = [
        "claude", "-p",
        "--model", args.model,
        "--effort", args.effort,
        "--output-format", "stream-json",
        "--verbose",
        "--no-session-persistence",
        "--safe-mode",
        "--strict-mcp-config",
        "--setting-sources", "",
        "--settings", str(settings_path),
        "--tools", TOOLS,
        "--disallowedTools", "WebSearch,WebFetch",
        "--allowedTools", ALLOWED,
        "--permission-mode", "dontAsk",
        "--permission-prompts", "none",
        "--system-prompt", system_prompt,
    ]

    info = {
        "arm": args.arm,
        "run": args.run,
        "model": args.model,
        "effort": args.effort,
        "claude_code_version": claude_version(),
        "command": cmd + ["<prompt>"],
        "tools": TOOLS,
        "sandbox_settings": SANDBOX_SETTINGS,
        "system_prompt": system_prompt,
        "questions_file": args.questions,
        "questions": [p[0] for p in prompts],
        "prompt_delivery": "argument, one fresh session per question, from a throwaway working directory under /srv/comp14-runs",
        "repo_commit": git_commit(),
        "started_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
    }

    info["jobs"] = args.jobs

    def one(item):
        label, prompt = item
        work = stage_workdir(args.arm)
        files = sorted(str(p.relative_to(work)) for p in work.rglob("*") if p.is_file())
        summary, events = run_question(cmd, prompt, work, run_dir / f"{label.lower()}.jsonl")
        shutil.rmtree(work, ignore_errors=True)
        (run_dir / f"{label.lower()}.json").write_text(json.dumps({"label": label, "prompt": prompt, **summary}, indent=2, ensure_ascii=False) + "\n")
        print(f"[{args.arm} run-{args.run}] {label}: {summary['status']}, {summary['seconds']}s, turns {summary['num_turns']}", flush=True)
        return label, prompt, summary, events, files

    import concurrent.futures
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.jobs)) as pool:
        for label, prompt, summary, events, files in pool.map(one, prompts):
            results[label] = (prompt, summary, events, files)
    per_q, events_by_q = [], {}
    for label, _ in prompts:                      # keep the committed order in the transcript
        prompt, summary, events, files = results[label]
        info["workdir_files"] = files
        per_q.append({"label": label, "prompt": prompt, "summary": summary})
        events_by_q[label] = events

    info["finished_at"] = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    (run_dir / "run-info.json").write_text(json.dumps(info, indent=2) + "\n")
    (run_dir / "transcript.md").write_text(render_transcript(args.arm, args.run, info, per_q, events_by_q))
    shown = run_dir.relative_to(ROOT) if run_dir.is_relative_to(ROOT) else run_dir
    print(f"wrote {shown}")


if __name__ == "__main__":
    main()
