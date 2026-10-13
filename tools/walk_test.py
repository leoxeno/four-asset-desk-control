"""Walk test: three orientation prompts against the committed folder.

Each prompt runs in a fresh headless session with exactly the treatment
arm's flags, sandbox and working directory (see tools/run_arm.py and
PROTOCOL.md). None of them is a scored run. The answers are logged
verbatim in treatment/walk-test.md with the files the model opened and
the bash calls it made; the raw event streams and result objects go
beside it under treatment/walk-test/. The "What I changed" lines and the
verdict are written by hand afterwards and say so.

Usage:
    python3 tools/walk_test.py
"""
import datetime as dt
import json
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import run_arm  # noqa: E402

PROMPTS = [
    "What is this project for, and what do you need from me to do your job?",
    "What must you never do here?",
    "Which file would you open to find out how a drawdown is defined, and which section?",
]
OUT_DIR = run_arm.ROOT / "treatment" / "walk-test"
OUT_MD = run_arm.ROOT / "treatment" / "walk-test.md"


def main() -> None:
    if OUT_MD.exists() or OUT_DIR.exists():
        raise SystemExit("walk test already recorded; this script never overwrites it")
    OUT_DIR.mkdir(parents=True)
    arm = "treatment"
    system_prompt = run_arm.BASE_SYSTEM_PROMPT + " " + run_arm.ARM_LINE[arm]
    settings_path = OUT_DIR / "settings.json"
    settings_path.write_text(json.dumps(run_arm.SANDBOX_SETTINGS, indent=2) + "\n")
    cmd = [
        "claude", "-p",
        "--model", run_arm.MODEL,
        "--effort", run_arm.EFFORT,
        "--output-format", "stream-json",
        "--verbose",
        "--no-session-persistence",
        "--safe-mode",
        "--strict-mcp-config",
        "--setting-sources", "",
        "--settings", str(settings_path),
        "--tools", run_arm.TOOLS,
        "--disallowedTools", "WebSearch,WebFetch",
        "--allowedTools", run_arm.ALLOWED,
        "--permission-mode", "dontAsk",
        "--permission-prompts", "none",
        "--system-prompt", system_prompt,
    ]
    commit = run_arm.git_commit()
    lines = [
        "# Walk test: a fresh chat, only the folder",
        "",
        f"Run once before treatment run 1, with the folder as committed in `{commit}`: three prompts, each in a fresh headless session with exactly the treatment arm's flags, sandbox and working directory (see `PROTOCOL.md`), none of them a scored run. What it answered is logged verbatim by `tools/walk_test.py`, with the files it opened; the raw event streams are in `walk-test/`. This is the icm-architect walk test: an agent with no memory must orient, act and report from the files alone. The \"What I changed\" lines and the verdict were written by hand afterwards.",
        "",
    ]
    for i, prompt in enumerate(PROMPTS, 1):
        work = run_arm.stage_workdir(arm)
        started = dt.datetime.now().astimezone().isoformat(timespec="minutes")
        summary, _events = run_arm.run_question(cmd, prompt, work, OUT_DIR / f"p{i}.jsonl")
        shutil.rmtree(work, ignore_errors=True)
        (OUT_DIR / f"p{i}.json").write_text(json.dumps({"prompt": prompt, **summary}, indent=2, ensure_ascii=False) + "\n")
        reads = [c["file"] for c in summary["tool_calls"] if c["tool"] == "Read"]
        bash = sum(1 for c in summary["tool_calls"] if c["tool"] == "Bash")
        lines += [
            f"## Prompt {i}",
            "",
            f"`{prompt}`",
            "",
            "What it answered:",
            "",
            f"(run {started}, {summary['num_turns']} turns, {summary['seconds']}s, status {summary['status']}; files opened with Read: {reads}; bash calls: {bash})",
            "",
            (summary["result_text"] or "").strip(),
            "",
            "What I changed: (written by hand after reading the answer)",
            "",
        ]
        print(f"prompt {i}: {summary['status']}, {summary['seconds']}s, turns {summary['num_turns']}", flush=True)
    lines += ["## Verdict", "", "(written by hand)", ""]
    OUT_MD.write_text("\n".join(lines))
    print(f"wrote {OUT_MD.relative_to(run_arm.ROOT)}")


if __name__ == "__main__":
    main()
