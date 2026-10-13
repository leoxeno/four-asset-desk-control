"""Ask a blank session to write three questions we did not write.

The session sees the data dictionary and the methodology, so its questions
are answerable from the data under the house conventions. It never sees the
folder, questions.md, the answer key or any transcript. Its prompt and its
reply are saved verbatim under outside-check/generation/. We then key the
questions with tools/outside_key.py and commit both before any arm runs on
them.

Usage:
    python3 tools/outside_questions.py
"""
import datetime as dt
import json
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "outside-check" / "generation"
MODEL = "claude-opus-5-5"

COVERED = (
    "the best asset of 2024, GLD's 2025 return, the SPY and TLT return correlation, the equal-weight "
    "portfolio's cumulative return, its maximum drawdown, USO's annualised volatility, the best month of "
    "2026 for the portfolio, and a month outside the data"
)


def build_prompt() -> str:
    dictionary = (ROOT / "reference" / "data" / "data-dictionary.md").read_text()
    methodology = (ROOT / "reference" / "methodology.md").read_text()
    return f"""You are writing test questions for a portfolio desk. You have never seen the desk's files; you only have the two documents below: a data dictionary and a methodology.

Write exactly three questions a client might ask about these four ETFs, SPY, TLT, GLD and USO, or about the equal-weight portfolio of the four as the methodology defines it. Requirements:

- Each question must have one checkable numeric answer computable from a month-end price file covering 2022-12-31 to 2026-09-30 under the methodology. No opinion questions, no forecasts.
- Each question must be self-contained: name the assets, the period (months and years), and the portfolio rule in plain words, as if the reader had no documents at all. Never mention a file, a dataset, a folder or the methodology.
- Use three different quantities. Avoid these, which are already covered: {COVERED}.
- Stay inside January 2023 to September 2026.
- Do not include the answers.

Output exactly this format and nothing else, with your three questions in place of the placeholders:

## X1. <short title>

Prompt: `<the question, one sentence>`

## X2. <short title>

Prompt: `<the question, one sentence>`

## X3. <short title>

Prompt: `<the question, one sentence>`

--- DATA DICTIONARY ---
{dictionary}
--- METHODOLOGY ---
{methodology}
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    prompt = build_prompt()
    (OUT / "prompt.txt").write_text(prompt)
    work = pathlib.Path(tempfile.mkdtemp(prefix="outside-questions-"))
    cmd = [
        "claude", "-p", "--model", MODEL, "--effort", "high", "--output-format", "json",
        "--no-session-persistence", "--safe-mode", "--strict-mcp-config", "--setting-sources", "",
        "--tools", "", "--permission-mode", "dontAsk",
        "--system-prompt", "You write test questions. Follow the format exactly.",
        prompt,
    ]
    started = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    proc = subprocess.run(cmd, cwd=work, capture_output=True, text=True, timeout=600)
    result = json.loads(proc.stdout)
    (OUT / "response.md").write_text((result.get("result") or "") + "\n")
    (OUT / "run-info.json").write_text(json.dumps({
        "model": MODEL,
        "command": cmd[:-1] + ["<prompt in prompt.txt>"],
        "started_at": started,
        "finished_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "usage": result.get("usage"),
        "model_usage": result.get("modelUsage"),
        "session_id": result.get("session_id"),
    }, indent=2) + "\n")
    print(result.get("result"))


if __name__ == "__main__":
    main()
