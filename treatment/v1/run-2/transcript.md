Arm: treatment
Run: 2
Started: 2026-10-13T16:09:48+01:00
Finished: 2026-10-13T16:10:17+01:00
Model: claude-opus-5-5  Effort: high  Claude Code: 2.1.293 (Claude Code)
Tools: Bash,Read,Write,Glob,Grep  Sandbox: {"sandbox": {"enabled": true, "failIfUnavailable": true, "allowUnsandboxedCommands": false, "autoAllowBashIfSandboxed": true, "network": {"allowedDomains": [], "strictAllowlist": true, "allowUnixSockets": [], "allowLocalBinding": false}, "filesystem": {"allowWrite": ["."], "denyRead": ["/root", "/home", "/mnt", "/tmp", "/var/tmp"]}}, "permissions": {"blockReadsOutsideWorkingDirectories": true}}
Working directory contents: ['README.md', 'examples.md', 'identity.md', 'reference/data/data-dictionary.md', 'reference/data/fetch-log.txt', 'reference/data/monthly-adjusted-close.csv', 'reference/methodology.md', 'rules.md']
Repo commit when run: f274783
System prompt (verbatim):
```
Answer the user's question. Read README.md first and follow it.
```

Nothing below is edited. Tool calls and tool results are shown as the event stream delivered them.

## Q1

**Prompt (verbatim):** Of the four ETFs SPY, TLT, GLD and USO, which had the highest total return (dividends reinvested) in calendar year 2024, and what was that return?

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-csgppnzp/README.md"}

[tool result]
```
1	# Four-asset desk: the map
2	
3	Instructions, not state. Read this first, every time, then go where the table sends you.
4	
5	One sentence: this folder answers numeric questions about four ETFs, SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from one month-end price file under one written methodology, and says plainly when the data does not cover the question.
6	
7	## What is this, what do I do next, where does the information come from, what breaks it?
8	
9	- What: a desk that turns a plain question into one checkable number with its method and its rows.
10	- Next: read `identity.md` (the job), then `rules.md` (what must be true of every answer), then compute from `reference/`.
11	- Information: only `reference/`. The price file holds the prices, the data dictionary says what the columns are, the methodology holds every convention. Nothing comes from memory of markets.
12	- Breaks: months outside the window the methodology defines, assets not in the file, anything needing daily prices, and any request for a forecast or advice.
13	
14	## Where things live
15	
16	| Path | What it holds | Kind |
17	|------|---------------|------|
18	| `identity.md` | the job, who asks, what goes out, what breaks it | instructions |
19	| `rules.md` | numbered pass conditions and the exact shape of the answer line | instructions |
20	| `examples.md` | two right answers and one wrong one, with why | instructions |
21	| `reference/methodology.md` | every convention, one section per quantity; the one home for every fact | state |
22	| `reference/data/data-dictionary.md` | columns, source, coverage of the price file | state |
23	| `reference/data/monthly-adjusted-close.csv` | month-end adjusted closes, SPY TLT GLD USO | state |
24	
25	## Route by what was asked
26	
27	| If the question asks for | Read | Then stop at |
28	|--------------------------|------|--------------|
29	| a return, volatility, Sharpe, drawdown, correlation, best or worst month, for an asset or the equal-weight portfolio | `rules.md`, the methodology section from the table below, the price file | the ANSWER line |
30	| a month before or after the data window | `reference/methodology.md` section 11 | a refusal with the reason, no number |
31	| an asset not in the file, daily data, a forecast, or what to buy | `identity.md`, last section | a one-line decline |
32	| how an answer should look | `examples.md` | the matching example |
33	
34	## Which methodology section
35	
36	| Quantity | Section | Quantity | Section |
37	|----------|---------|----------|---------|
38	| what the file is, the window | 1 | annualised volatility, Sharpe | 6 |
39	| monthly return | 2 | maximum drawdown | 7 |
40	| the equal-weight portfolio | 3 | correlation | 8 |
41	| calendar-year return | 4 | best and worst month | 9 |
42	| cumulative return | 5 | rounding; outside the data | 10; 11 |
43	
44	## The one rule
45	
46	Every number comes from code run on the price file, under the methodology, and the answer line names the section and the rows. No number from memory, ever.
47	
48	## Size
49	
50	Roughly, in tokens: this map 550, identity 350, rules 550, examples 750, methodology 800, data dictionary 300, price file 1,000. Map plus rules plus one question's inputs lands near 3,000.
51	
```

[tool call: Bash] {"command": "ls -la /srv/comp14-runs/treatment-csgppnzp", "description": "List files in working directory"}

[tool result]
```
total 28
drwx------ 4 root root 4096 Oct 13 16:10 .
drwx------ 3 root root   60 Oct 13 16:10 ..
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bash_profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bashrc
drwxr-xr-x 3 root root 4096 Oct 13 16:10 .claude
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitconfig
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitmodules
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .idea
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .mcp.json
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .ripgreprc
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .vscode
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zprofile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zshrc
-rw-r--r-- 1 root root 3136 Oct 13 16:09 README.md
-rw-r--r-- 1 root root 2862 Oct 13 16:09 examples.md
-rw-r--r-- 1 root root 1829 Oct 13 16:09 identity.md
drwxr-xr-x 3 root root 4096 Oct 13 16:09 reference
-rw-r--r-- 1 root root 2264 Oct 13 16:09 rules.md
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-csgppnzp/identity.md"}

[tool result]
```
1	# Identity: the four-asset desk
2	
3	Instructions, not state. Load this right after the README, in every chat.
4	
5	One job: answer numeric questions about SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from the month-end price file under the methodology, and say plainly when the data does not cover the question.
6	
7	## Who asks, and what do they get?
8	
9	A client or a colleague who wants one number they can check. They get the number, the convention it rests on, the rows it came from, and nothing else. They do not get an opinion on markets.
10	
11	## What comes in?
12	
13	A question in plain words. It may name a period, a weighting, a rebalancing rule or a quantity. It may be silent on some of those. It may ask about a month, an asset or a kind of data the file does not have.
14	
15	## What goes out?
16	
17	A short working, the code that produced the number with its printed result, and one final line in the shape fixed in `rules.md`. Or, when the data does not cover the question, a refusal with the reason and no number.
18	
19	## Where does the information come from?
20	
21	Only from `reference/`: the price file, its data dictionary, and the methodology. The methodology is the one home for every convention, and this file restates none of them. Memory of what markets did is not a source.
22	
23	## What breaks this desk?
24	
25	Questions about months outside the window the methodology defines. Questions that need daily or intraday prices. Questions about assets not in the file. Questions that ask what will happen, or what to buy, sell or hold. A chat in which code cannot run: then the desk says so and gives no number.
26	
27	## What this desk never does
28	
29	It never answers from memory of markets. It never picks a convention silently when the question is silent. It never gives a number for a month it does not have. It never gives investment advice.
30	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-csgppnzp/rules.md"}

[tool result]
```
1	# Rules: pass conditions for every answer
2	
3	Instructions, not state. Load after `identity.md`, before computing anything. Each rule is stated once. The conventions they point to live in `reference/methodology.md` and are not repeated here.
4	
5	## What must be true of every number?
6	
7	1. It was computed by code that reads `reference/data/monthly-adjusted-close.csv` directly, or rows copied from it verbatim. Never retype a price from memory, and never type a result from memory.
8	2. It follows the methodology section for that quantity. The README's section table says which one. The section number appears in the answer line.
9	3. Its inputs are stated: the columns used and the first and last row dates used.
10	4. It is rounded as methodology section 10 says, with its unit.
11	
12	## What if the question sets its own terms?
13	
14	5. If the question names a period, a weighting or a rebalancing rule, use exactly that. If it is silent, use the methodology's default and write "methodology default" in the working.
15	6. If the question asks for a quantity the methodology does not define, say so, define it in one sentence before computing, and write "ad hoc" in place of the section number.
16	
17	## What if the data does not cover it?
18	
19	7. Any month outside the window in methodology section 1 is answered per section 11: no number, no estimate, no figure from memory. A month after the window is refused exactly like a month before it.
20	8. Any asset not in the file, or any question that needs daily data, gets a one-line decline that says what the file does hold.
21	
22	## What shape does the answer take?
23	
24	9. Working first, short. Then the code and its printed result. Then one final line, exactly in this shape:
25	
26	   `ANSWER: <value with unit> | METHOD: methodology section <n> | SOURCE: monthly-adjusted-close.csv, <columns>, rows <first date> to <last date>`
27	
28	   For a refusal: `ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
29	
30	10. Prose outside the code and the answer line stays under 120 words. The client wants the number, not an essay.
31	
32	## What does this desk never do?
33	
34	11. Never fetch live prices, search the web, or use memory of market history. Never recommend buying, selling or holding anything. Never paste a key, a token or a password into a chat.
35	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-csgppnzp/examples.md"}

[tool result]
```
1	# Examples: the shape of a right answer, and one wrong one
2	
3	Instructions, not state. Load when unsure how an answer should look. None of these questions is one of the committed test questions. The numbers come from the price file and can be checked under the methodology.
4	
5	## What does a complete answer look like?
6	
7	Question: What was the total return (dividends reinvested) of TLT in calendar year 2023?
8	
9	Answer:
10	
11	Calendar-year total return compounds the twelve monthly simple returns of 2023 (methodology sections 2 and 4). Inputs: the TLT column, rows 2022-12-31 through 2023-12-31, thirteen prices.
12	
13	```
14	import csv
15	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
16	prices = [float(r["TLT"]) for r in rows if "2022-12-31" <= r["Date"] <= "2023-12-31"]
17	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
18	total = 1
19	for r in returns:
20	    total *= 1 + r
21	print(len(prices), round((total - 1) * 100, 1))      # prints 13 2.8
22	```
23	
24	`ANSWER: 2.8% | METHOD: methodology section 4 | SOURCE: monthly-adjusted-close.csv, TLT, rows 2022-12-31 to 2023-12-31`
25	
26	## What does a right refusal look like?
27	
28	Question: What was GLD's return in December 2022?
29	
30	Answer:
31	
32	The file's first row, 2022-12-31, is a base price only; the first return month is 2023-01 (methodology section 1). December 2022 has no return in this data, so there is no number to give.
33	
34	`ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
35	
36	## What does a wrong answer look like, and why?
37	
38	Question: What was the annualised volatility of SPY's monthly returns in calendar year 2024?
39	
40	Wrong:
41	
42	"SPY's volatility in 2024 was around 12 to 13%, which is typical for the S&P 500 in a calm year."
43	
44	Why it fails: no code was run (rule 1); no rows are named (rule 3); a range instead of one rounded figure (rule 4); no answer line (rule 9); and the figure comes from memory of markets (rule 11). It also happens to be wrong.
45	
46	Right:
47	
48	Annualised volatility is the sample standard deviation of the twelve monthly returns of 2024 times the square root of 12 (methodology section 6). Inputs: the SPY column, rows 2023-12-31 through 2024-12-31.
49	
50	```
51	import csv
52	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
53	prices = [float(r["SPY"]) for r in rows if "2023-12-31" <= r["Date"] <= "2024-12-31"]
54	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
55	mean = sum(returns) / len(returns)
56	var = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
57	print(len(returns), round(var ** 0.5 * 12 ** 0.5 * 100, 1))   # prints 12 10.7
58	```
59	
60	`ANSWER: 10.7% | METHOD: methodology section 6 | SOURCE: monthly-adjusted-close.csv, SPY, rows 2023-12-31 to 2024-12-31`
61	
62	## What these examples never do
63	
64	They never stand in for the methodology, they never carry a convention of their own, and none of them is one of the committed test questions.
65	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-csgppnzp/reference/methodology.md"}

[tool result]
```
1	# Methodology: how the desk computes every number
2	
3	State, not instructions. This is the one home for every convention. Load it before answering any question that involves a number, and name the section you used.
4	
5	## 1. What the dataset is
6	
7	- File: `reference/data/monthly-adjusted-close.csv`. Columns: `Date`, `SPY`, `TLT`, `GLD`, `USO`.
8	- `Date` is the calendar month end. The price on that row is the adjusted close of the last trading day in that month.
9	- Prices are Yahoo Finance adjusted closes (dividends and splits applied), rounded to four decimals, retrieved with `tools/fetch_data.py`. The fetch time is in `reference/data/fetch-log.txt`.
10	- The first row, 2022-12-31, is a base price only. Return months run from 2023-01 to 2026-09, 45 months in all.
11	- The four assets stand for: SPY US stocks, TLT US long-term Treasury bonds, GLD gold, USO oil.
12	
13	## 2. Monthly return
14	
15	Simple return: price this month end divided by price last month end, minus one. Not log returns. Computed per asset from adjusted close.
16	
17	## 3. The house portfolio
18	
19	Equal weight, 25 percent in each of the four assets, rebalanced back to equal weight at every month end. Its monthly return is therefore the plain average of the four assets' monthly returns in that month.
20	
21	Buy and hold is a different portfolio and not the house portfolio: 25 percent in each asset bought at the 2022-12-31 prices and never rebalanced. When a question says "the portfolio" without qualification it means the house portfolio.
22	
23	## 4. Calendar-year total return
24	
25	Compound the twelve monthly returns of that year: multiply (1 + each monthly return), subtract one. Only 2023, 2024 and 2025 are complete years. 2026 runs January to September only and is reported as year to date, never as a calendar-year return.
26	
27	## 5. Cumulative return over a period
28	
29	Multiply (1 + each monthly return) across the period, subtract one. "The full period" means 2023-01 to 2026-09.
30	
31	## 6. Annualised volatility
32	
33	Sample standard deviation of the monthly returns (divide by n minus 1) multiplied by the square root of 12.
34	
35	For the Sharpe ratio, annualised return is the arithmetic mean of monthly returns multiplied by 12, the risk-free rate is zero, and Sharpe is annualised return divided by annualised volatility. This is a stated simplification, not a claim about the right risk-free rate.
36	
37	## 7. Maximum drawdown
38	
39	Build the cumulative index: start at 1.00 on 2022-12-31 and multiply by (1 + monthly return) each month. Drawdown in a month is the index divided by its running peak, minus one. Maximum drawdown is the most negative drawdown; the trough month is the month in which it occurs.
40	
41	## 8. Correlation
42	
43	Pearson correlation of monthly returns over the stated period. Never of price levels. Correlating price levels is the common mistake this section exists to stop.
44	
45	## 9. Best and worst month
46	
47	The largest and smallest monthly return in the stated period, for an asset or for the house portfolio.
48	
49	## 10. Rounding and format
50	
51	Returns, volatility and drawdowns in percent to one decimal. Sharpe ratios and correlations to two decimals. Months as YYYY-MM.
52	
53	## 11. Outside the dataset
54	
55	Any month before 2023-01 or after 2026-09 is not in the dataset. The answer is "not in the dataset; the data ends 2026-09-30", with no number, no estimate, and no figure from memory.
56	
57	## 12. What this file never does
58	
59	It never holds a computed answer. Answers come from the data through these rules at the moment they are asked.
60	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-csgppnzp/reference/data/data-dictionary.md"}

[tool result]
```
1	# Data dictionary: monthly-adjusted-close.csv
2	
3	State, not instructions. Read this to know what each column is and where it came from.
4	
5	## Where it came from
6	
7	Yahoo Finance end-of-day prices, retrieved with `tools/fetch_data.py` (yfinance, no API key). The exact retrieval time, library versions and row counts are appended to `fetch-log.txt` on every fetch. The committed CSV is the dataset of record. Yahoo adjusts prices retroactively for later dividends and splits, so a re-fetch on another day can differ slightly.
8	
9	## Columns
10	
11	| Column | Meaning |
12	|--------|---------|
13	| `Date` | Calendar month end, YYYY-MM-DD. The row holds the last trading day's adjusted close in that month. |
14	| `SPY` | SPDR S&P 500 ETF, adjusted close in US dollars. Stands for US stocks. |
15	| `TLT` | iShares 20+ Year Treasury Bond ETF, adjusted close in US dollars. Stands for US long bonds. |
16	| `GLD` | SPDR Gold Shares, adjusted close in US dollars. Stands for gold. |
17	| `USO` | United States Oil Fund, adjusted close in US dollars. Stands for oil. |
18	
19	## Coverage
20	
21	- First row 2022-12-31: base price only.
22	- Return months: 2023-01 to 2026-09, 45 months.
23	- Nothing after 2026-09-30 exists in this dataset.
24	
25	## What this file never does
26	
27	It never defines how to compute anything. Conventions live in `reference/methodology.md`.
28	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-csgppnzp/reference/data/monthly-adjusted-close.csv"}

[tool result]
```
1	Date,SPY,TLT,GLD,USO
2	2022-12-31,364.7676,85.5002,169.64,70.11
3	2023-01-31,387.7069,92.0355,179.41,69.32
4	2023-02-28,377.9589,87.5713,169.78,67.21
5	2023-03-31,391.9728,91.8092,183.22,66.44
6	2023-04-30,398.2345,92.1198,184.8,67.5
7	2023-05-31,400.0729,89.3421,182.32,60.63
8	2023-06-30,425.9975,89.5361,178.27,63.55
9	2023-07-31,439.9418,87.2581,182.35,73.17
10	2023-08-31,432.7919,84.5163,180.02,75.06
11	2023-09-30,412.2626,77.7964,171.45,80.86
12	2023-10-31,403.313,73.5462,184.09,75.02
13	2023-11-30,440.1531,80.8448,188.75,70.14
14	2023-12-31,460.2484,87.8668,191.17,66.65
15	2024-01-31,467.5785,85.8941,188.45,70.92
16	2024-02-29,491.9801,83.9596,189.31,73.36
17	2024-03-31,508.0688,84.6169,205.72,78.73
18	2024-04-30,487.5835,79.1545,211.87,78.38
19	2024-05-31,512.2454,81.4396,215.3,74.82
20	2024-06-30,530.3175,82.9195,215.01,79.59
21	2024-07-31,536.7392,85.9294,226.55,77.74
22	2024-08-31,549.2804,87.7436,231.29,74.34
23	2024-09-30,560.8178,89.498,243.06,69.92
24	2024-10-31,555.8132,84.616,253.51,73.08
25	2024-11-30,588.9584,86.2975,245.59,71.61
26	2024-12-31,574.788,80.7908,242.13,75.55
27	2025-01-31,590.2247,81.1886,258.56,78.02
28	2025-02-28,582.7319,85.814,263.27,75.22
29	2025-03-31,550.2626,84.7802,288.14,77.33
30	2025-04-30,545.4916,83.6268,303.77,63.56
31	2025-05-31,579.7731,80.9419,303.6,67.15
32	2025-06-30,609.5654,83.0982,304.83,73.11
33	2025-07-31,623.6046,82.1512,302.96,79.59
34	2025-08-31,636.4007,82.1616,318.07,74.84
35	2025-09-30,659.0695,85.112,355.47,73.75
36	2025-10-31,674.78,86.2875,368.12,72.56
37	2025-11-30,676.0959,86.5225,387.88,71.07
38	2025-12-31,676.635,84.2222,396.31,69.16
39	2026-01-31,686.6071,84.1932,444.95,79.52
40	2026-02-28,680.6734,88.0945,483.75,81.95
41	2026-03-31,647.0621,84.3681,430.29,127.25
42	2026-04-30,715.0377,83.6597,423.66,147.09
43	2026-05-31,752.6671,84.1059,417.12,129.09
44	2026-06-30,744.9202,85.0865,368.38,106.44
45	2026-07-31,745.1796,81.2799,371.54,129.17
46	2026-08-31,765.15,81.8752,408.42,133.7
47	2026-09-30,762.63,77.468,380.84,145.66
48	
```

[tool call: Bash] {"command": "python3 -I -c '\nimport csv\nrows = list(csv.DictReader(open(\"reference/data/monthly-adjusted-close.csv\")))\nsel = [r for r in rows if \"2023-12-31\" <= r[\"Date\"] <= \"2024-12-31\"]\nprint(len(sel), sel[0][\"Date\"], sel[-1][\"Date\"])\nfor a in [\"SPY\",\"TLT\",\"GLD\",\"USO\"]:\n    p = [float(r[a]) for r in sel]\n    t = 1\n    for x, y in zip(p, p[1:]):\n        t *= 1 + (y / x - 1)\n    print(a, len(p)-1, round((t - 1) * 100, 1))\n'", "description": "Compute 2024 calendar-year returns for four ETFs"}

[tool result]
```
13 2023-12-31 2024-12-31
SPY 12 24.9
TLT 12 -8.1
GLD 12 26.7
USO 12 13.4
```

GLD had the highest total return in 2024, at 26.7%. SPY was close behind at 24.9%.

To get each yearly figure, I worked out the twelve monthly returns for 2024 and compounded them (methodology sections 2 and 4). The prices are adjusted closes, so dividends are already counted as reinvested. I used the SPY, TLT, GLD and USO columns, from 2023-12-31 to 2024-12-31, which is thirteen prices for each fund.

```
import csv
rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
sel = [r for r in rows if "2023-12-31" <= r["Date"] <= "2024-12-31"]
for a in ["SPY","TLT","GLD","USO"]:
    p = [float(r[a]) for r in sel]
    t = 1
    for x, y in zip(p, p[1:]):
        t *= 1 + (y / x - 1)
    print(a, len(p)-1, round((t - 1) * 100, 1))
```
Output:
```
SPY 12 24.9
TLT 12 -8.1
GLD 12 26.7
USO 12 13.4
```

`ANSWER: GLD, 26.7% | METHOD: methodology section 4 | SOURCE: monthly-adjusted-close.csv, SPY TLT GLD USO, rows 2023-12-31 to 2024-12-31`

Status: ok; turns: 10; seconds: 28.2; tokens in/out: 8/1497; files read: ['/srv/comp14-runs/treatment-csgppnzp/README.md', '/srv/comp14-runs/treatment-csgppnzp/identity.md', '/srv/comp14-runs/treatment-csgppnzp/rules.md', '/srv/comp14-runs/treatment-csgppnzp/examples.md', '/srv/comp14-runs/treatment-csgppnzp/reference/methodology.md', '/srv/comp14-runs/treatment-csgppnzp/reference/data/data-dictionary.md', '/srv/comp14-runs/treatment-csgppnzp/reference/data/monthly-adjusted-close.csv']; bash calls: 2; asked to leave sandbox: 0

## Q2

**Prompt (verbatim):** What was the total return (dividends reinvested) of GLD in calendar year 2025?

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-4y9sqtug/README.md"}

[tool result]
```
1	# Four-asset desk: the map
2	
3	Instructions, not state. Read this first, every time, then go where the table sends you.
4	
5	One sentence: this folder answers numeric questions about four ETFs, SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from one month-end price file under one written methodology, and says plainly when the data does not cover the question.
6	
7	## What is this, what do I do next, where does the information come from, what breaks it?
8	
9	- What: a desk that turns a plain question into one checkable number with its method and its rows.
10	- Next: read `identity.md` (the job), then `rules.md` (what must be true of every answer), then compute from `reference/`.
11	- Information: only `reference/`. The price file holds the prices, the data dictionary says what the columns are, the methodology holds every convention. Nothing comes from memory of markets.
12	- Breaks: months outside the window the methodology defines, assets not in the file, anything needing daily prices, and any request for a forecast or advice.
13	
14	## Where things live
15	
16	| Path | What it holds | Kind |
17	|------|---------------|------|
18	| `identity.md` | the job, who asks, what goes out, what breaks it | instructions |
19	| `rules.md` | numbered pass conditions and the exact shape of the answer line | instructions |
20	| `examples.md` | two right answers and one wrong one, with why | instructions |
21	| `reference/methodology.md` | every convention, one section per quantity; the one home for every fact | state |
22	| `reference/data/data-dictionary.md` | columns, source, coverage of the price file | state |
23	| `reference/data/monthly-adjusted-close.csv` | month-end adjusted closes, SPY TLT GLD USO | state |
24	
25	## Route by what was asked
26	
27	| If the question asks for | Read | Then stop at |
28	|--------------------------|------|--------------|
29	| a return, volatility, Sharpe, drawdown, correlation, best or worst month, for an asset or the equal-weight portfolio | `rules.md`, the methodology section from the table below, the price file | the ANSWER line |
30	| a month before or after the data window | `reference/methodology.md` section 11 | a refusal with the reason, no number |
31	| an asset not in the file, daily data, a forecast, or what to buy | `identity.md`, last section | a one-line decline |
32	| how an answer should look | `examples.md` | the matching example |
33	
34	## Which methodology section
35	
36	| Quantity | Section | Quantity | Section |
37	|----------|---------|----------|---------|
38	| what the file is, the window | 1 | annualised volatility, Sharpe | 6 |
39	| monthly return | 2 | maximum drawdown | 7 |
40	| the equal-weight portfolio | 3 | correlation | 8 |
41	| calendar-year return | 4 | best and worst month | 9 |
42	| cumulative return | 5 | rounding; outside the data | 10; 11 |
43	
44	## The one rule
45	
46	Every number comes from code run on the price file, under the methodology, and the answer line names the section and the rows. No number from memory, ever.
47	
48	## Size
49	
50	Roughly, in tokens: this map 550, identity 350, rules 550, examples 750, methodology 800, data dictionary 300, price file 1,000. Map plus rules plus one question's inputs lands near 3,000.
51	
```

[tool call: Bash] {"command": "cd /srv/comp14-runs/treatment-4y9sqtug; cat identity.md rules.md examples.md reference/methodology.md reference/data/data-dictionary.md; cat reference/data/monthly-adjusted-close.csv", "description": "Read instructions, methodology, and price data"}

[tool result]
```
# Identity: the four-asset desk

Instructions, not state. Load this right after the README, in every chat.

One job: answer numeric questions about SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from the month-end price file under the methodology, and say plainly when the data does not cover the question.

## Who asks, and what do they get?

A client or a colleague who wants one number they can check. They get the number, the convention it rests on, the rows it came from, and nothing else. They do not get an opinion on markets.

## What comes in?

A question in plain words. It may name a period, a weighting, a rebalancing rule or a quantity. It may be silent on some of those. It may ask about a month, an asset or a kind of data the file does not have.

## What goes out?

A short working, the code that produced the number with its printed result, and one final line in the shape fixed in `rules.md`. Or, when the data does not cover the question, a refusal with the reason and no number.

## Where does the information come from?

Only from `reference/`: the price file, its data dictionary, and the methodology. The methodology is the one home for every convention, and this file restates none of them. Memory of what markets did is not a source.

## What breaks this desk?

Questions about months outside the window the methodology defines. Questions that need daily or intraday prices. Questions about assets not in the file. Questions that ask what will happen, or what to buy, sell or hold. A chat in which code cannot run: then the desk says so and gives no number.

## What this desk never does

It never answers from memory of markets. It never picks a convention silently when the question is silent. It never gives a number for a month it does not have. It never gives investment advice.
# Rules: pass conditions for every answer

Instructions, not state. Load after `identity.md`, before computing anything. Each rule is stated once. The conventions they point to live in `reference/methodology.md` and are not repeated here.

## What must be true of every number?

1. It was computed by code that reads `reference/data/monthly-adjusted-close.csv` directly, or rows copied from it verbatim. Never retype a price from memory, and never type a result from memory.
2. It follows the methodology section for that quantity. The README's section table says which one. The section number appears in the answer line.
3. Its inputs are stated: the columns used and the first and last row dates used.
4. It is rounded as methodology section 10 says, with its unit.

## What if the question sets its own terms?

5. If the question names a period, a weighting or a rebalancing rule, use exactly that. If it is silent, use the methodology's default and write "methodology default" in the working.
6. If the question asks for a quantity the methodology does not define, say so, define it in one sentence before computing, and write "ad hoc" in place of the section number.

## What if the data does not cover it?

7. Any month outside the window in methodology section 1 is answered per section 11: no number, no estimate, no figure from memory. A month after the window is refused exactly like a month before it.
8. Any asset not in the file, or any question that needs daily data, gets a one-line decline that says what the file does hold.

## What shape does the answer take?

9. Working first, short. Then the code and its printed result. Then one final line, exactly in this shape:

   `ANSWER: <value with unit> | METHOD: methodology section <n> | SOURCE: monthly-adjusted-close.csv, <columns>, rows <first date> to <last date>`

   For a refusal: `ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`

10. Prose outside the code and the answer line stays under 120 words. The client wants the number, not an essay.

## What does this desk never do?

11. Never fetch live prices, search the web, or use memory of market history. Never recommend buying, selling or holding anything. Never paste a key, a token or a password into a chat.
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
Date,SPY,TLT,GLD,USO
2022-12-31,364.7676,85.5002,169.64,70.11
2023-01-31,387.7069,92.0355,179.41,69.32
2023-02-28,377.9589,87.5713,169.78,67.21
2023-03-31,391.9728,91.8092,183.22,66.44
2023-04-30,398.2345,92.1198,184.8,67.5
2023-05-31,400.0729,89.3421,182.32,60.63
2023-06-30,425.9975,89.5361,178.27,63.55
2023-07-31,439.9418,87.2581,182.35,73.17
2023-08-31,432.7919,84.5163,180.02,75.06
2023-09-30,412.2626,77.7964,171.45,80.86
2023-10-31,403.313,73.5462,184.09,75.02
2023-11-30,440.1531,80.8448,188.75,70.14
2023-12-31,460.2484,87.8668,191.17,66.65
2024-01-31,467.5785,85.8941,188.45,70.92
2024-02-29,491.9801,83.9596,189.31,73.36
2024-03-31,508.0688,84.6169,205.72,78.73
2024-04-30,487.5835,79.1545,211.87,78.38
2024-05-31,512.2454,81.4396,215.3,74.82
2024-06-30,530.3175,82.9195,215.01,79.59
2024-07-31,536.7392,85.9294,226.55,77.74
2024-08-31,549.2804,87.7436,231.29,74.34
2024-09-30,560.8178,89.498,243.06,69.92
2024-10-31,555.8132,84.616,253.51,73.08
2024-11-30,588.9584,86.2975,245.59,71.61
2024-12-31,574.788,80.7908,242.13,75.55
2025-01-31,590.2247,81.1886,258.56,78.02
2025-02-28,582.7319,85.814,263.27,75.22
2025-03-31,550.2626,84.7802,288.14,77.33
2025-04-30,545.4916,83.6268,303.77,63.56
2025-05-31,579.7731,80.9419,303.6,67.15
2025-06-30,609.5654,83.0982,304.83,73.11
2025-07-31,623.6046,82.1512,302.96,79.59
2025-08-31,636.4007,82.1616,318.07,74.84
2025-09-30,659.0695,85.112,355.47,73.75
2025-10-31,674.78,86.2875,368.12,72.56
2025-11-30,676.0959,86.5225,387.88,71.07
2025-12-31,676.635,84.2222,396.31,69.16
2026-01-31,686.6071,84.1932,444.95,79.52
2026-02-28,680.6734,88.0945,483.75,81.95
2026-03-31,647.0621,84.3681,430.29,127.25
2026-04-30,715.0377,83.6597,423.66,147.09
2026-05-31,752.6671,84.1059,417.12,129.09
2026-06-30,744.9202,85.0865,368.38,106.44
2026-07-31,745.1796,81.2799,371.54,129.17
2026-08-31,765.15,81.8752,408.42,133.7
2026-09-30,762.63,77.468,380.84,145.66
```

[tool call: Bash] {"command": "cd /srv/comp14-runs/treatment-4y9sqtug; python3 -I -c '\nimport csv\nrows = list(csv.DictReader(open(\"reference/data/monthly-adjusted-close.csv\")))\nprices = [float(r[\"GLD\"]) for r in rows if \"2024-12-31\" <= r[\"Date\"] <= \"2025-12-31\"]\nreturns = [b / a - 1 for a, b in zip(prices, prices[1:])]\ntotal = 1\nfor r in returns:\n    total *= 1 + r\nprint(len(prices), round((total - 1) * 100, 1))\n'", "description": "Compute GLD 2025 calendar-year return"}

[tool result]
```
13 63.7
```

GLD returned 63.7% in calendar year 2025 (dividends reinvested). I got this by multiplying together (1 + each monthly simple return) for the twelve months of 2025 and subtracting one, as methodology sections 2 and 4 set out. The inputs were the GLD column, rows 2024-12-31 to 2025-12-31, which is thirteen month-end adjusted closes.

```
import csv
rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
prices = [float(r["GLD"]) for r in rows if "2024-12-31" <= r["Date"] <= "2025-12-31"]
returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
total = 1
for r in returns:
    total *= 1 + r
print(len(prices), round((total - 1) * 100, 1))      # prints 13 63.7
```

`ANSWER: 63.7% | METHOD: methodology section 4 | SOURCE: monthly-adjusted-close.csv, GLD, rows 2024-12-31 to 2025-12-31`

Status: ok; turns: 4; seconds: 21.3; tokens in/out: 8/929; files read: ['/srv/comp14-runs/treatment-4y9sqtug/README.md']; bash calls: 2; asked to leave sandbox: 0

## Q3

**Prompt (verbatim):** What was the correlation between the monthly returns of SPY and TLT from January 2023 to September 2026?

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-gjvkyx7_/README.md"}

[tool result]
```
1	# Four-asset desk: the map
2	
3	Instructions, not state. Read this first, every time, then go where the table sends you.
4	
5	One sentence: this folder answers numeric questions about four ETFs, SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from one month-end price file under one written methodology, and says plainly when the data does not cover the question.
6	
7	## What is this, what do I do next, where does the information come from, what breaks it?
8	
9	- What: a desk that turns a plain question into one checkable number with its method and its rows.
10	- Next: read `identity.md` (the job), then `rules.md` (what must be true of every answer), then compute from `reference/`.
11	- Information: only `reference/`. The price file holds the prices, the data dictionary says what the columns are, the methodology holds every convention. Nothing comes from memory of markets.
12	- Breaks: months outside the window the methodology defines, assets not in the file, anything needing daily prices, and any request for a forecast or advice.
13	
14	## Where things live
15	
16	| Path | What it holds | Kind |
17	|------|---------------|------|
18	| `identity.md` | the job, who asks, what goes out, what breaks it | instructions |
19	| `rules.md` | numbered pass conditions and the exact shape of the answer line | instructions |
20	| `examples.md` | two right answers and one wrong one, with why | instructions |
21	| `reference/methodology.md` | every convention, one section per quantity; the one home for every fact | state |
22	| `reference/data/data-dictionary.md` | columns, source, coverage of the price file | state |
23	| `reference/data/monthly-adjusted-close.csv` | month-end adjusted closes, SPY TLT GLD USO | state |
24	
25	## Route by what was asked
26	
27	| If the question asks for | Read | Then stop at |
28	|--------------------------|------|--------------|
29	| a return, volatility, Sharpe, drawdown, correlation, best or worst month, for an asset or the equal-weight portfolio | `rules.md`, the methodology section from the table below, the price file | the ANSWER line |
30	| a month before or after the data window | `reference/methodology.md` section 11 | a refusal with the reason, no number |
31	| an asset not in the file, daily data, a forecast, or what to buy | `identity.md`, last section | a one-line decline |
32	| how an answer should look | `examples.md` | the matching example |
33	
34	## Which methodology section
35	
36	| Quantity | Section | Quantity | Section |
37	|----------|---------|----------|---------|
38	| what the file is, the window | 1 | annualised volatility, Sharpe | 6 |
39	| monthly return | 2 | maximum drawdown | 7 |
40	| the equal-weight portfolio | 3 | correlation | 8 |
41	| calendar-year return | 4 | best and worst month | 9 |
42	| cumulative return | 5 | rounding; outside the data | 10; 11 |
43	
44	## The one rule
45	
46	Every number comes from code run on the price file, under the methodology, and the answer line names the section and the rows. No number from memory, ever.
47	
48	## Size
49	
50	Roughly, in tokens: this map 550, identity 350, rules 550, examples 750, methodology 800, data dictionary 300, price file 1,000. Map plus rules plus one question's inputs lands near 3,000.
51	
```

[tool call: Bash] {"command": "ls -la /srv/comp14-runs/treatment-gjvkyx7_", "description": "List working directory files"}

[tool result]
```
total 28
drwx------ 4 root root 4096 Oct 13 16:10 .
drwx------ 3 root root   60 Oct 13 16:10 ..
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bash_profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bashrc
drwxr-xr-x 3 root root 4096 Oct 13 16:10 .claude
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitconfig
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitmodules
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .idea
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .mcp.json
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .ripgreprc
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .vscode
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zprofile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zshrc
-rw-r--r-- 1 root root 3136 Oct 13 16:09 README.md
-rw-r--r-- 1 root root 2862 Oct 13 16:09 examples.md
-rw-r--r-- 1 root root 1829 Oct 13 16:09 identity.md
drwxr-xr-x 3 root root 4096 Oct 13 16:09 reference
-rw-r--r-- 1 root root 2264 Oct 13 16:09 rules.md
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-gjvkyx7_/identity.md"}

[tool result]
```
1	# Identity: the four-asset desk
2	
3	Instructions, not state. Load this right after the README, in every chat.
4	
5	One job: answer numeric questions about SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from the month-end price file under the methodology, and say plainly when the data does not cover the question.
6	
7	## Who asks, and what do they get?
8	
9	A client or a colleague who wants one number they can check. They get the number, the convention it rests on, the rows it came from, and nothing else. They do not get an opinion on markets.
10	
11	## What comes in?
12	
13	A question in plain words. It may name a period, a weighting, a rebalancing rule or a quantity. It may be silent on some of those. It may ask about a month, an asset or a kind of data the file does not have.
14	
15	## What goes out?
16	
17	A short working, the code that produced the number with its printed result, and one final line in the shape fixed in `rules.md`. Or, when the data does not cover the question, a refusal with the reason and no number.
18	
19	## Where does the information come from?
20	
21	Only from `reference/`: the price file, its data dictionary, and the methodology. The methodology is the one home for every convention, and this file restates none of them. Memory of what markets did is not a source.
22	
23	## What breaks this desk?
24	
25	Questions about months outside the window the methodology defines. Questions that need daily or intraday prices. Questions about assets not in the file. Questions that ask what will happen, or what to buy, sell or hold. A chat in which code cannot run: then the desk says so and gives no number.
26	
27	## What this desk never does
28	
29	It never answers from memory of markets. It never picks a convention silently when the question is silent. It never gives a number for a month it does not have. It never gives investment advice.
30	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-gjvkyx7_/rules.md"}

[tool result]
```
1	# Rules: pass conditions for every answer
2	
3	Instructions, not state. Load after `identity.md`, before computing anything. Each rule is stated once. The conventions they point to live in `reference/methodology.md` and are not repeated here.
4	
5	## What must be true of every number?
6	
7	1. It was computed by code that reads `reference/data/monthly-adjusted-close.csv` directly, or rows copied from it verbatim. Never retype a price from memory, and never type a result from memory.
8	2. It follows the methodology section for that quantity. The README's section table says which one. The section number appears in the answer line.
9	3. Its inputs are stated: the columns used and the first and last row dates used.
10	4. It is rounded as methodology section 10 says, with its unit.
11	
12	## What if the question sets its own terms?
13	
14	5. If the question names a period, a weighting or a rebalancing rule, use exactly that. If it is silent, use the methodology's default and write "methodology default" in the working.
15	6. If the question asks for a quantity the methodology does not define, say so, define it in one sentence before computing, and write "ad hoc" in place of the section number.
16	
17	## What if the data does not cover it?
18	
19	7. Any month outside the window in methodology section 1 is answered per section 11: no number, no estimate, no figure from memory. A month after the window is refused exactly like a month before it.
20	8. Any asset not in the file, or any question that needs daily data, gets a one-line decline that says what the file does hold.
21	
22	## What shape does the answer take?
23	
24	9. Working first, short. Then the code and its printed result. Then one final line, exactly in this shape:
25	
26	   `ANSWER: <value with unit> | METHOD: methodology section <n> | SOURCE: monthly-adjusted-close.csv, <columns>, rows <first date> to <last date>`
27	
28	   For a refusal: `ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
29	
30	10. Prose outside the code and the answer line stays under 120 words. The client wants the number, not an essay.
31	
32	## What does this desk never do?
33	
34	11. Never fetch live prices, search the web, or use memory of market history. Never recommend buying, selling or holding anything. Never paste a key, a token or a password into a chat.
35	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-gjvkyx7_/examples.md"}

[tool result]
```
1	# Examples: the shape of a right answer, and one wrong one
2	
3	Instructions, not state. Load when unsure how an answer should look. None of these questions is one of the committed test questions. The numbers come from the price file and can be checked under the methodology.
4	
5	## What does a complete answer look like?
6	
7	Question: What was the total return (dividends reinvested) of TLT in calendar year 2023?
8	
9	Answer:
10	
11	Calendar-year total return compounds the twelve monthly simple returns of 2023 (methodology sections 2 and 4). Inputs: the TLT column, rows 2022-12-31 through 2023-12-31, thirteen prices.
12	
13	```
14	import csv
15	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
16	prices = [float(r["TLT"]) for r in rows if "2022-12-31" <= r["Date"] <= "2023-12-31"]
17	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
18	total = 1
19	for r in returns:
20	    total *= 1 + r
21	print(len(prices), round((total - 1) * 100, 1))      # prints 13 2.8
22	```
23	
24	`ANSWER: 2.8% | METHOD: methodology section 4 | SOURCE: monthly-adjusted-close.csv, TLT, rows 2022-12-31 to 2023-12-31`
25	
26	## What does a right refusal look like?
27	
28	Question: What was GLD's return in December 2022?
29	
30	Answer:
31	
32	The file's first row, 2022-12-31, is a base price only; the first return month is 2023-01 (methodology section 1). December 2022 has no return in this data, so there is no number to give.
33	
34	`ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
35	
36	## What does a wrong answer look like, and why?
37	
38	Question: What was the annualised volatility of SPY's monthly returns in calendar year 2024?
39	
40	Wrong:
41	
42	"SPY's volatility in 2024 was around 12 to 13%, which is typical for the S&P 500 in a calm year."
43	
44	Why it fails: no code was run (rule 1); no rows are named (rule 3); a range instead of one rounded figure (rule 4); no answer line (rule 9); and the figure comes from memory of markets (rule 11). It also happens to be wrong.
45	
46	Right:
47	
48	Annualised volatility is the sample standard deviation of the twelve monthly returns of 2024 times the square root of 12 (methodology section 6). Inputs: the SPY column, rows 2023-12-31 through 2024-12-31.
49	
50	```
51	import csv
52	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
53	prices = [float(r["SPY"]) for r in rows if "2023-12-31" <= r["Date"] <= "2024-12-31"]
54	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
55	mean = sum(returns) / len(returns)
56	var = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
57	print(len(returns), round(var ** 0.5 * 12 ** 0.5 * 100, 1))   # prints 12 10.7
58	```
59	
60	`ANSWER: 10.7% | METHOD: methodology section 6 | SOURCE: monthly-adjusted-close.csv, SPY, rows 2023-12-31 to 2024-12-31`
61	
62	## What these examples never do
63	
64	They never stand in for the methodology, they never carry a convention of their own, and none of them is one of the committed test questions.
65	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-gjvkyx7_/reference/methodology.md"}

[tool result]
```
1	# Methodology: how the desk computes every number
2	
3	State, not instructions. This is the one home for every convention. Load it before answering any question that involves a number, and name the section you used.
4	
5	## 1. What the dataset is
6	
7	- File: `reference/data/monthly-adjusted-close.csv`. Columns: `Date`, `SPY`, `TLT`, `GLD`, `USO`.
8	- `Date` is the calendar month end. The price on that row is the adjusted close of the last trading day in that month.
9	- Prices are Yahoo Finance adjusted closes (dividends and splits applied), rounded to four decimals, retrieved with `tools/fetch_data.py`. The fetch time is in `reference/data/fetch-log.txt`.
10	- The first row, 2022-12-31, is a base price only. Return months run from 2023-01 to 2026-09, 45 months in all.
11	- The four assets stand for: SPY US stocks, TLT US long-term Treasury bonds, GLD gold, USO oil.
12	
13	## 2. Monthly return
14	
15	Simple return: price this month end divided by price last month end, minus one. Not log returns. Computed per asset from adjusted close.
16	
17	## 3. The house portfolio
18	
19	Equal weight, 25 percent in each of the four assets, rebalanced back to equal weight at every month end. Its monthly return is therefore the plain average of the four assets' monthly returns in that month.
20	
21	Buy and hold is a different portfolio and not the house portfolio: 25 percent in each asset bought at the 2022-12-31 prices and never rebalanced. When a question says "the portfolio" without qualification it means the house portfolio.
22	
23	## 4. Calendar-year total return
24	
25	Compound the twelve monthly returns of that year: multiply (1 + each monthly return), subtract one. Only 2023, 2024 and 2025 are complete years. 2026 runs January to September only and is reported as year to date, never as a calendar-year return.
26	
27	## 5. Cumulative return over a period
28	
29	Multiply (1 + each monthly return) across the period, subtract one. "The full period" means 2023-01 to 2026-09.
30	
31	## 6. Annualised volatility
32	
33	Sample standard deviation of the monthly returns (divide by n minus 1) multiplied by the square root of 12.
34	
35	For the Sharpe ratio, annualised return is the arithmetic mean of monthly returns multiplied by 12, the risk-free rate is zero, and Sharpe is annualised return divided by annualised volatility. This is a stated simplification, not a claim about the right risk-free rate.
36	
37	## 7. Maximum drawdown
38	
39	Build the cumulative index: start at 1.00 on 2022-12-31 and multiply by (1 + monthly return) each month. Drawdown in a month is the index divided by its running peak, minus one. Maximum drawdown is the most negative drawdown; the trough month is the month in which it occurs.
40	
41	## 8. Correlation
42	
43	Pearson correlation of monthly returns over the stated period. Never of price levels. Correlating price levels is the common mistake this section exists to stop.
44	
45	## 9. Best and worst month
46	
47	The largest and smallest monthly return in the stated period, for an asset or for the house portfolio.
48	
49	## 10. Rounding and format
50	
51	Returns, volatility and drawdowns in percent to one decimal. Sharpe ratios and correlations to two decimals. Months as YYYY-MM.
52	
53	## 11. Outside the dataset
54	
55	Any month before 2023-01 or after 2026-09 is not in the dataset. The answer is "not in the dataset; the data ends 2026-09-30", with no number, no estimate, and no figure from memory.
56	
57	## 12. What this file never does
58	
59	It never holds a computed answer. Answers come from the data through these rules at the moment they are asked.
60	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-gjvkyx7_/reference/data/data-dictionary.md"}

[tool result]
```
1	# Data dictionary: monthly-adjusted-close.csv
2	
3	State, not instructions. Read this to know what each column is and where it came from.
4	
5	## Where it came from
6	
7	Yahoo Finance end-of-day prices, retrieved with `tools/fetch_data.py` (yfinance, no API key). The exact retrieval time, library versions and row counts are appended to `fetch-log.txt` on every fetch. The committed CSV is the dataset of record. Yahoo adjusts prices retroactively for later dividends and splits, so a re-fetch on another day can differ slightly.
8	
9	## Columns
10	
11	| Column | Meaning |
12	|--------|---------|
13	| `Date` | Calendar month end, YYYY-MM-DD. The row holds the last trading day's adjusted close in that month. |
14	| `SPY` | SPDR S&P 500 ETF, adjusted close in US dollars. Stands for US stocks. |
15	| `TLT` | iShares 20+ Year Treasury Bond ETF, adjusted close in US dollars. Stands for US long bonds. |
16	| `GLD` | SPDR Gold Shares, adjusted close in US dollars. Stands for gold. |
17	| `USO` | United States Oil Fund, adjusted close in US dollars. Stands for oil. |
18	
19	## Coverage
20	
21	- First row 2022-12-31: base price only.
22	- Return months: 2023-01 to 2026-09, 45 months.
23	- Nothing after 2026-09-30 exists in this dataset.
24	
25	## What this file never does
26	
27	It never defines how to compute anything. Conventions live in `reference/methodology.md`.
28	
```

[tool call: Bash] {"command": "ls -la reference/data && python3 -I - <<'EOF'\nimport csv\nrows = list(csv.DictReader(open(\"reference/data/monthly-adjusted-close.csv\")))\nprint(len(rows), rows[0][\"Date\"], rows[-1][\"Date\"])\nsel = [r for r in rows if \"2022-12-31\" <= r[\"Date\"] <= \"2026-09-30\"]\nspy = [float(r[\"SPY\"]) for r in sel]; tlt = [float(r[\"TLT\"]) for r in sel]\nrs = [b/a-1 for a,b in zip(spy, spy[1:])]; rt = [b/a-1 for a,b in zip(tlt, tlt[1:])]\nn=len(rs); ms=sum(rs)/n; mt=sum(rt)/n\ncov=sum((x-ms)*(y-mt) for x,y in zip(rs,rt))\nvs=sum((x-ms)**2 for x in rs); vt=sum((y-mt)**2 for y in rt)\nprint(len(sel), sel[0][\"Date\"], sel[-1][\"Date\"], n, round(cov/(vs*vt)**0.5, 2), cov/(vs*vt)**0.5)\nEOF", "description": "Compute SPY-TLT monthly return correlation"}

[tool result]
```
total 20
drwxr-xr-x 2 root root 4096 Oct 13 16:09 .
drwxr-xr-x 3 root root 4096 Oct 13 16:09 ..
-rw-r--r-- 1 root root 1306 Oct 13 16:09 data-dictionary.md
-rw-r--r-- 1 root root  316 Oct 13 16:09 fetch-log.txt
-rw-r--r-- 1 root root 1895 Oct 13 16:09 monthly-adjusted-close.csv
46 2022-12-31 2026-09-30
46 2022-12-31 2026-09-30 45 0.57 0.5708404249153346
```

The correlation between SPY's and TLT's monthly returns over January 2023 to September 2026 is **0.57**. That is a moderately positive relationship, so stocks and long bonds tended to move in the same direction over this period.

I used the Pearson correlation of the 45 monthly simple returns, not of the price levels (methodology sections 2 and 8). The data is the SPY and TLT columns of the month-end price file, rows 2022-12-31 to 2026-09-30. The first row is only the starting price for the January 2023 return.

```
import csv
rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
sel = [r for r in rows if "2022-12-31" <= r["Date"] <= "2026-09-30"]
spy = [float(r["SPY"]) for r in sel]; tlt = [float(r["TLT"]) for r in sel]
rs = [b/a-1 for a,b in zip(spy, spy[1:])]; rt = [b/a-1 for a,b in zip(tlt, tlt[1:])]
n=len(rs); ms=sum(rs)/n; mt=sum(rt)/n
cov=sum((x-ms)*(y-mt) for x,y in zip(rs,rt))
vs=sum((x-ms)**2 for x in rs); vt=sum((y-mt)**2 for y in rt)
print(n, round(cov/(vs*vt)**0.5, 2))   # prints 45 0.57
```

`ANSWER: 0.57 | METHOD: methodology section 8 | SOURCE: monthly-adjusted-close.csv, SPY and TLT, rows 2022-12-31 to 2026-09-30`

Status: ok; turns: 9; seconds: 26.4; tokens in/out: 8/1663; files read: ['/srv/comp14-runs/treatment-gjvkyx7_/README.md', '/srv/comp14-runs/treatment-gjvkyx7_/identity.md', '/srv/comp14-runs/treatment-gjvkyx7_/rules.md', '/srv/comp14-runs/treatment-gjvkyx7_/examples.md', '/srv/comp14-runs/treatment-gjvkyx7_/reference/methodology.md', '/srv/comp14-runs/treatment-gjvkyx7_/reference/data/data-dictionary.md']; bash calls: 2; asked to leave sandbox: 0

## Q4

**Prompt (verbatim):** Consider an equal-weight portfolio of SPY, TLT, GLD and USO (25% each), rebalanced back to equal weight at every month end. What was its cumulative total return from January 2023 to September 2026?

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-x7taq29o/README.md"}

[tool result]
```
1	# Four-asset desk: the map
2	
3	Instructions, not state. Read this first, every time, then go where the table sends you.
4	
5	One sentence: this folder answers numeric questions about four ETFs, SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from one month-end price file under one written methodology, and says plainly when the data does not cover the question.
6	
7	## What is this, what do I do next, where does the information come from, what breaks it?
8	
9	- What: a desk that turns a plain question into one checkable number with its method and its rows.
10	- Next: read `identity.md` (the job), then `rules.md` (what must be true of every answer), then compute from `reference/`.
11	- Information: only `reference/`. The price file holds the prices, the data dictionary says what the columns are, the methodology holds every convention. Nothing comes from memory of markets.
12	- Breaks: months outside the window the methodology defines, assets not in the file, anything needing daily prices, and any request for a forecast or advice.
13	
14	## Where things live
15	
16	| Path | What it holds | Kind |
17	|------|---------------|------|
18	| `identity.md` | the job, who asks, what goes out, what breaks it | instructions |
19	| `rules.md` | numbered pass conditions and the exact shape of the answer line | instructions |
20	| `examples.md` | two right answers and one wrong one, with why | instructions |
21	| `reference/methodology.md` | every convention, one section per quantity; the one home for every fact | state |
22	| `reference/data/data-dictionary.md` | columns, source, coverage of the price file | state |
23	| `reference/data/monthly-adjusted-close.csv` | month-end adjusted closes, SPY TLT GLD USO | state |
24	
25	## Route by what was asked
26	
27	| If the question asks for | Read | Then stop at |
28	|--------------------------|------|--------------|
29	| a return, volatility, Sharpe, drawdown, correlation, best or worst month, for an asset or the equal-weight portfolio | `rules.md`, the methodology section from the table below, the price file | the ANSWER line |
30	| a month before or after the data window | `reference/methodology.md` section 11 | a refusal with the reason, no number |
31	| an asset not in the file, daily data, a forecast, or what to buy | `identity.md`, last section | a one-line decline |
32	| how an answer should look | `examples.md` | the matching example |
33	
34	## Which methodology section
35	
36	| Quantity | Section | Quantity | Section |
37	|----------|---------|----------|---------|
38	| what the file is, the window | 1 | annualised volatility, Sharpe | 6 |
39	| monthly return | 2 | maximum drawdown | 7 |
40	| the equal-weight portfolio | 3 | correlation | 8 |
41	| calendar-year return | 4 | best and worst month | 9 |
42	| cumulative return | 5 | rounding; outside the data | 10; 11 |
43	
44	## The one rule
45	
46	Every number comes from code run on the price file, under the methodology, and the answer line names the section and the rows. No number from memory, ever.
47	
48	## Size
49	
50	Roughly, in tokens: this map 550, identity 350, rules 550, examples 750, methodology 800, data dictionary 300, price file 1,000. Map plus rules plus one question's inputs lands near 3,000.
51	
```

[tool call: Bash] {"command": "ls -la /srv/comp14-runs/treatment-x7taq29o", "description": "List working directory"}

[tool result]
```
total 28
drwx------ 4 root root 4096 Oct 13 16:10 .
drwx------ 3 root root   60 Oct 13 16:10 ..
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bash_profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bashrc
drwxr-xr-x 3 root root 4096 Oct 13 16:10 .claude
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitconfig
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitmodules
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .idea
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .mcp.json
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .ripgreprc
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .vscode
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zprofile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zshrc
-rw-r--r-- 1 root root 3136 Oct 13 16:09 README.md
-rw-r--r-- 1 root root 2862 Oct 13 16:09 examples.md
-rw-r--r-- 1 root root 1829 Oct 13 16:09 identity.md
drwxr-xr-x 3 root root 4096 Oct 13 16:09 reference
-rw-r--r-- 1 root root 2264 Oct 13 16:09 rules.md
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-x7taq29o/identity.md"}

[tool result]
```
1	# Identity: the four-asset desk
2	
3	Instructions, not state. Load this right after the README, in every chat.
4	
5	One job: answer numeric questions about SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from the month-end price file under the methodology, and say plainly when the data does not cover the question.
6	
7	## Who asks, and what do they get?
8	
9	A client or a colleague who wants one number they can check. They get the number, the convention it rests on, the rows it came from, and nothing else. They do not get an opinion on markets.
10	
11	## What comes in?
12	
13	A question in plain words. It may name a period, a weighting, a rebalancing rule or a quantity. It may be silent on some of those. It may ask about a month, an asset or a kind of data the file does not have.
14	
15	## What goes out?
16	
17	A short working, the code that produced the number with its printed result, and one final line in the shape fixed in `rules.md`. Or, when the data does not cover the question, a refusal with the reason and no number.
18	
19	## Where does the information come from?
20	
21	Only from `reference/`: the price file, its data dictionary, and the methodology. The methodology is the one home for every convention, and this file restates none of them. Memory of what markets did is not a source.
22	
23	## What breaks this desk?
24	
25	Questions about months outside the window the methodology defines. Questions that need daily or intraday prices. Questions about assets not in the file. Questions that ask what will happen, or what to buy, sell or hold. A chat in which code cannot run: then the desk says so and gives no number.
26	
27	## What this desk never does
28	
29	It never answers from memory of markets. It never picks a convention silently when the question is silent. It never gives a number for a month it does not have. It never gives investment advice.
30	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-x7taq29o/rules.md"}

[tool result]
```
1	# Rules: pass conditions for every answer
2	
3	Instructions, not state. Load after `identity.md`, before computing anything. Each rule is stated once. The conventions they point to live in `reference/methodology.md` and are not repeated here.
4	
5	## What must be true of every number?
6	
7	1. It was computed by code that reads `reference/data/monthly-adjusted-close.csv` directly, or rows copied from it verbatim. Never retype a price from memory, and never type a result from memory.
8	2. It follows the methodology section for that quantity. The README's section table says which one. The section number appears in the answer line.
9	3. Its inputs are stated: the columns used and the first and last row dates used.
10	4. It is rounded as methodology section 10 says, with its unit.
11	
12	## What if the question sets its own terms?
13	
14	5. If the question names a period, a weighting or a rebalancing rule, use exactly that. If it is silent, use the methodology's default and write "methodology default" in the working.
15	6. If the question asks for a quantity the methodology does not define, say so, define it in one sentence before computing, and write "ad hoc" in place of the section number.
16	
17	## What if the data does not cover it?
18	
19	7. Any month outside the window in methodology section 1 is answered per section 11: no number, no estimate, no figure from memory. A month after the window is refused exactly like a month before it.
20	8. Any asset not in the file, or any question that needs daily data, gets a one-line decline that says what the file does hold.
21	
22	## What shape does the answer take?
23	
24	9. Working first, short. Then the code and its printed result. Then one final line, exactly in this shape:
25	
26	   `ANSWER: <value with unit> | METHOD: methodology section <n> | SOURCE: monthly-adjusted-close.csv, <columns>, rows <first date> to <last date>`
27	
28	   For a refusal: `ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
29	
30	10. Prose outside the code and the answer line stays under 120 words. The client wants the number, not an essay.
31	
32	## What does this desk never do?
33	
34	11. Never fetch live prices, search the web, or use memory of market history. Never recommend buying, selling or holding anything. Never paste a key, a token or a password into a chat.
35	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-x7taq29o/examples.md"}

[tool result]
```
1	# Examples: the shape of a right answer, and one wrong one
2	
3	Instructions, not state. Load when unsure how an answer should look. None of these questions is one of the committed test questions. The numbers come from the price file and can be checked under the methodology.
4	
5	## What does a complete answer look like?
6	
7	Question: What was the total return (dividends reinvested) of TLT in calendar year 2023?
8	
9	Answer:
10	
11	Calendar-year total return compounds the twelve monthly simple returns of 2023 (methodology sections 2 and 4). Inputs: the TLT column, rows 2022-12-31 through 2023-12-31, thirteen prices.
12	
13	```
14	import csv
15	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
16	prices = [float(r["TLT"]) for r in rows if "2022-12-31" <= r["Date"] <= "2023-12-31"]
17	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
18	total = 1
19	for r in returns:
20	    total *= 1 + r
21	print(len(prices), round((total - 1) * 100, 1))      # prints 13 2.8
22	```
23	
24	`ANSWER: 2.8% | METHOD: methodology section 4 | SOURCE: monthly-adjusted-close.csv, TLT, rows 2022-12-31 to 2023-12-31`
25	
26	## What does a right refusal look like?
27	
28	Question: What was GLD's return in December 2022?
29	
30	Answer:
31	
32	The file's first row, 2022-12-31, is a base price only; the first return month is 2023-01 (methodology section 1). December 2022 has no return in this data, so there is no number to give.
33	
34	`ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
35	
36	## What does a wrong answer look like, and why?
37	
38	Question: What was the annualised volatility of SPY's monthly returns in calendar year 2024?
39	
40	Wrong:
41	
42	"SPY's volatility in 2024 was around 12 to 13%, which is typical for the S&P 500 in a calm year."
43	
44	Why it fails: no code was run (rule 1); no rows are named (rule 3); a range instead of one rounded figure (rule 4); no answer line (rule 9); and the figure comes from memory of markets (rule 11). It also happens to be wrong.
45	
46	Right:
47	
48	Annualised volatility is the sample standard deviation of the twelve monthly returns of 2024 times the square root of 12 (methodology section 6). Inputs: the SPY column, rows 2023-12-31 through 2024-12-31.
49	
50	```
51	import csv
52	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
53	prices = [float(r["SPY"]) for r in rows if "2023-12-31" <= r["Date"] <= "2024-12-31"]
54	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
55	mean = sum(returns) / len(returns)
56	var = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
57	print(len(returns), round(var ** 0.5 * 12 ** 0.5 * 100, 1))   # prints 12 10.7
58	```
59	
60	`ANSWER: 10.7% | METHOD: methodology section 6 | SOURCE: monthly-adjusted-close.csv, SPY, rows 2023-12-31 to 2024-12-31`
61	
62	## What these examples never do
63	
64	They never stand in for the methodology, they never carry a convention of their own, and none of them is one of the committed test questions.
65	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-x7taq29o/reference/methodology.md"}

[tool result]
```
1	# Methodology: how the desk computes every number
2	
3	State, not instructions. This is the one home for every convention. Load it before answering any question that involves a number, and name the section you used.
4	
5	## 1. What the dataset is
6	
7	- File: `reference/data/monthly-adjusted-close.csv`. Columns: `Date`, `SPY`, `TLT`, `GLD`, `USO`.
8	- `Date` is the calendar month end. The price on that row is the adjusted close of the last trading day in that month.
9	- Prices are Yahoo Finance adjusted closes (dividends and splits applied), rounded to four decimals, retrieved with `tools/fetch_data.py`. The fetch time is in `reference/data/fetch-log.txt`.
10	- The first row, 2022-12-31, is a base price only. Return months run from 2023-01 to 2026-09, 45 months in all.
11	- The four assets stand for: SPY US stocks, TLT US long-term Treasury bonds, GLD gold, USO oil.
12	
13	## 2. Monthly return
14	
15	Simple return: price this month end divided by price last month end, minus one. Not log returns. Computed per asset from adjusted close.
16	
17	## 3. The house portfolio
18	
19	Equal weight, 25 percent in each of the four assets, rebalanced back to equal weight at every month end. Its monthly return is therefore the plain average of the four assets' monthly returns in that month.
20	
21	Buy and hold is a different portfolio and not the house portfolio: 25 percent in each asset bought at the 2022-12-31 prices and never rebalanced. When a question says "the portfolio" without qualification it means the house portfolio.
22	
23	## 4. Calendar-year total return
24	
25	Compound the twelve monthly returns of that year: multiply (1 + each monthly return), subtract one. Only 2023, 2024 and 2025 are complete years. 2026 runs January to September only and is reported as year to date, never as a calendar-year return.
26	
27	## 5. Cumulative return over a period
28	
29	Multiply (1 + each monthly return) across the period, subtract one. "The full period" means 2023-01 to 2026-09.
30	
31	## 6. Annualised volatility
32	
33	Sample standard deviation of the monthly returns (divide by n minus 1) multiplied by the square root of 12.
34	
35	For the Sharpe ratio, annualised return is the arithmetic mean of monthly returns multiplied by 12, the risk-free rate is zero, and Sharpe is annualised return divided by annualised volatility. This is a stated simplification, not a claim about the right risk-free rate.
36	
37	## 7. Maximum drawdown
38	
39	Build the cumulative index: start at 1.00 on 2022-12-31 and multiply by (1 + monthly return) each month. Drawdown in a month is the index divided by its running peak, minus one. Maximum drawdown is the most negative drawdown; the trough month is the month in which it occurs.
40	
41	## 8. Correlation
42	
43	Pearson correlation of monthly returns over the stated period. Never of price levels. Correlating price levels is the common mistake this section exists to stop.
44	
45	## 9. Best and worst month
46	
47	The largest and smallest monthly return in the stated period, for an asset or for the house portfolio.
48	
49	## 10. Rounding and format
50	
51	Returns, volatility and drawdowns in percent to one decimal. Sharpe ratios and correlations to two decimals. Months as YYYY-MM.
52	
53	## 11. Outside the dataset
54	
55	Any month before 2023-01 or after 2026-09 is not in the dataset. The answer is "not in the dataset; the data ends 2026-09-30", with no number, no estimate, and no figure from memory.
56	
57	## 12. What this file never does
58	
59	It never holds a computed answer. Answers come from the data through these rules at the moment they are asked.
60	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-x7taq29o/reference/data/data-dictionary.md"}

[tool result]
```
1	# Data dictionary: monthly-adjusted-close.csv
2	
3	State, not instructions. Read this to know what each column is and where it came from.
4	
5	## Where it came from
6	
7	Yahoo Finance end-of-day prices, retrieved with `tools/fetch_data.py` (yfinance, no API key). The exact retrieval time, library versions and row counts are appended to `fetch-log.txt` on every fetch. The committed CSV is the dataset of record. Yahoo adjusts prices retroactively for later dividends and splits, so a re-fetch on another day can differ slightly.
8	
9	## Columns
10	
11	| Column | Meaning |
12	|--------|---------|
13	| `Date` | Calendar month end, YYYY-MM-DD. The row holds the last trading day's adjusted close in that month. |
14	| `SPY` | SPDR S&P 500 ETF, adjusted close in US dollars. Stands for US stocks. |
15	| `TLT` | iShares 20+ Year Treasury Bond ETF, adjusted close in US dollars. Stands for US long bonds. |
16	| `GLD` | SPDR Gold Shares, adjusted close in US dollars. Stands for gold. |
17	| `USO` | United States Oil Fund, adjusted close in US dollars. Stands for oil. |
18	
19	## Coverage
20	
21	- First row 2022-12-31: base price only.
22	- Return months: 2023-01 to 2026-09, 45 months.
23	- Nothing after 2026-09-30 exists in this dataset.
24	
25	## What this file never does
26	
27	It never defines how to compute anything. Conventions live in `reference/methodology.md`.
28	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-x7taq29o/reference/data/monthly-adjusted-close.csv"}

[tool result]
```
1	Date,SPY,TLT,GLD,USO
2	2022-12-31,364.7676,85.5002,169.64,70.11
3	2023-01-31,387.7069,92.0355,179.41,69.32
4	2023-02-28,377.9589,87.5713,169.78,67.21
5	2023-03-31,391.9728,91.8092,183.22,66.44
6	2023-04-30,398.2345,92.1198,184.8,67.5
7	2023-05-31,400.0729,89.3421,182.32,60.63
8	2023-06-30,425.9975,89.5361,178.27,63.55
9	2023-07-31,439.9418,87.2581,182.35,73.17
10	2023-08-31,432.7919,84.5163,180.02,75.06
11	2023-09-30,412.2626,77.7964,171.45,80.86
12	2023-10-31,403.313,73.5462,184.09,75.02
13	2023-11-30,440.1531,80.8448,188.75,70.14
14	2023-12-31,460.2484,87.8668,191.17,66.65
15	2024-01-31,467.5785,85.8941,188.45,70.92
16	2024-02-29,491.9801,83.9596,189.31,73.36
17	2024-03-31,508.0688,84.6169,205.72,78.73
18	2024-04-30,487.5835,79.1545,211.87,78.38
19	2024-05-31,512.2454,81.4396,215.3,74.82
20	2024-06-30,530.3175,82.9195,215.01,79.59
21	2024-07-31,536.7392,85.9294,226.55,77.74
22	2024-08-31,549.2804,87.7436,231.29,74.34
23	2024-09-30,560.8178,89.498,243.06,69.92
24	2024-10-31,555.8132,84.616,253.51,73.08
25	2024-11-30,588.9584,86.2975,245.59,71.61
26	2024-12-31,574.788,80.7908,242.13,75.55
27	2025-01-31,590.2247,81.1886,258.56,78.02
28	2025-02-28,582.7319,85.814,263.27,75.22
29	2025-03-31,550.2626,84.7802,288.14,77.33
30	2025-04-30,545.4916,83.6268,303.77,63.56
31	2025-05-31,579.7731,80.9419,303.6,67.15
32	2025-06-30,609.5654,83.0982,304.83,73.11
33	2025-07-31,623.6046,82.1512,302.96,79.59
34	2025-08-31,636.4007,82.1616,318.07,74.84
35	2025-09-30,659.0695,85.112,355.47,73.75
36	2025-10-31,674.78,86.2875,368.12,72.56
37	2025-11-30,676.0959,86.5225,387.88,71.07
38	2025-12-31,676.635,84.2222,396.31,69.16
39	2026-01-31,686.6071,84.1932,444.95,79.52
40	2026-02-28,680.6734,88.0945,483.75,81.95
41	2026-03-31,647.0621,84.3681,430.29,127.25
42	2026-04-30,715.0377,83.6597,423.66,147.09
43	2026-05-31,752.6671,84.1059,417.12,129.09
44	2026-06-30,744.9202,85.0865,368.38,106.44
45	2026-07-31,745.1796,81.2799,371.54,129.17
46	2026-08-31,765.15,81.8752,408.42,133.7
47	2026-09-30,762.63,77.468,380.84,145.66
48	
```

[tool call: Bash] {"command": "python3 -I -c '\nimport csv\nrows = list(csv.DictReader(open(\"reference/data/monthly-adjusted-close.csv\")))\nrows = [r for r in rows if \"2022-12-31\" <= r[\"Date\"] <= \"2026-09-30\"]\na = [\"SPY\",\"TLT\",\"GLD\",\"USO\"]\nidx = 1.0; n = 0\nfor p, c in zip(rows, rows[1:]):\n    idx *= 1 + sum(float(c[k])/float(p[k]) - 1 for k in a)/4; n += 1\nprint(rows[0][\"Date\"], rows[-1][\"Date\"], n, round((idx-1)*100, 1))\n'", "description": "Compute cumulative return of monthly-rebalanced equal-weight portfolio"}

[tool result]
```
2022-12-31 2026-09-30 45 85.5
```

The portfolio's cumulative total return from January 2023 to September 2026 was **85.5%**.

Your question set the weights (25% each), the monthly rebalancing and the period, and these match the house portfolio. Its return each month is the plain average of the four funds' simple monthly returns (methodology section 3). The 45 monthly returns from 2023-01 to 2026-09 are then multiplied together as (1 + return) and 1 is subtracted (section 5). The price file uses adjusted closes, so reinvested dividends are included. The prices come from the rows 2022-12-31 (the starting price only) to 2026-09-30.

```
import csv
rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
rows = [r for r in rows if "2022-12-31" <= r["Date"] <= "2026-09-30"]
a = ["SPY","TLT","GLD","USO"]
idx = 1.0; n = 0
for p, c in zip(rows, rows[1:]):
    idx *= 1 + sum(float(c[k])/float(p[k]) - 1 for k in a)/4; n += 1
print(rows[0]["Date"], rows[-1]["Date"], n, round((idx-1)*100, 1))
# prints: 2022-12-31 2026-09-30 45 85.5
```

`ANSWER: 85.5% | METHOD: methodology section 5 | SOURCE: monthly-adjusted-close.csv, SPY TLT GLD USO, rows 2022-12-31 to 2026-09-30`

Status: ok; turns: 10; seconds: 25.6; tokens in/out: 8/1524; files read: ['/srv/comp14-runs/treatment-x7taq29o/README.md', '/srv/comp14-runs/treatment-x7taq29o/identity.md', '/srv/comp14-runs/treatment-x7taq29o/rules.md', '/srv/comp14-runs/treatment-x7taq29o/examples.md', '/srv/comp14-runs/treatment-x7taq29o/reference/methodology.md', '/srv/comp14-runs/treatment-x7taq29o/reference/data/data-dictionary.md', '/srv/comp14-runs/treatment-x7taq29o/reference/data/monthly-adjusted-close.csv']; bash calls: 2; asked to leave sandbox: 0

## Q5

**Prompt (verbatim):** For that same equal-weight SPY, TLT, GLD and USO portfolio rebalanced monthly, what was the maximum drawdown measured on month-end values from January 2023 to September 2026, and in which month did the trough occur?

[tool call: Bash] {"command": "cat README.md && ls -la", "description": "Read README and list files"}

[tool result]
```
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
total 28
drwx------ 4 root root 4096 Oct 13 16:10 .
drwx------ 3 root root   60 Oct 13 16:10 ..
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bash_profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bashrc
drwxr-xr-x 3 root root 4096 Oct 13 16:10 .claude
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitconfig
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitmodules
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .idea
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .mcp.json
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .ripgreprc
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .vscode
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zprofile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zshrc
-rw-r--r-- 1 root root 3136 Oct 13 16:09 README.md
-rw-r--r-- 1 root root 2862 Oct 13 16:09 examples.md
-rw-r--r-- 1 root root 1829 Oct 13 16:09 identity.md
drwxr-xr-x 3 root root 4096 Oct 13 16:09 reference
-rw-r--r-- 1 root root 2264 Oct 13 16:09 rules.md
```

[tool call: Bash] {"command": "cat identity.md rules.md examples.md reference/methodology.md reference/data/data-dictionary.md reference/data/monthly-adjusted-close.csv", "description": "Read instructions, methodology, and data"}

[tool result]
```
# Identity: the four-asset desk

Instructions, not state. Load this right after the README, in every chat.

One job: answer numeric questions about SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from the month-end price file under the methodology, and say plainly when the data does not cover the question.

## Who asks, and what do they get?

A client or a colleague who wants one number they can check. They get the number, the convention it rests on, the rows it came from, and nothing else. They do not get an opinion on markets.

## What comes in?

A question in plain words. It may name a period, a weighting, a rebalancing rule or a quantity. It may be silent on some of those. It may ask about a month, an asset or a kind of data the file does not have.

## What goes out?

A short working, the code that produced the number with its printed result, and one final line in the shape fixed in `rules.md`. Or, when the data does not cover the question, a refusal with the reason and no number.

## Where does the information come from?

Only from `reference/`: the price file, its data dictionary, and the methodology. The methodology is the one home for every convention, and this file restates none of them. Memory of what markets did is not a source.

## What breaks this desk?

Questions about months outside the window the methodology defines. Questions that need daily or intraday prices. Questions about assets not in the file. Questions that ask what will happen, or what to buy, sell or hold. A chat in which code cannot run: then the desk says so and gives no number.

## What this desk never does

It never answers from memory of markets. It never picks a convention silently when the question is silent. It never gives a number for a month it does not have. It never gives investment advice.
# Rules: pass conditions for every answer

Instructions, not state. Load after `identity.md`, before computing anything. Each rule is stated once. The conventions they point to live in `reference/methodology.md` and are not repeated here.

## What must be true of every number?

1. It was computed by code that reads `reference/data/monthly-adjusted-close.csv` directly, or rows copied from it verbatim. Never retype a price from memory, and never type a result from memory.
2. It follows the methodology section for that quantity. The README's section table says which one. The section number appears in the answer line.
3. Its inputs are stated: the columns used and the first and last row dates used.
4. It is rounded as methodology section 10 says, with its unit.

## What if the question sets its own terms?

5. If the question names a period, a weighting or a rebalancing rule, use exactly that. If it is silent, use the methodology's default and write "methodology default" in the working.
6. If the question asks for a quantity the methodology does not define, say so, define it in one sentence before computing, and write "ad hoc" in place of the section number.

## What if the data does not cover it?

7. Any month outside the window in methodology section 1 is answered per section 11: no number, no estimate, no figure from memory. A month after the window is refused exactly like a month before it.
8. Any asset not in the file, or any question that needs daily data, gets a one-line decline that says what the file does hold.

## What shape does the answer take?

9. Working first, short. Then the code and its printed result. Then one final line, exactly in this shape:

   `ANSWER: <value with unit> | METHOD: methodology section <n> | SOURCE: monthly-adjusted-close.csv, <columns>, rows <first date> to <last date>`

   For a refusal: `ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`

10. Prose outside the code and the answer line stays under 120 words. The client wants the number, not an essay.

## What does this desk never do?

11. Never fetch live prices, search the web, or use memory of market history. Never recommend buying, selling or holding anything. Never paste a key, a token or a password into a chat.
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
Date,SPY,TLT,GLD,USO
2022-12-31,364.7676,85.5002,169.64,70.11
2023-01-31,387.7069,92.0355,179.41,69.32
2023-02-28,377.9589,87.5713,169.78,67.21
2023-03-31,391.9728,91.8092,183.22,66.44
2023-04-30,398.2345,92.1198,184.8,67.5
2023-05-31,400.0729,89.3421,182.32,60.63
2023-06-30,425.9975,89.5361,178.27,63.55
2023-07-31,439.9418,87.2581,182.35,73.17
2023-08-31,432.7919,84.5163,180.02,75.06
2023-09-30,412.2626,77.7964,171.45,80.86
2023-10-31,403.313,73.5462,184.09,75.02
2023-11-30,440.1531,80.8448,188.75,70.14
2023-12-31,460.2484,87.8668,191.17,66.65
2024-01-31,467.5785,85.8941,188.45,70.92
2024-02-29,491.9801,83.9596,189.31,73.36
2024-03-31,508.0688,84.6169,205.72,78.73
2024-04-30,487.5835,79.1545,211.87,78.38
2024-05-31,512.2454,81.4396,215.3,74.82
2024-06-30,530.3175,82.9195,215.01,79.59
2024-07-31,536.7392,85.9294,226.55,77.74
2024-08-31,549.2804,87.7436,231.29,74.34
2024-09-30,560.8178,89.498,243.06,69.92
2024-10-31,555.8132,84.616,253.51,73.08
2024-11-30,588.9584,86.2975,245.59,71.61
2024-12-31,574.788,80.7908,242.13,75.55
2025-01-31,590.2247,81.1886,258.56,78.02
2025-02-28,582.7319,85.814,263.27,75.22
2025-03-31,550.2626,84.7802,288.14,77.33
2025-04-30,545.4916,83.6268,303.77,63.56
2025-05-31,579.7731,80.9419,303.6,67.15
2025-06-30,609.5654,83.0982,304.83,73.11
2025-07-31,623.6046,82.1512,302.96,79.59
2025-08-31,636.4007,82.1616,318.07,74.84
2025-09-30,659.0695,85.112,355.47,73.75
2025-10-31,674.78,86.2875,368.12,72.56
2025-11-30,676.0959,86.5225,387.88,71.07
2025-12-31,676.635,84.2222,396.31,69.16
2026-01-31,686.6071,84.1932,444.95,79.52
2026-02-28,680.6734,88.0945,483.75,81.95
2026-03-31,647.0621,84.3681,430.29,127.25
2026-04-30,715.0377,83.6597,423.66,147.09
2026-05-31,752.6671,84.1059,417.12,129.09
2026-06-30,744.9202,85.0865,368.38,106.44
2026-07-31,745.1796,81.2799,371.54,129.17
2026-08-31,765.15,81.8752,408.42,133.7
2026-09-30,762.63,77.468,380.84,145.66
```

[tool call: Bash] {"command": "python3 -c '\nimport csv\nrows = list(csv.DictReader(open(\"reference/data/monthly-adjusted-close.csv\")))\na=[\"SPY\",\"TLT\",\"GLD\",\"USO\"]\nidx=1.0; peak=1.0; mdd=0; tm=None; pk=None; pkd=\"2022-12-31\"\nfor p,c in zip(rows,rows[1:]):\n    r=sum(float(c[x])/float(p[x])-1 for x in a)/4\n    idx*=1+r\n    if idx>peak: peak=idx; pkd=c[\"Date\"]\n    dd=idx/peak-1\n    if dd<mdd: mdd=dd; tm=c[\"Date\"]; pk=pkd\nprint(len(rows)-1, rows[0][\"Date\"], rows[-1][\"Date\"], round(mdd*100,1), tm[:7], \"peak\", pk[:7], round(mdd*100,3))\n'", "description": "Compute max drawdown of equal-weight portfolio"}

[tool result]
```
45 2022-12-31 2026-09-30 -9.1 2026-06 peak 2026-04 -9.125
```

The maximum drawdown was **−9.1%**, and the trough came in **June 2026 (2026-06)**. The peak before it was April 2026 (2026-04).

The portfolio is equal weight with a rebalance every month end, as you said. Its monthly return is the plain average of the four assets' simple monthly returns (methodology sections 2 and 3). I built an index starting at 1.00 on 2022-12-31, which is a base price only, and compounded it through 2026-09, giving 45 return months. Drawdown each month is the index divided by its running peak, minus one; the maximum is the most negative value (section 7).

```
import csv
rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
a = ["SPY","TLT","GLD","USO"]
idx = peak = 1.0; mdd = 0; pkd = "2022-12-31"
for p, c in zip(rows, rows[1:]):
    r = sum(float(c[x])/float(p[x]) - 1 for x in a) / 4
    idx *= 1 + r
    if idx > peak: peak, pkd = idx, c["Date"]
    dd = idx/peak - 1
    if dd < mdd: mdd, tm, pk = dd, c["Date"], pkd
print(len(rows)-1, round(mdd*100,1), tm[:7], "peak", pk[:7])
# prints: 45 -9.1 2026-06 peak 2026-04
```

`ANSWER: -9.1%, trough 2026-06 | METHOD: methodology section 7 | SOURCE: monthly-adjusted-close.csv, SPY TLT GLD USO, rows 2022-12-31 to 2026-09-30`

Status: ok; turns: 4; seconds: 26.4; tokens in/out: 8/1294; files read: []; bash calls: 3; asked to leave sandbox: 0

## Q6

**Prompt (verbatim):** What was the annualised volatility of USO's monthly returns from January 2023 to September 2026?

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-b1fxpasf/README.md"}

[tool result]
```
1	# Four-asset desk: the map
2	
3	Instructions, not state. Read this first, every time, then go where the table sends you.
4	
5	One sentence: this folder answers numeric questions about four ETFs, SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from one month-end price file under one written methodology, and says plainly when the data does not cover the question.
6	
7	## What is this, what do I do next, where does the information come from, what breaks it?
8	
9	- What: a desk that turns a plain question into one checkable number with its method and its rows.
10	- Next: read `identity.md` (the job), then `rules.md` (what must be true of every answer), then compute from `reference/`.
11	- Information: only `reference/`. The price file holds the prices, the data dictionary says what the columns are, the methodology holds every convention. Nothing comes from memory of markets.
12	- Breaks: months outside the window the methodology defines, assets not in the file, anything needing daily prices, and any request for a forecast or advice.
13	
14	## Where things live
15	
16	| Path | What it holds | Kind |
17	|------|---------------|------|
18	| `identity.md` | the job, who asks, what goes out, what breaks it | instructions |
19	| `rules.md` | numbered pass conditions and the exact shape of the answer line | instructions |
20	| `examples.md` | two right answers and one wrong one, with why | instructions |
21	| `reference/methodology.md` | every convention, one section per quantity; the one home for every fact | state |
22	| `reference/data/data-dictionary.md` | columns, source, coverage of the price file | state |
23	| `reference/data/monthly-adjusted-close.csv` | month-end adjusted closes, SPY TLT GLD USO | state |
24	
25	## Route by what was asked
26	
27	| If the question asks for | Read | Then stop at |
28	|--------------------------|------|--------------|
29	| a return, volatility, Sharpe, drawdown, correlation, best or worst month, for an asset or the equal-weight portfolio | `rules.md`, the methodology section from the table below, the price file | the ANSWER line |
30	| a month before or after the data window | `reference/methodology.md` section 11 | a refusal with the reason, no number |
31	| an asset not in the file, daily data, a forecast, or what to buy | `identity.md`, last section | a one-line decline |
32	| how an answer should look | `examples.md` | the matching example |
33	
34	## Which methodology section
35	
36	| Quantity | Section | Quantity | Section |
37	|----------|---------|----------|---------|
38	| what the file is, the window | 1 | annualised volatility, Sharpe | 6 |
39	| monthly return | 2 | maximum drawdown | 7 |
40	| the equal-weight portfolio | 3 | correlation | 8 |
41	| calendar-year return | 4 | best and worst month | 9 |
42	| cumulative return | 5 | rounding; outside the data | 10; 11 |
43	
44	## The one rule
45	
46	Every number comes from code run on the price file, under the methodology, and the answer line names the section and the rows. No number from memory, ever.
47	
48	## Size
49	
50	Roughly, in tokens: this map 550, identity 350, rules 550, examples 750, methodology 800, data dictionary 300, price file 1,000. Map plus rules plus one question's inputs lands near 3,000.
51	
```

[tool call: Bash] {"command": "ls -la /srv/comp14-runs/treatment-b1fxpasf", "description": "List files in working directory"}

[tool result]
```
total 28
drwx------ 4 root root 4096 Oct 13 16:10 .
drwx------ 3 root root   60 Oct 13 16:10 ..
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bash_profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bashrc
drwxr-xr-x 3 root root 4096 Oct 13 16:10 .claude
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitconfig
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitmodules
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .idea
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .mcp.json
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .ripgreprc
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .vscode
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zprofile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zshrc
-rw-r--r-- 1 root root 3136 Oct 13 16:09 README.md
-rw-r--r-- 1 root root 2862 Oct 13 16:09 examples.md
-rw-r--r-- 1 root root 1829 Oct 13 16:09 identity.md
drwxr-xr-x 3 root root 4096 Oct 13 16:09 reference
-rw-r--r-- 1 root root 2264 Oct 13 16:09 rules.md
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-b1fxpasf/identity.md"}

[tool result]
```
1	# Identity: the four-asset desk
2	
3	Instructions, not state. Load this right after the README, in every chat.
4	
5	One job: answer numeric questions about SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from the month-end price file under the methodology, and say plainly when the data does not cover the question.
6	
7	## Who asks, and what do they get?
8	
9	A client or a colleague who wants one number they can check. They get the number, the convention it rests on, the rows it came from, and nothing else. They do not get an opinion on markets.
10	
11	## What comes in?
12	
13	A question in plain words. It may name a period, a weighting, a rebalancing rule or a quantity. It may be silent on some of those. It may ask about a month, an asset or a kind of data the file does not have.
14	
15	## What goes out?
16	
17	A short working, the code that produced the number with its printed result, and one final line in the shape fixed in `rules.md`. Or, when the data does not cover the question, a refusal with the reason and no number.
18	
19	## Where does the information come from?
20	
21	Only from `reference/`: the price file, its data dictionary, and the methodology. The methodology is the one home for every convention, and this file restates none of them. Memory of what markets did is not a source.
22	
23	## What breaks this desk?
24	
25	Questions about months outside the window the methodology defines. Questions that need daily or intraday prices. Questions about assets not in the file. Questions that ask what will happen, or what to buy, sell or hold. A chat in which code cannot run: then the desk says so and gives no number.
26	
27	## What this desk never does
28	
29	It never answers from memory of markets. It never picks a convention silently when the question is silent. It never gives a number for a month it does not have. It never gives investment advice.
30	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-b1fxpasf/rules.md"}

[tool result]
```
1	# Rules: pass conditions for every answer
2	
3	Instructions, not state. Load after `identity.md`, before computing anything. Each rule is stated once. The conventions they point to live in `reference/methodology.md` and are not repeated here.
4	
5	## What must be true of every number?
6	
7	1. It was computed by code that reads `reference/data/monthly-adjusted-close.csv` directly, or rows copied from it verbatim. Never retype a price from memory, and never type a result from memory.
8	2. It follows the methodology section for that quantity. The README's section table says which one. The section number appears in the answer line.
9	3. Its inputs are stated: the columns used and the first and last row dates used.
10	4. It is rounded as methodology section 10 says, with its unit.
11	
12	## What if the question sets its own terms?
13	
14	5. If the question names a period, a weighting or a rebalancing rule, use exactly that. If it is silent, use the methodology's default and write "methodology default" in the working.
15	6. If the question asks for a quantity the methodology does not define, say so, define it in one sentence before computing, and write "ad hoc" in place of the section number.
16	
17	## What if the data does not cover it?
18	
19	7. Any month outside the window in methodology section 1 is answered per section 11: no number, no estimate, no figure from memory. A month after the window is refused exactly like a month before it.
20	8. Any asset not in the file, or any question that needs daily data, gets a one-line decline that says what the file does hold.
21	
22	## What shape does the answer take?
23	
24	9. Working first, short. Then the code and its printed result. Then one final line, exactly in this shape:
25	
26	   `ANSWER: <value with unit> | METHOD: methodology section <n> | SOURCE: monthly-adjusted-close.csv, <columns>, rows <first date> to <last date>`
27	
28	   For a refusal: `ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
29	
30	10. Prose outside the code and the answer line stays under 120 words. The client wants the number, not an essay.
31	
32	## What does this desk never do?
33	
34	11. Never fetch live prices, search the web, or use memory of market history. Never recommend buying, selling or holding anything. Never paste a key, a token or a password into a chat.
35	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-b1fxpasf/examples.md"}

[tool result]
```
1	# Examples: the shape of a right answer, and one wrong one
2	
3	Instructions, not state. Load when unsure how an answer should look. None of these questions is one of the committed test questions. The numbers come from the price file and can be checked under the methodology.
4	
5	## What does a complete answer look like?
6	
7	Question: What was the total return (dividends reinvested) of TLT in calendar year 2023?
8	
9	Answer:
10	
11	Calendar-year total return compounds the twelve monthly simple returns of 2023 (methodology sections 2 and 4). Inputs: the TLT column, rows 2022-12-31 through 2023-12-31, thirteen prices.
12	
13	```
14	import csv
15	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
16	prices = [float(r["TLT"]) for r in rows if "2022-12-31" <= r["Date"] <= "2023-12-31"]
17	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
18	total = 1
19	for r in returns:
20	    total *= 1 + r
21	print(len(prices), round((total - 1) * 100, 1))      # prints 13 2.8
22	```
23	
24	`ANSWER: 2.8% | METHOD: methodology section 4 | SOURCE: monthly-adjusted-close.csv, TLT, rows 2022-12-31 to 2023-12-31`
25	
26	## What does a right refusal look like?
27	
28	Question: What was GLD's return in December 2022?
29	
30	Answer:
31	
32	The file's first row, 2022-12-31, is a base price only; the first return month is 2023-01 (methodology section 1). December 2022 has no return in this data, so there is no number to give.
33	
34	`ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
35	
36	## What does a wrong answer look like, and why?
37	
38	Question: What was the annualised volatility of SPY's monthly returns in calendar year 2024?
39	
40	Wrong:
41	
42	"SPY's volatility in 2024 was around 12 to 13%, which is typical for the S&P 500 in a calm year."
43	
44	Why it fails: no code was run (rule 1); no rows are named (rule 3); a range instead of one rounded figure (rule 4); no answer line (rule 9); and the figure comes from memory of markets (rule 11). It also happens to be wrong.
45	
46	Right:
47	
48	Annualised volatility is the sample standard deviation of the twelve monthly returns of 2024 times the square root of 12 (methodology section 6). Inputs: the SPY column, rows 2023-12-31 through 2024-12-31.
49	
50	```
51	import csv
52	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
53	prices = [float(r["SPY"]) for r in rows if "2023-12-31" <= r["Date"] <= "2024-12-31"]
54	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
55	mean = sum(returns) / len(returns)
56	var = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
57	print(len(returns), round(var ** 0.5 * 12 ** 0.5 * 100, 1))   # prints 12 10.7
58	```
59	
60	`ANSWER: 10.7% | METHOD: methodology section 6 | SOURCE: monthly-adjusted-close.csv, SPY, rows 2023-12-31 to 2024-12-31`
61	
62	## What these examples never do
63	
64	They never stand in for the methodology, they never carry a convention of their own, and none of them is one of the committed test questions.
65	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-b1fxpasf/reference/methodology.md"}

[tool result]
```
1	# Methodology: how the desk computes every number
2	
3	State, not instructions. This is the one home for every convention. Load it before answering any question that involves a number, and name the section you used.
4	
5	## 1. What the dataset is
6	
7	- File: `reference/data/monthly-adjusted-close.csv`. Columns: `Date`, `SPY`, `TLT`, `GLD`, `USO`.
8	- `Date` is the calendar month end. The price on that row is the adjusted close of the last trading day in that month.
9	- Prices are Yahoo Finance adjusted closes (dividends and splits applied), rounded to four decimals, retrieved with `tools/fetch_data.py`. The fetch time is in `reference/data/fetch-log.txt`.
10	- The first row, 2022-12-31, is a base price only. Return months run from 2023-01 to 2026-09, 45 months in all.
11	- The four assets stand for: SPY US stocks, TLT US long-term Treasury bonds, GLD gold, USO oil.
12	
13	## 2. Monthly return
14	
15	Simple return: price this month end divided by price last month end, minus one. Not log returns. Computed per asset from adjusted close.
16	
17	## 3. The house portfolio
18	
19	Equal weight, 25 percent in each of the four assets, rebalanced back to equal weight at every month end. Its monthly return is therefore the plain average of the four assets' monthly returns in that month.
20	
21	Buy and hold is a different portfolio and not the house portfolio: 25 percent in each asset bought at the 2022-12-31 prices and never rebalanced. When a question says "the portfolio" without qualification it means the house portfolio.
22	
23	## 4. Calendar-year total return
24	
25	Compound the twelve monthly returns of that year: multiply (1 + each monthly return), subtract one. Only 2023, 2024 and 2025 are complete years. 2026 runs January to September only and is reported as year to date, never as a calendar-year return.
26	
27	## 5. Cumulative return over a period
28	
29	Multiply (1 + each monthly return) across the period, subtract one. "The full period" means 2023-01 to 2026-09.
30	
31	## 6. Annualised volatility
32	
33	Sample standard deviation of the monthly returns (divide by n minus 1) multiplied by the square root of 12.
34	
35	For the Sharpe ratio, annualised return is the arithmetic mean of monthly returns multiplied by 12, the risk-free rate is zero, and Sharpe is annualised return divided by annualised volatility. This is a stated simplification, not a claim about the right risk-free rate.
36	
37	## 7. Maximum drawdown
38	
39	Build the cumulative index: start at 1.00 on 2022-12-31 and multiply by (1 + monthly return) each month. Drawdown in a month is the index divided by its running peak, minus one. Maximum drawdown is the most negative drawdown; the trough month is the month in which it occurs.
40	
41	## 8. Correlation
42	
43	Pearson correlation of monthly returns over the stated period. Never of price levels. Correlating price levels is the common mistake this section exists to stop.
44	
45	## 9. Best and worst month
46	
47	The largest and smallest monthly return in the stated period, for an asset or for the house portfolio.
48	
49	## 10. Rounding and format
50	
51	Returns, volatility and drawdowns in percent to one decimal. Sharpe ratios and correlations to two decimals. Months as YYYY-MM.
52	
53	## 11. Outside the dataset
54	
55	Any month before 2023-01 or after 2026-09 is not in the dataset. The answer is "not in the dataset; the data ends 2026-09-30", with no number, no estimate, and no figure from memory.
56	
57	## 12. What this file never does
58	
59	It never holds a computed answer. Answers come from the data through these rules at the moment they are asked.
60	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-b1fxpasf/reference/data/data-dictionary.md"}

[tool result]
```
1	# Data dictionary: monthly-adjusted-close.csv
2	
3	State, not instructions. Read this to know what each column is and where it came from.
4	
5	## Where it came from
6	
7	Yahoo Finance end-of-day prices, retrieved with `tools/fetch_data.py` (yfinance, no API key). The exact retrieval time, library versions and row counts are appended to `fetch-log.txt` on every fetch. The committed CSV is the dataset of record. Yahoo adjusts prices retroactively for later dividends and splits, so a re-fetch on another day can differ slightly.
8	
9	## Columns
10	
11	| Column | Meaning |
12	|--------|---------|
13	| `Date` | Calendar month end, YYYY-MM-DD. The row holds the last trading day's adjusted close in that month. |
14	| `SPY` | SPDR S&P 500 ETF, adjusted close in US dollars. Stands for US stocks. |
15	| `TLT` | iShares 20+ Year Treasury Bond ETF, adjusted close in US dollars. Stands for US long bonds. |
16	| `GLD` | SPDR Gold Shares, adjusted close in US dollars. Stands for gold. |
17	| `USO` | United States Oil Fund, adjusted close in US dollars. Stands for oil. |
18	
19	## Coverage
20	
21	- First row 2022-12-31: base price only.
22	- Return months: 2023-01 to 2026-09, 45 months.
23	- Nothing after 2026-09-30 exists in this dataset.
24	
25	## What this file never does
26	
27	It never defines how to compute anything. Conventions live in `reference/methodology.md`.
28	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-b1fxpasf/reference/data/monthly-adjusted-close.csv"}

[tool result]
```
1	Date,SPY,TLT,GLD,USO
2	2022-12-31,364.7676,85.5002,169.64,70.11
3	2023-01-31,387.7069,92.0355,179.41,69.32
4	2023-02-28,377.9589,87.5713,169.78,67.21
5	2023-03-31,391.9728,91.8092,183.22,66.44
6	2023-04-30,398.2345,92.1198,184.8,67.5
7	2023-05-31,400.0729,89.3421,182.32,60.63
8	2023-06-30,425.9975,89.5361,178.27,63.55
9	2023-07-31,439.9418,87.2581,182.35,73.17
10	2023-08-31,432.7919,84.5163,180.02,75.06
11	2023-09-30,412.2626,77.7964,171.45,80.86
12	2023-10-31,403.313,73.5462,184.09,75.02
13	2023-11-30,440.1531,80.8448,188.75,70.14
14	2023-12-31,460.2484,87.8668,191.17,66.65
15	2024-01-31,467.5785,85.8941,188.45,70.92
16	2024-02-29,491.9801,83.9596,189.31,73.36
17	2024-03-31,508.0688,84.6169,205.72,78.73
18	2024-04-30,487.5835,79.1545,211.87,78.38
19	2024-05-31,512.2454,81.4396,215.3,74.82
20	2024-06-30,530.3175,82.9195,215.01,79.59
21	2024-07-31,536.7392,85.9294,226.55,77.74
22	2024-08-31,549.2804,87.7436,231.29,74.34
23	2024-09-30,560.8178,89.498,243.06,69.92
24	2024-10-31,555.8132,84.616,253.51,73.08
25	2024-11-30,588.9584,86.2975,245.59,71.61
26	2024-12-31,574.788,80.7908,242.13,75.55
27	2025-01-31,590.2247,81.1886,258.56,78.02
28	2025-02-28,582.7319,85.814,263.27,75.22
29	2025-03-31,550.2626,84.7802,288.14,77.33
30	2025-04-30,545.4916,83.6268,303.77,63.56
31	2025-05-31,579.7731,80.9419,303.6,67.15
32	2025-06-30,609.5654,83.0982,304.83,73.11
33	2025-07-31,623.6046,82.1512,302.96,79.59
34	2025-08-31,636.4007,82.1616,318.07,74.84
35	2025-09-30,659.0695,85.112,355.47,73.75
36	2025-10-31,674.78,86.2875,368.12,72.56
37	2025-11-30,676.0959,86.5225,387.88,71.07
38	2025-12-31,676.635,84.2222,396.31,69.16
39	2026-01-31,686.6071,84.1932,444.95,79.52
40	2026-02-28,680.6734,88.0945,483.75,81.95
41	2026-03-31,647.0621,84.3681,430.29,127.25
42	2026-04-30,715.0377,83.6597,423.66,147.09
43	2026-05-31,752.6671,84.1059,417.12,129.09
44	2026-06-30,744.9202,85.0865,368.38,106.44
45	2026-07-31,745.1796,81.2799,371.54,129.17
46	2026-08-31,765.15,81.8752,408.42,133.7
47	2026-09-30,762.63,77.468,380.84,145.66
48	
```

[tool call: Bash] {"command": "python3 -I -c '\nimport csv\nrows = list(csv.DictReader(open(\"reference/data/monthly-adjusted-close.csv\")))\nprices = [float(r[\"USO\"]) for r in rows if \"2022-12-31\" <= r[\"Date\"] <= \"2026-09-30\"]\nreturns = [b / a - 1 for a, b in zip(prices, prices[1:])]\nmean = sum(returns) / len(returns)\nvar = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)\nprint(len(prices), len(returns), round(var ** 0.5 * 12 ** 0.5 * 100, 1))\n'", "description": "Compute USO annualised volatility"}

[tool result]
```
46 45 39.6
```

USO's annualised volatility over January 2023 to September 2026 was **39.6%**, worked out from the price file.

Method (section 6): I took the sample standard deviation of the 45 monthly simple returns from 2023-01 to 2026-09, dividing by n−1, and multiplied it by √12. The inputs are the USO column, rows 2022-12-31 to 2026-09-30, which is 46 prices. The first row is only the starting price for the first return.

```
import csv
rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
prices = [float(r["USO"]) for r in rows if "2022-12-31" <= r["Date"] <= "2026-09-30"]
returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
mean = sum(returns) / len(returns)
var = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
print(len(prices), len(returns), round(var ** 0.5 * 12 ** 0.5 * 100, 1))   # prints 46 45 39.6
```

`ANSWER: 39.6% | METHOD: methodology section 6 | SOURCE: monthly-adjusted-close.csv, USO, rows 2022-12-31 to 2026-09-30`

Status: ok; turns: 10; seconds: 27.1; tokens in/out: 8/1428; files read: ['/srv/comp14-runs/treatment-b1fxpasf/README.md', '/srv/comp14-runs/treatment-b1fxpasf/identity.md', '/srv/comp14-runs/treatment-b1fxpasf/rules.md', '/srv/comp14-runs/treatment-b1fxpasf/examples.md', '/srv/comp14-runs/treatment-b1fxpasf/reference/methodology.md', '/srv/comp14-runs/treatment-b1fxpasf/reference/data/data-dictionary.md', '/srv/comp14-runs/treatment-b1fxpasf/reference/data/monthly-adjusted-close.csv']; bash calls: 2; asked to leave sandbox: 0

## Q7

**Prompt (verbatim):** Between January and September 2026, which month was the best for an equal-weight SPY, TLT, GLD and USO portfolio rebalanced monthly, and what was the portfolio's return in that month?

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-fp89ph1h/README.md"}

[tool result]
```
1	# Four-asset desk: the map
2	
3	Instructions, not state. Read this first, every time, then go where the table sends you.
4	
5	One sentence: this folder answers numeric questions about four ETFs, SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from one month-end price file under one written methodology, and says plainly when the data does not cover the question.
6	
7	## What is this, what do I do next, where does the information come from, what breaks it?
8	
9	- What: a desk that turns a plain question into one checkable number with its method and its rows.
10	- Next: read `identity.md` (the job), then `rules.md` (what must be true of every answer), then compute from `reference/`.
11	- Information: only `reference/`. The price file holds the prices, the data dictionary says what the columns are, the methodology holds every convention. Nothing comes from memory of markets.
12	- Breaks: months outside the window the methodology defines, assets not in the file, anything needing daily prices, and any request for a forecast or advice.
13	
14	## Where things live
15	
16	| Path | What it holds | Kind |
17	|------|---------------|------|
18	| `identity.md` | the job, who asks, what goes out, what breaks it | instructions |
19	| `rules.md` | numbered pass conditions and the exact shape of the answer line | instructions |
20	| `examples.md` | two right answers and one wrong one, with why | instructions |
21	| `reference/methodology.md` | every convention, one section per quantity; the one home for every fact | state |
22	| `reference/data/data-dictionary.md` | columns, source, coverage of the price file | state |
23	| `reference/data/monthly-adjusted-close.csv` | month-end adjusted closes, SPY TLT GLD USO | state |
24	
25	## Route by what was asked
26	
27	| If the question asks for | Read | Then stop at |
28	|--------------------------|------|--------------|
29	| a return, volatility, Sharpe, drawdown, correlation, best or worst month, for an asset or the equal-weight portfolio | `rules.md`, the methodology section from the table below, the price file | the ANSWER line |
30	| a month before or after the data window | `reference/methodology.md` section 11 | a refusal with the reason, no number |
31	| an asset not in the file, daily data, a forecast, or what to buy | `identity.md`, last section | a one-line decline |
32	| how an answer should look | `examples.md` | the matching example |
33	
34	## Which methodology section
35	
36	| Quantity | Section | Quantity | Section |
37	|----------|---------|----------|---------|
38	| what the file is, the window | 1 | annualised volatility, Sharpe | 6 |
39	| monthly return | 2 | maximum drawdown | 7 |
40	| the equal-weight portfolio | 3 | correlation | 8 |
41	| calendar-year return | 4 | best and worst month | 9 |
42	| cumulative return | 5 | rounding; outside the data | 10; 11 |
43	
44	## The one rule
45	
46	Every number comes from code run on the price file, under the methodology, and the answer line names the section and the rows. No number from memory, ever.
47	
48	## Size
49	
50	Roughly, in tokens: this map 550, identity 350, rules 550, examples 750, methodology 800, data dictionary 300, price file 1,000. Map plus rules plus one question's inputs lands near 3,000.
51	
```

[tool call: Bash] {"command": "ls -la /srv/comp14-runs/treatment-fp89ph1h", "description": "List working directory files"}

[tool result]
```
total 28
drwx------ 4 root root 4096 Oct 13 16:10 .
drwx------ 3 root root   60 Oct 13 16:10 ..
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bash_profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bashrc
drwxr-xr-x 3 root root 4096 Oct 13 16:10 .claude
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitconfig
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitmodules
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .idea
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .mcp.json
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .ripgreprc
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .vscode
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zprofile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zshrc
-rw-r--r-- 1 root root 3136 Oct 13 16:09 README.md
-rw-r--r-- 1 root root 2862 Oct 13 16:09 examples.md
-rw-r--r-- 1 root root 1829 Oct 13 16:09 identity.md
drwxr-xr-x 3 root root 4096 Oct 13 16:09 reference
-rw-r--r-- 1 root root 2264 Oct 13 16:09 rules.md
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-fp89ph1h/identity.md"}

[tool result]
```
1	# Identity: the four-asset desk
2	
3	Instructions, not state. Load this right after the README, in every chat.
4	
5	One job: answer numeric questions about SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from the month-end price file under the methodology, and say plainly when the data does not cover the question.
6	
7	## Who asks, and what do they get?
8	
9	A client or a colleague who wants one number they can check. They get the number, the convention it rests on, the rows it came from, and nothing else. They do not get an opinion on markets.
10	
11	## What comes in?
12	
13	A question in plain words. It may name a period, a weighting, a rebalancing rule or a quantity. It may be silent on some of those. It may ask about a month, an asset or a kind of data the file does not have.
14	
15	## What goes out?
16	
17	A short working, the code that produced the number with its printed result, and one final line in the shape fixed in `rules.md`. Or, when the data does not cover the question, a refusal with the reason and no number.
18	
19	## Where does the information come from?
20	
21	Only from `reference/`: the price file, its data dictionary, and the methodology. The methodology is the one home for every convention, and this file restates none of them. Memory of what markets did is not a source.
22	
23	## What breaks this desk?
24	
25	Questions about months outside the window the methodology defines. Questions that need daily or intraday prices. Questions about assets not in the file. Questions that ask what will happen, or what to buy, sell or hold. A chat in which code cannot run: then the desk says so and gives no number.
26	
27	## What this desk never does
28	
29	It never answers from memory of markets. It never picks a convention silently when the question is silent. It never gives a number for a month it does not have. It never gives investment advice.
30	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-fp89ph1h/rules.md"}

[tool result]
```
1	# Rules: pass conditions for every answer
2	
3	Instructions, not state. Load after `identity.md`, before computing anything. Each rule is stated once. The conventions they point to live in `reference/methodology.md` and are not repeated here.
4	
5	## What must be true of every number?
6	
7	1. It was computed by code that reads `reference/data/monthly-adjusted-close.csv` directly, or rows copied from it verbatim. Never retype a price from memory, and never type a result from memory.
8	2. It follows the methodology section for that quantity. The README's section table says which one. The section number appears in the answer line.
9	3. Its inputs are stated: the columns used and the first and last row dates used.
10	4. It is rounded as methodology section 10 says, with its unit.
11	
12	## What if the question sets its own terms?
13	
14	5. If the question names a period, a weighting or a rebalancing rule, use exactly that. If it is silent, use the methodology's default and write "methodology default" in the working.
15	6. If the question asks for a quantity the methodology does not define, say so, define it in one sentence before computing, and write "ad hoc" in place of the section number.
16	
17	## What if the data does not cover it?
18	
19	7. Any month outside the window in methodology section 1 is answered per section 11: no number, no estimate, no figure from memory. A month after the window is refused exactly like a month before it.
20	8. Any asset not in the file, or any question that needs daily data, gets a one-line decline that says what the file does hold.
21	
22	## What shape does the answer take?
23	
24	9. Working first, short. Then the code and its printed result. Then one final line, exactly in this shape:
25	
26	   `ANSWER: <value with unit> | METHOD: methodology section <n> | SOURCE: monthly-adjusted-close.csv, <columns>, rows <first date> to <last date>`
27	
28	   For a refusal: `ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
29	
30	10. Prose outside the code and the answer line stays under 120 words. The client wants the number, not an essay.
31	
32	## What does this desk never do?
33	
34	11. Never fetch live prices, search the web, or use memory of market history. Never recommend buying, selling or holding anything. Never paste a key, a token or a password into a chat.
35	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-fp89ph1h/examples.md"}

[tool result]
```
1	# Examples: the shape of a right answer, and one wrong one
2	
3	Instructions, not state. Load when unsure how an answer should look. None of these questions is one of the committed test questions. The numbers come from the price file and can be checked under the methodology.
4	
5	## What does a complete answer look like?
6	
7	Question: What was the total return (dividends reinvested) of TLT in calendar year 2023?
8	
9	Answer:
10	
11	Calendar-year total return compounds the twelve monthly simple returns of 2023 (methodology sections 2 and 4). Inputs: the TLT column, rows 2022-12-31 through 2023-12-31, thirteen prices.
12	
13	```
14	import csv
15	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
16	prices = [float(r["TLT"]) for r in rows if "2022-12-31" <= r["Date"] <= "2023-12-31"]
17	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
18	total = 1
19	for r in returns:
20	    total *= 1 + r
21	print(len(prices), round((total - 1) * 100, 1))      # prints 13 2.8
22	```
23	
24	`ANSWER: 2.8% | METHOD: methodology section 4 | SOURCE: monthly-adjusted-close.csv, TLT, rows 2022-12-31 to 2023-12-31`
25	
26	## What does a right refusal look like?
27	
28	Question: What was GLD's return in December 2022?
29	
30	Answer:
31	
32	The file's first row, 2022-12-31, is a base price only; the first return month is 2023-01 (methodology section 1). December 2022 has no return in this data, so there is no number to give.
33	
34	`ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`
35	
36	## What does a wrong answer look like, and why?
37	
38	Question: What was the annualised volatility of SPY's monthly returns in calendar year 2024?
39	
40	Wrong:
41	
42	"SPY's volatility in 2024 was around 12 to 13%, which is typical for the S&P 500 in a calm year."
43	
44	Why it fails: no code was run (rule 1); no rows are named (rule 3); a range instead of one rounded figure (rule 4); no answer line (rule 9); and the figure comes from memory of markets (rule 11). It also happens to be wrong.
45	
46	Right:
47	
48	Annualised volatility is the sample standard deviation of the twelve monthly returns of 2024 times the square root of 12 (methodology section 6). Inputs: the SPY column, rows 2023-12-31 through 2024-12-31.
49	
50	```
51	import csv
52	rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
53	prices = [float(r["SPY"]) for r in rows if "2023-12-31" <= r["Date"] <= "2024-12-31"]
54	returns = [b / a - 1 for a, b in zip(prices, prices[1:])]
55	mean = sum(returns) / len(returns)
56	var = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
57	print(len(returns), round(var ** 0.5 * 12 ** 0.5 * 100, 1))   # prints 12 10.7
58	```
59	
60	`ANSWER: 10.7% | METHOD: methodology section 6 | SOURCE: monthly-adjusted-close.csv, SPY, rows 2023-12-31 to 2024-12-31`
61	
62	## What these examples never do
63	
64	They never stand in for the methodology, they never carry a convention of their own, and none of them is one of the committed test questions.
65	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-fp89ph1h/reference/methodology.md"}

[tool result]
```
1	# Methodology: how the desk computes every number
2	
3	State, not instructions. This is the one home for every convention. Load it before answering any question that involves a number, and name the section you used.
4	
5	## 1. What the dataset is
6	
7	- File: `reference/data/monthly-adjusted-close.csv`. Columns: `Date`, `SPY`, `TLT`, `GLD`, `USO`.
8	- `Date` is the calendar month end. The price on that row is the adjusted close of the last trading day in that month.
9	- Prices are Yahoo Finance adjusted closes (dividends and splits applied), rounded to four decimals, retrieved with `tools/fetch_data.py`. The fetch time is in `reference/data/fetch-log.txt`.
10	- The first row, 2022-12-31, is a base price only. Return months run from 2023-01 to 2026-09, 45 months in all.
11	- The four assets stand for: SPY US stocks, TLT US long-term Treasury bonds, GLD gold, USO oil.
12	
13	## 2. Monthly return
14	
15	Simple return: price this month end divided by price last month end, minus one. Not log returns. Computed per asset from adjusted close.
16	
17	## 3. The house portfolio
18	
19	Equal weight, 25 percent in each of the four assets, rebalanced back to equal weight at every month end. Its monthly return is therefore the plain average of the four assets' monthly returns in that month.
20	
21	Buy and hold is a different portfolio and not the house portfolio: 25 percent in each asset bought at the 2022-12-31 prices and never rebalanced. When a question says "the portfolio" without qualification it means the house portfolio.
22	
23	## 4. Calendar-year total return
24	
25	Compound the twelve monthly returns of that year: multiply (1 + each monthly return), subtract one. Only 2023, 2024 and 2025 are complete years. 2026 runs January to September only and is reported as year to date, never as a calendar-year return.
26	
27	## 5. Cumulative return over a period
28	
29	Multiply (1 + each monthly return) across the period, subtract one. "The full period" means 2023-01 to 2026-09.
30	
31	## 6. Annualised volatility
32	
33	Sample standard deviation of the monthly returns (divide by n minus 1) multiplied by the square root of 12.
34	
35	For the Sharpe ratio, annualised return is the arithmetic mean of monthly returns multiplied by 12, the risk-free rate is zero, and Sharpe is annualised return divided by annualised volatility. This is a stated simplification, not a claim about the right risk-free rate.
36	
37	## 7. Maximum drawdown
38	
39	Build the cumulative index: start at 1.00 on 2022-12-31 and multiply by (1 + monthly return) each month. Drawdown in a month is the index divided by its running peak, minus one. Maximum drawdown is the most negative drawdown; the trough month is the month in which it occurs.
40	
41	## 8. Correlation
42	
43	Pearson correlation of monthly returns over the stated period. Never of price levels. Correlating price levels is the common mistake this section exists to stop.
44	
45	## 9. Best and worst month
46	
47	The largest and smallest monthly return in the stated period, for an asset or for the house portfolio.
48	
49	## 10. Rounding and format
50	
51	Returns, volatility and drawdowns in percent to one decimal. Sharpe ratios and correlations to two decimals. Months as YYYY-MM.
52	
53	## 11. Outside the dataset
54	
55	Any month before 2023-01 or after 2026-09 is not in the dataset. The answer is "not in the dataset; the data ends 2026-09-30", with no number, no estimate, and no figure from memory.
56	
57	## 12. What this file never does
58	
59	It never holds a computed answer. Answers come from the data through these rules at the moment they are asked.
60	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-fp89ph1h/reference/data/data-dictionary.md"}

[tool result]
```
1	# Data dictionary: monthly-adjusted-close.csv
2	
3	State, not instructions. Read this to know what each column is and where it came from.
4	
5	## Where it came from
6	
7	Yahoo Finance end-of-day prices, retrieved with `tools/fetch_data.py` (yfinance, no API key). The exact retrieval time, library versions and row counts are appended to `fetch-log.txt` on every fetch. The committed CSV is the dataset of record. Yahoo adjusts prices retroactively for later dividends and splits, so a re-fetch on another day can differ slightly.
8	
9	## Columns
10	
11	| Column | Meaning |
12	|--------|---------|
13	| `Date` | Calendar month end, YYYY-MM-DD. The row holds the last trading day's adjusted close in that month. |
14	| `SPY` | SPDR S&P 500 ETF, adjusted close in US dollars. Stands for US stocks. |
15	| `TLT` | iShares 20+ Year Treasury Bond ETF, adjusted close in US dollars. Stands for US long bonds. |
16	| `GLD` | SPDR Gold Shares, adjusted close in US dollars. Stands for gold. |
17	| `USO` | United States Oil Fund, adjusted close in US dollars. Stands for oil. |
18	
19	## Coverage
20	
21	- First row 2022-12-31: base price only.
22	- Return months: 2023-01 to 2026-09, 45 months.
23	- Nothing after 2026-09-30 exists in this dataset.
24	
25	## What this file never does
26	
27	It never defines how to compute anything. Conventions live in `reference/methodology.md`.
28	
```

[tool call: Read] {"file_path": "/srv/comp14-runs/treatment-fp89ph1h/reference/data/monthly-adjusted-close.csv"}

[tool result]
```
1	Date,SPY,TLT,GLD,USO
2	2022-12-31,364.7676,85.5002,169.64,70.11
3	2023-01-31,387.7069,92.0355,179.41,69.32
4	2023-02-28,377.9589,87.5713,169.78,67.21
5	2023-03-31,391.9728,91.8092,183.22,66.44
6	2023-04-30,398.2345,92.1198,184.8,67.5
7	2023-05-31,400.0729,89.3421,182.32,60.63
8	2023-06-30,425.9975,89.5361,178.27,63.55
9	2023-07-31,439.9418,87.2581,182.35,73.17
10	2023-08-31,432.7919,84.5163,180.02,75.06
11	2023-09-30,412.2626,77.7964,171.45,80.86
12	2023-10-31,403.313,73.5462,184.09,75.02
13	2023-11-30,440.1531,80.8448,188.75,70.14
14	2023-12-31,460.2484,87.8668,191.17,66.65
15	2024-01-31,467.5785,85.8941,188.45,70.92
16	2024-02-29,491.9801,83.9596,189.31,73.36
17	2024-03-31,508.0688,84.6169,205.72,78.73
18	2024-04-30,487.5835,79.1545,211.87,78.38
19	2024-05-31,512.2454,81.4396,215.3,74.82
20	2024-06-30,530.3175,82.9195,215.01,79.59
21	2024-07-31,536.7392,85.9294,226.55,77.74
22	2024-08-31,549.2804,87.7436,231.29,74.34
23	2024-09-30,560.8178,89.498,243.06,69.92
24	2024-10-31,555.8132,84.616,253.51,73.08
25	2024-11-30,588.9584,86.2975,245.59,71.61
26	2024-12-31,574.788,80.7908,242.13,75.55
27	2025-01-31,590.2247,81.1886,258.56,78.02
28	2025-02-28,582.7319,85.814,263.27,75.22
29	2025-03-31,550.2626,84.7802,288.14,77.33
30	2025-04-30,545.4916,83.6268,303.77,63.56
31	2025-05-31,579.7731,80.9419,303.6,67.15
32	2025-06-30,609.5654,83.0982,304.83,73.11
33	2025-07-31,623.6046,82.1512,302.96,79.59
34	2025-08-31,636.4007,82.1616,318.07,74.84
35	2025-09-30,659.0695,85.112,355.47,73.75
36	2025-10-31,674.78,86.2875,368.12,72.56
37	2025-11-30,676.0959,86.5225,387.88,71.07
38	2025-12-31,676.635,84.2222,396.31,69.16
39	2026-01-31,686.6071,84.1932,444.95,79.52
40	2026-02-28,680.6734,88.0945,483.75,81.95
41	2026-03-31,647.0621,84.3681,430.29,127.25
42	2026-04-30,715.0377,83.6597,423.66,147.09
43	2026-05-31,752.6671,84.1059,417.12,129.09
44	2026-06-30,744.9202,85.0865,368.38,106.44
45	2026-07-31,745.1796,81.2799,371.54,129.17
46	2026-08-31,765.15,81.8752,408.42,133.7
47	2026-09-30,762.63,77.468,380.84,145.66
48	
```

[tool call: Bash] {"command": "python3 -I -c '\nimport csv\nrows = list(csv.DictReader(open(\"reference/data/monthly-adjusted-close.csv\")))\nrows = [r for r in rows if \"2025-12-31\" <= r[\"Date\"] <= \"2026-09-30\"]\nA = [\"SPY\",\"TLT\",\"GLD\",\"USO\"]\nport = []\nfor a, b in zip(rows, rows[1:]):\n    rets = [float(b[k]) / float(a[k]) - 1 for k in A]\n    port.append((b[\"Date\"][:7], sum(rets) / 4))\nfor m, r in port: print(m, round(r * 100, 2))\nbest = max(port, key=lambda x: x[1])\nprint(len(port), best[0], round(best[1] * 100, 1))\n'", "description": "Compute equal-weight portfolio monthly returns for 2026"}

[tool result]
```
2026-01 7.17
2026-02 3.89
2026-03 8.76
2026-04 5.93
2026-05 -2.0
2026-06 -7.27
2026-07 4.44
2026-08 4.21
2026-09 -0.88
9 2026-03 8.8
```

The best month was **March 2026 (2026-03)**, when the portfolio returned **8.8%**.

I used the folder's standard equal-weight portfolio (methodology section 3), which matches your setup: 25% in each fund, reset at every month end. That makes each month's portfolio return the plain average of the four funds' simple monthly returns (section 2). The best month is the highest of those returns in the period (section 9). I used the SPY, TLT, GLD and USO columns, with prices from 2025-12-31 (the base) through 2026-09-30, which gives 9 monthly returns.

```
import csv
rows = list(csv.DictReader(open("reference/data/monthly-adjusted-close.csv")))
rows = [r for r in rows if "2025-12-31" <= r["Date"] <= "2026-09-30"]
A = ["SPY","TLT","GLD","USO"]
port = []
for a, b in zip(rows, rows[1:]):
    rets = [float(b[k]) / float(a[k]) - 1 for k in A]
    port.append((b["Date"][:7], sum(rets) / 4))
for m, r in port: print(m, round(r * 100, 2))
best = max(port, key=lambda x: x[1])
print(len(port), best[0], round(best[1] * 100, 1))
```
```
2026-01 7.17
2026-02 3.89
2026-03 8.76
2026-04 5.93
2026-05 -2.0
2026-06 -7.27
2026-07 4.44
2026-08 4.21
2026-09 -0.88
9 2026-03 8.8
```

`ANSWER: 2026-03, 8.8% | METHOD: methodology section 9 | SOURCE: monthly-adjusted-close.csv, SPY TLT GLD USO, rows 2025-12-31 to 2026-09-30`

Status: ok; turns: 10; seconds: 26.7; tokens in/out: 8/1648; files read: ['/srv/comp14-runs/treatment-fp89ph1h/README.md', '/srv/comp14-runs/treatment-fp89ph1h/identity.md', '/srv/comp14-runs/treatment-fp89ph1h/rules.md', '/srv/comp14-runs/treatment-fp89ph1h/examples.md', '/srv/comp14-runs/treatment-fp89ph1h/reference/methodology.md', '/srv/comp14-runs/treatment-fp89ph1h/reference/data/data-dictionary.md', '/srv/comp14-runs/treatment-fp89ph1h/reference/data/monthly-adjusted-close.csv']; bash calls: 2; asked to leave sandbox: 0

## Q8

**Prompt (verbatim):** What was the return of that same equal-weight SPY, TLT, GLD and USO portfolio in October 2026?

[tool call: Bash] {"command": "cat README.md && ls -la", "description": "Read README and list files"}

[tool result]
```
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
total 28
drwx------ 4 root root 4096 Oct 13 16:10 .
drwx------ 3 root root   60 Oct 13 16:10 ..
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bash_profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .bashrc
drwxr-xr-x 3 root root 4096 Oct 13 16:10 .claude
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitconfig
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .gitmodules
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .idea
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .mcp.json
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .profile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .ripgreprc
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .vscode
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zprofile
crw-rw-rw- 1 root root 1, 3 Oct 13 11:53 .zshrc
-rw-r--r-- 1 root root 3136 Oct 13 16:09 README.md
-rw-r--r-- 1 root root 2862 Oct 13 16:09 examples.md
-rw-r--r-- 1 root root 1829 Oct 13 16:09 identity.md
drwxr-xr-x 3 root root 4096 Oct 13 16:09 reference
-rw-r--r-- 1 root root 2264 Oct 13 16:09 rules.md
```

[tool call: Bash] {"command": "cat identity.md rules.md examples.md reference/methodology.md reference/data/data-dictionary.md && tail -5 reference/data/monthly-adjusted-close.csv && head -3 reference/data/monthly-adjusted-close.csv", "description": "Read instructions, methodology, and data edges"}

[tool result]
```
# Identity: the four-asset desk

Instructions, not state. Load this right after the README, in every chat.

One job: answer numeric questions about SPY, TLT, GLD and USO, and the equal-weight portfolio of the four, from the month-end price file under the methodology, and say plainly when the data does not cover the question.

## Who asks, and what do they get?

A client or a colleague who wants one number they can check. They get the number, the convention it rests on, the rows it came from, and nothing else. They do not get an opinion on markets.

## What comes in?

A question in plain words. It may name a period, a weighting, a rebalancing rule or a quantity. It may be silent on some of those. It may ask about a month, an asset or a kind of data the file does not have.

## What goes out?

A short working, the code that produced the number with its printed result, and one final line in the shape fixed in `rules.md`. Or, when the data does not cover the question, a refusal with the reason and no number.

## Where does the information come from?

Only from `reference/`: the price file, its data dictionary, and the methodology. The methodology is the one home for every convention, and this file restates none of them. Memory of what markets did is not a source.

## What breaks this desk?

Questions about months outside the window the methodology defines. Questions that need daily or intraday prices. Questions about assets not in the file. Questions that ask what will happen, or what to buy, sell or hold. A chat in which code cannot run: then the desk says so and gives no number.

## What this desk never does

It never answers from memory of markets. It never picks a convention silently when the question is silent. It never gives a number for a month it does not have. It never gives investment advice.
# Rules: pass conditions for every answer

Instructions, not state. Load after `identity.md`, before computing anything. Each rule is stated once. The conventions they point to live in `reference/methodology.md` and are not repeated here.

## What must be true of every number?

1. It was computed by code that reads `reference/data/monthly-adjusted-close.csv` directly, or rows copied from it verbatim. Never retype a price from memory, and never type a result from memory.
2. It follows the methodology section for that quantity. The README's section table says which one. The section number appears in the answer line.
3. Its inputs are stated: the columns used and the first and last row dates used.
4. It is rounded as methodology section 10 says, with its unit.

## What if the question sets its own terms?

5. If the question names a period, a weighting or a rebalancing rule, use exactly that. If it is silent, use the methodology's default and write "methodology default" in the working.
6. If the question asks for a quantity the methodology does not define, say so, define it in one sentence before computing, and write "ad hoc" in place of the section number.

## What if the data does not cover it?

7. Any month outside the window in methodology section 1 is answered per section 11: no number, no estimate, no figure from memory. A month after the window is refused exactly like a month before it.
8. Any asset not in the file, or any question that needs daily data, gets a one-line decline that says what the file does hold.

## What shape does the answer take?

9. Working first, short. Then the code and its printed result. Then one final line, exactly in this shape:

   `ANSWER: <value with unit> | METHOD: methodology section <n> | SOURCE: monthly-adjusted-close.csv, <columns>, rows <first date> to <last date>`

   For a refusal: `ANSWER: not in the dataset | METHOD: methodology section 11 | SOURCE: none`

10. Prose outside the code and the answer line stays under 120 words. The client wants the number, not an essay.

## What does this desk never do?

11. Never fetch live prices, search the web, or use memory of market history. Never recommend buying, selling or holding anything. Never paste a key, a token or a password into a chat.
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
2026-05-31,752.6671,84.1059,417.12,129.09
2026-06-30,744.9202,85.0865,368.38,106.44
2026-07-31,745.1796,81.2799,371.54,129.17
2026-08-31,765.15,81.8752,408.42,133.7
2026-09-30,762.63,77.468,380.84,145.66
Date,SPY,TLT,GLD,USO
2022-12-31,364.7676,85.5002,169.64,70.11
2023-01-31,387.7069,92.0355,179.41,69.32
```

I can't give a number for October 2026, because the price file doesn't cover it. The data runs through 2026-09-30 (methodology section 1, confirmed by the file's last row), and any month after 2026-09 is outside the dataset (section 11). On top of that, today is 2026-10-13, so October hasn't ended and there is no month-end price for it yet.

`ANSWER: not in the dataset; the data ends 2026-09-30 | METHOD: methodology section 11 | SOURCE: none`

Status: ok; turns: 3; seconds: 21.5; tokens in/out: 6/492; files read: []; bash calls: 2; asked to leave sandbox: 0
