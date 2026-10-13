# Walk test: a fresh chat, only the folder

Run once before treatment run 1, with the folder as committed in `2227e89`: three prompts, each in a fresh headless session with exactly the treatment arm's flags, sandbox and working directory (see `PROTOCOL.md`), none of them a scored run. What it answered is logged verbatim by `tools/walk_test.py`, with the files it opened; the raw event streams are in `walk-test/`. This is the icm-architect walk test: an agent with no memory must orient, act and report from the files alone. The "What I changed" lines and the verdict were written by hand afterwards.

## Prompt 1

`What is this project for, and what do you need from me to do your job?`

What it answered:

(run 2026-10-13T16:02+01:00, 8 turns, 24.5s, status ok; files opened with Read: ['/srv/comp14-runs/treatment-yf0c_i69/README.md', '/srv/comp14-runs/treatment-yf0c_i69/identity.md', '/srv/comp14-runs/treatment-yf0c_i69/rules.md', '/srv/comp14-runs/treatment-yf0c_i69/reference/data/data-dictionary.md', '/srv/comp14-runs/treatment-yf0c_i69/reference/methodology.md']; bash calls: 2)

**What this project is for**

It's a small "desk" that answers numeric questions about four ETFs (SPY for US stocks, TLT for long Treasuries, GLD for gold, USO for oil) and about an equal-weight portfolio of the four, rebalanced monthly. Every answer comes from one file of month-end prices and follows one written methodology. Each answer is a single number you can check, with a short working, the code that produced it, and a fixed final line giving the value, the methodology section and the rows used.

It can calculate monthly, calendar-year and cumulative returns, annualised volatility, Sharpe ratio (with a risk-free rate of zero), maximum drawdown, correlation, and best or worst month.

It will refuse:
- **Months outside 2023-01 to 2026-09.** The data ends 2026-09-30, so I'll say "not in the dataset" and give no estimate.
- **Other assets, daily data, forecasts, or buy/sell/hold advice.** These get a one-line decline.

I checked the setup and it works: the price file has the 2022-12-31 base row plus 45 return months, and Python with pandas runs here, so I can calculate rather than quote from memory.

**What I need from you**

1. **A question.** Plain words are fine, for example "What was the portfolio's max drawdown?" or "SPY–GLD correlation in 2024?"
2. **Your own terms, if you have them.** If you name a period, a weighting or a rebalancing rule, I'll use exactly that. If you don't, I'll use the methodology's default and say so. One example: "the portfolio" means the monthly-rebalanced equal-weight portfolio, not buy-and-hold.

You don't need to give me data, API keys or logins. Everything comes from the files in `reference/`.

One gap: the data notes mention a `tools/fetch_data.py` script for refreshing prices, but it isn't in this folder. That doesn't affect answers, because the saved price file is the official dataset. It just means I can't refresh it, and I wouldn't fetch live prices anyway.

What I changed: Nothing. It oriented from the files alone and asked only for a question. The one gap it named, that the data dictionary mentions a fetch script which is not in the folder, changes no answer and is left as it is. It opened five of the seven files to orient; how much the first map makes the model read is what the treatment runs measure.

## Prompt 2

`What must you never do here?`

What it answered:

(run 2026-10-13T16:03+01:00, 4 turns, 16.1s, status ok; files opened with Read: ['/srv/comp14-runs/treatment-k1x2w2x8/README.md', '/srv/comp14-runs/treatment-k1x2w2x8/identity.md', '/srv/comp14-runs/treatment-k1x2w2x8/rules.md']; bash calls: 0)

Here are the things this desk must never do, taken from `identity.md` (last section) and `rules.md` (rules 1, 7 and 11):

1. **Never answer from memory.** That covers market history, prices and results alike. Every number has to come from code that reads `reference/data/monthly-adjusted-close.csv`.
2. **Never fetch live prices or search the web.** The only source is `reference/`.
3. **Never quietly pick a convention when the question doesn't specify one.** Use the methodology default and say so.
4. **Never give a number for a month outside the data window.** That includes estimates. Months before and after the window are both refused, per methodology section 11.
5. **Never give investment advice**, such as what to buy, sell or hold, and never make forecasts.
6. **Never paste a key, token or password into a chat.**

The rules also say that if code can't run, the desk says so and gives no number.

What I changed: Nothing. The six never-events are the last section of `identity.md` and rule 11, with rule 7 for months outside the window, and it found them in three files.

## Prompt 3

`Which file would you open to find out how a drawdown is defined, and which section?`

What it answered:

(run 2026-10-13T16:03+01:00, 3 turns, 14.1s, status ok; files opened with Read: ['/srv/comp14-runs/treatment-0t5favuj/README.md']; bash calls: 0)

Open `reference/methodology.md` and go to **section 7, "Maximum drawdown"** (around line 37).

The README's methodology table points drawdown to section 7, and the file's headings confirm it. The README also says `methodology.md` is the only place conventions like this are defined, so no other file has its own drawdown definition.

If you're computing a drawdown rather than just looking up the definition, the README also has you read `rules.md` first and use `reference/data/monthly-adjusted-close.csv` for the prices.

What I changed: Nothing. It read only the map and sent the drawdown question to methodology section 7.

## Verdict

Yes. It oriented from the files alone: prompt 1 read the map, identity, rules, the data dictionary and the methodology, checked that the price file and Python were there, and asked for nothing the folder holds; prompt 2 listed the never-events from `identity.md` and rules 1, 7 and 11; prompt 3 read only `README.md` and sent the drawdown question to methodology section 7. Nothing in the folder was changed before treatment run 1. The private pilot's walk test on this same map had found one thing, a README footer that told the model it was in a test, and that footer was already gone from the map committed here.
