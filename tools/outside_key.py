"""Key the outside-check questions and render outside-check/questions.md.

The three prompts come verbatim from outside-check/generation/response.md,
written by a blank session that never saw the folder. This script computes
the expected answer for each under reference/methodology.md from the
committed CSV and writes the questions file in the same shape as
questions.md, so tools/run_arm.py can run them on every arm. Nothing
numeric is typed by hand.

Usage:
    python3 tools/outside_key.py
"""
import pathlib
import re

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
CSV = ROOT / "reference" / "data" / "monthly-adjusted-close.csv"
RESPONSE = ROOT / "outside-check" / "generation" / "response.md"
OUT = ROOT / "outside-check" / "questions.md"
TICKERS = ["SPY", "TLT", "GLD", "USO"]


def compute() -> dict:
    prices = pd.read_csv(CSV, index_col="Date", parse_dates=True)[TICKERS]
    rets = prices.pct_change().dropna()
    rets.index = rets.index.to_period("M")
    rets = rets.loc["2023-01":"2026-09"]
    port = rets.mean(axis=1)
    sharpe = port.mean() * 12 / (port.std(ddof=1) * 12 ** 0.5)          # methodology section 6
    spy_ytd = (1 + rets.loc["2026", "SPY"]).prod() - 1                   # section 4, year to date
    tlt = rets.loc["2023-01":"2025-12", "TLT"]                           # section 9
    return {
        "sharpe": round(float(sharpe), 2),
        "spy_ytd_2026": round(float(spy_ytd) * 100, 1),
        "tlt_worst_return": round(float(tlt.min()) * 100, 1),
        "tlt_worst_month": str(tlt.idxmin()),
        "n_2026_months": int(len(rets.loc["2026"])),
    }


def parse_prompts() -> list[tuple[str, str, str]]:
    text = RESPONSE.read_text()
    blocks = re.findall(r"^## (X\d+)\. (.+?)\n\nPrompt: `(.+?)`", text, flags=re.M)
    if len(blocks) != 3:
        raise SystemExit(f"expected 3 prompts in {RESPONSE}, found {len(blocks)}")
    return blocks


def render(k: dict, prompts: list[tuple[str, str, str]]) -> str:
    specs = {
        "X1": (
            f"**{k['sharpe']}**",
            "correct within 0.03. Partial within 0.10. Wrong otherwise, including any figure that uses a non-zero risk-free rate or compounds the annualised return.",
            "methodology section 6; `tools/outside_key.py`, sharpe.",
        ),
        "X2": (
            f"**{k['spy_ytd_2026']}%** (nine monthly returns, January to September 2026)",
            "correct within 0.3 percentage points. Partial within 2 percentage points. Wrong otherwise.",
            "methodology section 4 (year to date); `tools/outside_key.py`, spy_ytd_2026.",
        ),
        "X3": (
            f"**{k['tlt_worst_return']}%** (in {k['tlt_worst_month']}; the month is not asked for, but a wrong month beside the right number is noted)",
            "correct within 0.3 percentage points. Partial within 2 percentage points. Wrong otherwise.",
            "methodology sections 2 and 9; `tools/outside_key.py`, tlt_worst.",
        ),
    }
    lines = [
        "# Outside check: three questions we did not write",
        "",
        "Written by a blank session that saw only the data dictionary and the methodology, never the folder, the eight questions, the answer key or any transcript. Its prompt and reply are saved verbatim in `generation/`. The prompts below are copied from that reply unchanged. Expected answers are computed by `tools/outside_key.py` from the committed CSV under `reference/methodology.md`. Committed before any arm ran on these questions.",
        "",
        "Grading follows the same scheme as `questions.md`: correct, partial, wrong; declining to give a number is wrong; a number right under a rejected convention is partial at best.",
        "",
        "---",
        "",
    ]
    for label, title, prompt in prompts:
        expected, grading, where = specs[label]
        lines += [
            f"## {label}. {title}",
            "",
            f"Prompt: `{prompt}`",
            "",
            f"Expected: {expected}.",
            "",
            f"Grading: {grading}",
            "",
            f"Where the answer lives: {where}",
            "",
        ]
    lines += ["---", "", "## What this file never does", "", "It never changes after it is committed. The prompts are the blank session's words, not ours.", ""]
    return "\n".join(lines)


def main() -> None:
    k = compute()
    for key, value in k.items():
        print(f"{key:<18} {value}")
    OUT.write_text(render(k, parse_prompts()))
    print(f"wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
