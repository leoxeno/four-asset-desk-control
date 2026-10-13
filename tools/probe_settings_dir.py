"""Probe what a session can see of the directory that holds its settings file.

Found during cold control run 1: the runner passes each run's settings
file from the run's own output directory inside this repo, and one cold
session listed that directory with a plain `ls` and saw the settings file
and the system prompt. The sandbox denies reads under /root, so the
listing must come from Claude Code allowing the directory that holds the
settings file it was given. This script asks a session, with exactly the
runner's flags and the real settings file of control/run-1, to try that
directory, its parent, the repo root, the price file, the questions file
and a sibling result file, one plain command per Bash call, and to report
every output verbatim. The point is to establish what is reachable and
what is not; the output is kept in tools/settings-dir-probe.log.

Usage:
    python3 tools/probe_settings_dir.py
"""
import json
import pathlib
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import run_arm  # noqa: E402

REPO = run_arm.ROOT
SETTINGS = REPO / "control" / "run-1" / "settings.json"
COMMANDS = [
    f"ls -la {REPO}/control/run-1",
    f"ls -la {REPO}/control",
    f"ls -la {REPO}",
    f"head -3 {REPO}/reference/data/monthly-adjusted-close.csv",
    f"head -3 {REPO}/questions.md",
    f"head -c 200 {REPO}/control/run-1/q1.json",
    f"ls {REPO.parent}",
    "grep -c four-asset /proc/self/mountinfo",
]

PROMPT = (
    "Run each of the following bash commands as its own separate Bash tool call, exactly as written, one at a time. "
    "Never combine them, never retry, never fix or interpret anything. Then report every command's complete output "
    "(or error) verbatim, each in its own fenced block, numbered in order.\n"
    + "\n".join(f"{i}. {c}" for i, c in enumerate(COMMANDS, 1))
    + f"\nFinally, use the Read tool (not bash) on {REPO}/control/run-1/system-prompt.txt and on "
    f"{REPO}/questions.md, and report verbatim whether each returned content or an error."
)


def main() -> None:
    run_arm.WORK_PARENT.mkdir(parents=True, exist_ok=True)
    work = pathlib.Path(tempfile.mkdtemp(prefix="settings-probe-", dir=run_arm.WORK_PARENT))
    cmd = [
        "claude", "-p",
        "--model", run_arm.MODEL,
        "--effort", "low",
        "--output-format", "json",
        "--no-session-persistence",
        "--safe-mode",
        "--strict-mcp-config",
        "--setting-sources", "",
        "--settings", str(SETTINGS),
        "--tools", run_arm.TOOLS,
        "--disallowedTools", "WebSearch,WebFetch",
        "--allowedTools", run_arm.ALLOWED,
        "--permission-mode", "dontAsk",
        "--permission-prompts", "none",
        "--system-prompt", "Answer the user's question.",
        PROMPT,
    ]
    print(f"settings file: {SETTINGS}\nworking directory: {work}\n")
    proc = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=600)
    try:
        result = json.loads(proc.stdout)
        print(result.get("result"))
        print("\n--- permission_denials:", json.dumps(result.get("permission_denials"), ensure_ascii=False))
        print("--- is_error:", result.get("is_error"), "| turns:", result.get("num_turns"))
    except json.JSONDecodeError:
        print(proc.stdout[:3000])
    if proc.stderr.strip():
        print("--- stderr tail ---")
        print(proc.stderr[-1500:])


if __name__ == "__main__":
    main()
