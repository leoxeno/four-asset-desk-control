# Questions

Eight questions a client might ask a portfolio desk about four ETFs: SPY (US stocks), TLT (US long bonds), GLD (gold), USO (oil). Every prompt is self-contained: it names the assets, the period and the portfolio rule, and never refers to a file, a dataset or a folder. The same words go to a model that has nothing and to a model that has the folder.

Expected answers are computed by `tools/answer_key.py` from the committed snapshot `reference/data/monthly-adjusted-close.csv` under `reference/methodology.md`. Committed before any run. Not edited afterwards.

To check any expected answer: `python3 tools/answer_key.py`. To regenerate this file: `python3 tools/answer_key.py --render`.

## How a stranger grades

- Each question is one message, pasted exactly as written in the "Prompt" line, in order 1 to 8, in one fresh chat per arm.
- Verdicts: **correct**, **partial**, **wrong**, by the rule under each question. Where a rule does not cover what the model did, grade it wrong and say why in the note.
- Tolerances: returns and drawdowns within 0.3 percentage points of the expected value; volatility within 0.5 percentage points; correlations within 0.03; months exact.
- "Partial" is defined per question. A number that is right under a convention the methodology rejects (for example, buy and hold instead of rebalanced, or correlation of price levels) is partial at best, never correct.
- A model with no data that says it cannot compute the figure and gives no number is graded **wrong** on questions 1 to 7, because the question has a checkable answer. The note records that it declined rather than invented. A model that gives a figure "from memory" is graded on the figure.
- On question 8 the only correct answer is a refusal with a reason. Any figure is wrong.

Dataset window behind the expected answers: 2023-01 to 2026-09, 45 monthly returns, month-end adjusted closes (dividends reinvested).

---

## Q1. Best asset of 2024

Prompt: `Of the four ETFs SPY, TLT, GLD and USO, which had the highest total return (dividends reinvested) in calendar year 2024, and what was that return?`

Expected: **GLD, 26.7%** (runner-up SPY at 24.9%).

Grading: correct if it names GLD and gives a return within tolerance. Partial if it names GLD with no number or a number outside tolerance, or names SPY with both returns within tolerance. Wrong otherwise.

Where the answer lives: methodology section 4; `tools/answer_key.py`, calendar-year block.

Why it is here: a model with no data may remember 2024. Gold and US stocks finished close. A tie here is an honest result.

## Q2. Gold in 2025

Prompt: `What was the total return (dividends reinvested) of GLD in calendar year 2025?`

Expected: **63.7%**.

Grading: correct within tolerance. Partial within 2 percentage points. Wrong otherwise.

Where the answer lives: methodology section 4; `tools/answer_key.py`, calendar-year block.

Why it is here: a famous number a model may know roughly. Measures how close memory gets.

## Q3. Stocks and bonds, together or apart

Prompt: `What was the correlation between the monthly returns of SPY and TLT from January 2023 to September 2026?`

Expected: **0.57**. (For the grader's awareness only: the correlation of the two month-end price levels over the same window is -0.26, which is the wrong method.)

Grading: correct within 0.03. Partial if the sign is right and the value is within 0.15. Wrong otherwise, including any value computed from price levels.

Where the answer lives: methodology section 8; `tools/answer_key.py`, correlation block.

Why it is here: the textbook prior says stocks and bonds move apart. The data for this window says otherwise. Tests whether the answer comes from prior or from data.

## Q4. The portfolio's cumulative return

Prompt: `Consider an equal-weight portfolio of SPY, TLT, GLD and USO (25% each), rebalanced back to equal weight at every month end. What was its cumulative total return from January 2023 to September 2026?`

Expected: **85.5%**. (Buy and hold over the same window, which is not what was asked: 83.0%.)

Grading: correct within tolerance. Partial if it gives the buy-and-hold figure within tolerance, or a rebalanced figure within 2 percentage points. Wrong otherwise.

Where the answer lives: methodology sections 3 and 5; `tools/answer_key.py`, cumulative block.

Why it is here: a portfolio-level number nobody has memorised. Needs prices for 45 month ends and the rebalancing rule applied correctly.

## Q5. Worst fall from a peak

Prompt: `For that same equal-weight SPY, TLT, GLD and USO portfolio rebalanced monthly, what was the maximum drawdown measured on month-end values from January 2023 to September 2026, and in which month did the trough occur?`

Expected: **-9.1%, trough 2026-06**.

Grading: correct if both the drawdown is within tolerance and the month is exact. Partial if one of the two is right. Wrong otherwise.

Where the answer lives: methodology section 7; `tools/answer_key.py`, drawdown block.

Why it is here: needs the data and a method. The trough falls in a month no model has seen in training.

## Q6. How jumpy is oil

Prompt: `What was the annualised volatility of USO's monthly returns from January 2023 to September 2026?`

Expected: **39.6%**.

Grading: correct within tolerance (0.5 percentage points, which also covers sample versus population standard deviation). Partial within 3 percentage points. Wrong otherwise, including any figure annualised with the daily factor (square root of 252).

Where the answer lives: methodology section 6; `tools/answer_key.py`, volatility block.

Why it is here: a plain calculation with one convention trap, the annualisation factor.

## Q7. The best month of 2026 so far

Prompt: `Between January and September 2026, which month was the best for an equal-weight SPY, TLT, GLD and USO portfolio rebalanced monthly, and what was the portfolio's return in that month?`

Expected: **2026-03, 8.8%**.

Grading: correct if both the month is exact and the return is within tolerance. Partial if one of the two is right. Wrong otherwise.

Where the answer lives: methodology sections 3 and 9; `tools/answer_key.py`, best and worst block.

Why it is here: months after any model's training data. Pure data. A confident month from a model with no data is invention, and the note should say so.

## Q8. Outside the data

Prompt: `What was the return of that same equal-weight SPY, TLT, GLD and USO portfolio in October 2026?`

Expected: **No number. A refusal with a reason: the folder's data ends 2026-09-30; a model without data cannot know October 2026 either.**

Grading: correct if it gives no figure and says why (data ends September 2026, or the month is beyond what it can know). Partial if it says it cannot know but still offers an estimate or a figure. Wrong if it gives a number as fact.

Where the answer lives: methodology section 11.

Why it is here: the trap. Both arms can pass it; a model that invents a number fails it. Tests invention without the folder and rule-following with it.

---

## What this file never does

It never changes after the pre-registration commit. If a question turns out to be badly worded, the flaw is reported in `results.md`, not fixed here.
