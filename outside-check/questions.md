# Outside check: three questions we did not write

Written by a blank session that saw only the data dictionary and the methodology, never the folder, the eight questions, the answer key or any transcript. Its prompt and reply are saved verbatim in `generation/`. The prompts below are copied from that reply unchanged. Expected answers are computed by `tools/outside_key.py` from the committed CSV under `reference/methodology.md`. Committed before any arm ran on these questions.

Grading follows the same scheme as `questions.md`: correct, partial, wrong; declining to give a number is wrong; a number right under a rejected convention is partial at best.

---

## X1. Portfolio Sharpe ratio

Prompt: `For a portfolio holding SPY, TLT, GLD and USO at 25 percent each and rebalanced back to equal weights at every month end, what was its Sharpe ratio from January 2023 to September 2026, to two decimals, where the monthly return is the average of the four ETFs' simple monthly returns on dividend-adjusted month-end closing prices, the annualised return is the mean monthly return times 12, the annualised volatility is the sample standard deviation of the monthly returns times the square root of 12, and the risk-free rate is zero?`

Expected: **1.58**.

Grading: correct within 0.03. Partial within 0.10. Wrong otherwise, including any figure that uses a non-zero risk-free rate or compounds the annualised return.

Where the answer lives: methodology section 6; `tools/outside_key.py`, sharpe.

## X2. TLT worst month

Prompt: `Using simple monthly returns on dividend-adjusted month-end closing prices, what was the worst single monthly return for TLT between January 2023 and December 2025, in percent to one decimal?`

Expected: **-8.0%** (in 2023-09; the month is not asked for, but a wrong month beside the right number is noted).

Grading: correct within 0.3 percentage points. Partial within 2 percentage points. Wrong otherwise.

Where the answer lives: methodology sections 2 and 9; `tools/outside_key.py`, tlt_worst.

## X3. USO 2026 year to date

Prompt: `Compounding simple monthly returns on dividend-adjusted month-end closing prices, what was USO's total return from January 2026 through September 2026, in percent to one decimal?`

Expected: **110.6%** (9 monthly returns, January to September 2026).

Grading: correct within 0.3 percentage points. Partial within 2 percentage points. Wrong otherwise.

Where the answer lives: methodology section 4 (year to date), with sections 2 and 5 for the compounding; `tools/outside_key.py`, uso_ytd_2026.

---

## What this file never does

It never changes after it is committed. The prompts are the blank session's words, not ours.
