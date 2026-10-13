"""Compute every expected answer in questions.md from the committed CSV.

Nothing numeric in questions.md is typed by hand. This script implements
reference/methodology.md line by line, prints the answers, and can render
questions.md from tools/questions.template.md.

Usage:
    python3 tools/answer_key.py                  # print the answers
    python3 tools/answer_key.py --render         # write questions.md from the template
    python3 tools/answer_key.py --json           # print the answers as JSON
"""
import argparse
import json
import pathlib

import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
CSV = ROOT / "reference" / "data" / "monthly-adjusted-close.csv"
TEMPLATE = ROOT / "tools" / "questions.template.md"
QUESTIONS = ROOT / "questions.md"
TICKERS = ["SPY", "TLT", "GLD", "USO"]
PERIOD_START = "2023-01"
PERIOD_END = "2026-09"


def load_returns() -> tuple[pd.DataFrame, pd.DataFrame]:
    prices = pd.read_csv(CSV, index_col="Date", parse_dates=True)[TICKERS]
    rets = prices.pct_change().dropna()          # simple monthly returns, methodology section 2
    rets.index = rets.index.to_period("M")
    return rets.loc[PERIOD_START:PERIOD_END], prices


def compute() -> dict:
    rets, prices = load_returns()
    port = rets.mean(axis=1)                      # equal weight, rebalanced monthly, section 3
    out = {"n_months": int(len(rets)), "period_start": PERIOD_START, "period_end": PERIOD_END}

    # Calendar-year total returns, section 4
    for year in ["2023", "2024", "2025"]:
        for t in TICKERS:
            out[f"cy_{year}_{t}"] = round(((1 + rets.loc[year, t]).prod() - 1) * 100, 1)
        out[f"cy_{year}_PORT"] = round(((1 + port.loc[year]).prod() - 1) * 100, 1)
    out["ytd_2026_PORT"] = round(((1 + port.loc["2026"]).prod() - 1) * 100, 1)
    best_2024 = max(TICKERS, key=lambda t: out[f"cy_2024_{t}"])
    out["best_2024_asset"] = best_2024
    out["best_2024_return"] = out[f"cy_2024_{best_2024}"]
    runner = sorted(TICKERS, key=lambda t: out[f"cy_2024_{t}"])[-2]
    out["runner_2024_asset"] = runner
    out["runner_2024_return"] = out[f"cy_2024_{runner}"]

    # Correlation of monthly returns, section 8
    out["corr_SPY_TLT"] = round(float(rets["SPY"].corr(rets["TLT"])), 2)
    price_window = prices.loc[PERIOD_START:PERIOD_END]          # month-end prices of the return months
    out["corr_SPY_TLT_price_levels"] = round(float(price_window["SPY"].corr(price_window["TLT"])), 2)

    # Cumulative return, rebalanced vs buy and hold, sections 3 and 5
    out["cum_rebalanced"] = round(((1 + port).prod() - 1) * 100, 1)
    base = prices.iloc[0]                                        # 2022-12-31 base prices
    last = prices.loc[:PERIOD_END].iloc[-1]                      # last price in the period
    out["cum_buyhold"] = round(float(((last / base) * 0.25).sum() - 1) * 100, 1)

    # Max drawdown, section 7
    index = (1 + port).cumprod()
    drawdown = index / index.cummax() - 1
    out["mdd"] = round(float(drawdown.min()) * 100, 1)
    out["mdd_month"] = str(drawdown.idxmin())

    # Annualised volatility, section 6
    for t in TICKERS:
        out[f"vol_{t}"] = round(float(rets[t].std(ddof=1) * 12 ** 0.5) * 100, 1)
    out["vol_PORT"] = round(float(port.std(ddof=1) * 12 ** 0.5) * 100, 1)
    out["sharpe_PORT"] = round(float(port.mean() * 12 / (port.std(ddof=1) * 12 ** 0.5)), 2)

    # Best and worst months, section 9
    out["worst_month"] = str(port.idxmin())
    out["worst_month_return"] = round(float(port.min()) * 100, 1)
    out["best_month"] = str(port.idxmax())
    out["best_month_return"] = round(float(port.max()) * 100, 1)
    p26 = port.loc["2026"]
    out["best_2026_month"] = str(p26.idxmax())
    out["best_2026_return"] = round(float(p26.max()) * 100, 1)
    out["worst_2026_month"] = str(p26.idxmin())
    out["worst_2026_return"] = round(float(p26.min()) * 100, 1)
    return out


def render(answers: dict) -> str:
    text = TEMPLATE.read_text()
    for key, value in answers.items():
        text = text.replace("{{" + key + "}}", str(value))
    leftover = [line for line in text.splitlines() if "{{" in line]
    if leftover:
        raise SystemExit("unfilled placeholders:\n" + "\n".join(leftover))
    return text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    answers = compute()
    if args.json:
        print(json.dumps(answers, indent=2))
    elif args.render:
        QUESTIONS.write_text(render(answers))
        print(f"wrote {QUESTIONS.relative_to(ROOT)} from {TEMPLATE.relative_to(ROOT)}")
    else:
        width = max(len(k) for k in answers)
        for key, value in answers.items():
            print(f"{key:<{width}}  {value}")


if __name__ == "__main__":
    main()
