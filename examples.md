# Examples: the shape of a right answer, and one wrong one

Instructions, not state. Load when unsure how an answer should look. None of these questions is one of the committed test questions. The numbers come from the price file and can be checked under the methodology.

## What does a complete answer look like?

Question: What was the total return (dividends reinvested) of TLT in calendar year 2023?

Answer:

Calendar-year total return compounds the twelve monthly simple returns of 2023 (methodology sections 2 and 4). Inputs: the TLT column, rows 2022-12-31 through 2023-12-31, thirteen prices.

```
import csv
rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
prices = [float(r["TLT"]) for r in rows if "2022-12-31" <= r["Date"] <= "2023-12-31"]
returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
total = 1
for r in returns:
    total *= 1 + r
print(len(prices), round((total - 1) * 100, 1))      # prints 13 2.8
```

`ANSWER: 2.8% | METHOD: methodology section 4 | SOURCE: monthly-adjusted-close.csv, TLT, rows 2022-12-31 to 2023-12-31`

## What does a right refusal look like?

Question: What was GLD's return in December 2022?

Answer:

The file's first row, 2022-12-31, is a base price only; the first return month is 2023-01 (methodology section 1). December 2022 has no return in this data, so there is no number to give.

`ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`

## What does a wrong answer look like, and why?

Question: What was the annualised volatility of SPY's monthly returns in calendar year 2024?

Wrong:

"SPY's volatility in 2024 was around 12 to 13%, which is typical for the S&P 500 in a calm year."

Why it fails: no code was run (rule 1); no rows are named (rule 3); a range instead of one rounded figure (rule 4); no answer line (rule 9); and the figure comes from memory of markets (rule 11). It also happens to be wrong.

Right:

Annualised volatility is the sample standard deviation of the twelve monthly returns of 2024 times the square root of 12 (methodology section 6). Inputs: the SPY column, rows 2023-12-31 through 2024-12-31.

```
import csv
rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
prices = [float(r["SPY"]) for r in rows if "2023-12-31" <= r["Date"] <= "2024-12-31"]
returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
mean = sum(returns) / len(returns)
var = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
print(len(returns), round(var ** 0.5 * 12 ** 0.5 * 100, 1))   # prints 12 10.7
```

`ANSWER: 10.7% | METHOD: methodology section 6 | SOURCE: monthly-adjusted-close.csv, SPY, rows 2023-12-31 to 2024-12-31`

## What these examples never do

They never stand in for the methodology, they never carry a convention of their own, and none of them is one of the committed test questions.
