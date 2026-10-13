# Methodology: how the desk computes every number

State, not instructions. This is the one home for every convention. Load it before answering any question that involves a number, and name the section you used.

## 1. What the dataset is

- File: `reference/data/monthly-adjusted-close.csv`. Columns: `Date`, `SPY`, `TLT`, `GLD`, `USO`.
- `Date` is the calendar month end. The price on that row is the adjusted close of the last trading day in that month.
- Prices are Yahoo Finance adjusted closes (dividends and splits applied), rounded to four decimals, retrieved with `tools/fetch_data.py`. The fetch time is in `reference/data/fetch-log.txt`.
- The first row, 2022-12-31, is a base price only. Return months run from 2023-01 to 2026-09, 45 months in all.
- The four assets stand for: SPY US stocks, TLT US long-term Treasury bonds, GLD gold, USO oil.

## 2. Monthly return

Simple return: price this month end divided by price last month end, minus one. Not log returns. Computed per asset from adjusted close.

## 3. The house portfolio

Equal weight, 25 percent in each of the four assets, rebalanced back to equal weight at every month end. Its monthly return is therefore the plain average of the four assets' monthly returns in that month.

Buy and hold is a different portfolio and not the house portfolio: 25 percent in each asset bought at the 2022-12-31 prices and never rebalanced. When a question says "the portfolio" without qualification it means the house portfolio.

## 4. Calendar-year total return

Compound the twelve monthly returns of that year: multiply (1 + each monthly return), subtract one. Only 2023, 2024 and 2025 are complete years. 2026 runs January to September only and is reported as year to date, never as a calendar-year return.

## 5. Cumulative return over a period

Multiply (1 + each monthly return) across the period, subtract one. "The full period" means 2023-01 to 2026-09.

## 6. Annualised volatility

Sample standard deviation of the monthly returns (divide by n minus 1) multiplied by the square root of 12.

For the Sharpe ratio, annualised return is the arithmetic mean of monthly returns multiplied by 12, the risk-free rate is zero, and Sharpe is annualised return divided by annualised volatility. This is a stated simplification, not a claim about the right risk-free rate.

## 7. Maximum drawdown

Build the cumulative index: start at 1.00 on 2022-12-31 and multiply by (1 + monthly return) each month. Drawdown in a month is the index divided by its running peak, minus one. Maximum drawdown is the most negative drawdown; the trough month is the month in which it occurs.

## 8. Correlation

Pearson correlation of monthly returns over the stated period. Never of price levels. Correlating price levels is the common mistake this section exists to stop.

## 9. Best and worst month

The largest and smallest monthly return in the stated period, for an asset or for the house portfolio.

## 10. Rounding and format

Returns, volatility and drawdowns in percent to one decimal. Sharpe ratios and correlations to two decimals. Months as YYYY-MM.

## 11. Outside the dataset

Any month before 2023-01 or after 2026-09 is not in the dataset. The answer is "not in the dataset; the data ends 2026-09-30", with no number, no estimate, and no figure from memory.

## 12. What this file never does

It never holds a computed answer. Answers come from the data through these rules at the moment they are asked.
