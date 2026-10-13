# Four-asset desk: the map

Instructions, not state. Read this first, every time, then go where the table sends you.

One sentence: this folder answers numeric questions about four ETFs, SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from one month-end price file under one written methodology, and says plainly when the data does not cover the question.

## What is this, what do I do next, where does the information come from, what breaks it?

- What: a desk that turns a plain question into one checkable number with its method and its rows.
- Next: read `identity.md` (the job), then `rules.md` (what must be true of every answer), then compute from `reference/`.
- Information: only `reference/`. The price file holds the prices, the data dictionary says what the columns are, the methodology holds every convention. Nothing comes from memory of markets.
- Breaks: months outside the window the methodology defines, assets not in the file, anything needing daily prices, and any request for a forecast or advice.

## Where things live

| Path | What it holds | Kind |
|------|---------------|------|
| `identity.md` | the job, who asks, what goes out, what breaks it | instructions |
| `rules.md` | numbered pass conditions and the exact shape of the answer line | instructions |
| `examples.md` | two right answers and one wrong one, with why | instructions |
| `reference/methodology.md` | every convention, one section per quantity; the one home for every fact | state |
| `reference/data/data-dictionary.md` | columns, source, coverage of the price file | state |
| `reference/data/monthly-adjusted-close.csv` | month-end adjusted closes, SPY TLT GLD USO | state |

## Route by what was asked

| If the question asks for | Read | Then stop at |
|--------------------------|------|--------------|
| a return, volatility, Sharpe, drawdown, correlation, best or worst month, for an asset or the equal-weight portfolio | `rules.md`, the methodology section from the table below, the price file | the ANSWER line |
| a month before or after the data window | `reference/methodology.md` section 11 | a refusal with the reason, no number |
| an asset not in the file, daily data, a forecast, or what to buy | `identity.md`, last section | a one-line decline |
| how an answer should look | `examples.md` | the matching example |

## Which methodology section

| Quantity | Section | Quantity | Section |
|----------|---------|----------|---------|
| what the file is, the window | 1 | annualised volatility, Sharpe | 6 |
| monthly return | 2 | maximum drawdown | 7 |
| the equal-weight portfolio | 3 | correlation | 8 |
| calendar-year return | 4 | best and worst month | 9 |
| cumulative return | 5 | rounding; outside the data | 10; 11 |

## The one rule

Every number comes from code run on the price file, under the methodology, and the answer line names the section and the rows. No number from memory, ever.

## Size

Roughly, in tokens: this map 550, identity 350, rules 550, examples 750, methodology 800, data dictionary 300, price file 1,000. Map plus rules plus one question's inputs lands near 3,000.
