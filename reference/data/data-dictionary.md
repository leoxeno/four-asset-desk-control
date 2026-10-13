# Data dictionary: monthly-adjusted-close.csv

State, not instructions. Read this to know what each column is and where it came from.

## Where it came from

Yahoo Finance end-of-day prices, retrieved with `tools/fetch_data.py` (yfinance, no API key). The exact retrieval time, library versions and row counts are appended to `fetch-log.txt` on every fetch. The committed CSV is the dataset of record. Yahoo adjusts prices retroactively for later dividends and splits, so a re-fetch on another day can differ slightly.

## Columns

| Column | Meaning |
|--------|---------|
| `Date` | Calendar month end, YYYY-MM-DD. The row holds the last trading day's adjusted close in that month. |
| `SPY` | SPDR S&P 500 ETF, adjusted close in US dollars. Stands for US stocks. |
| `TLT` | iShares 20+ Year Treasury Bond ETF, adjusted close in US dollars. Stands for US long bonds. |
| `GLD` | SPDR Gold Shares, adjusted close in US dollars. Stands for gold. |
| `USO` | United States Oil Fund, adjusted close in US dollars. Stands for oil. |

## Coverage

- First row 2022-12-31: base price only.
- Return months: 2023-01 to 2026-09, 45 months.
- Nothing after 2026-09-30 exists in this dataset.

## What this file never does

It never defines how to compute anything. Conventions live in `reference/methodology.md`.
