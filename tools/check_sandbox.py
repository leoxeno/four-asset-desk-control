"""Prove the harness sandbox before any scored run.

Runs one headless session with exactly the flags tools/run_arm.py uses and
asks the model to execute three fixed commands verbatim. The printed
outputs show whether the network is reachable, whether the filesystem
outside the working directory is readable, and whether Python can import
a networking library and reach out. Keep the output: it goes into
PROTOCOL.md as the evidence that the control could not fetch prices.

Usage:
    python3 tools/check_sandbox.py
"""
import json
import pathlib
import subprocess
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import run_arm  # noqa: E402

PROMPT = (
    "Run exactly these three bash commands, one at a time, and then report each command's complete output "
    "verbatim in a fenced block. Do not interpret, fix or retry anything.\n"
    "1. curl -sS -m 8 https://finance.yahoo.com -o /dev/null -w 'HTTP %{http_code}\\n'; echo \"curl exit=$?\"\n"
    "2. python3 -c \"import urllib.request; print(urllib.request.urlopen('https://example.com', timeout=8).status)\"; echo \"python exit=$?\"\n"
    "3. ls /root/projects 2>&1 | head -5; echo \"ls exit=$?\"; cat /root/.claude/settings.json 2>&1 | head -c 120; echo; echo \"cat exit=$?\"\n"
    "Then, as a fourth step, use the Read tool (not bash) on the path /root/.claude/settings.json and report "
    "verbatim whether it returned content or an error. Fifth, run "
    "`find / -name 'monthly-adjusted-close.csv' 2>/dev/null | head; echo \"find exit=$?\"; ls /tmp /mnt /srv/comp14-runs 2>&1 | head -8; "
    "python3 -c 'import pandas, statistics; print(\"pandas\", pandas.__version__)'; ls -la .` "
    "and report its output verbatim."
)


def main() -> None:
    run_arm.WORK_PARENT.mkdir(parents=True, exist_ok=True)
    work = pathlib.Path(tempfile.mkdtemp(prefix="sandbox-check-", dir=run_arm.WORK_PARENT))
    (work / "canary.txt").write_text("the working directory itself must stay readable\n")
    settings = work / "settings.json"
    settings.write_text(json.dumps(run_arm.SANDBOX_SETTINGS, indent=2))
    cmd = [
        "claude", "-p",
        "--model", run_arm.MODEL,
        "--effort", "low",
        "--output-format", "json",
        "--no-session-persistence",
        "--safe-mode",
        "--strict-mcp-config",
        "--setting-sources", "",
        "--settings", str(settings),
        "--tools", run_arm.TOOLS,
        "--allowedTools", run_arm.ALLOWED,
        "--system-prompt", "Answer the user's question.",
        PROMPT,
    ]
    proc = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=600)
    try:
        result = json.loads(proc.stdout)
        print(result.get("result"))
        print("\n--- permission_denials:", result.get("permission_denials"))
        print("--- is_error:", result.get("is_error"), "| turns:", result.get("num_turns"))
    except json.JSONDecodeError:
        print(proc.stdout[:3000])
    if proc.stderr.strip():
        print("--- stderr tail ---")
        print(proc.stderr[-1500:])


if __name__ == "__main__":
    main()
