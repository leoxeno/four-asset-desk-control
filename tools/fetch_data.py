"""Fetch the month-end adjusted-close snapshot from Yahoo Finance.

No API key is needed. The committed CSV is the dataset of record: Yahoo applies
dividend and split adjustments retroactively, so a re-fetch on a later date can
differ in the fourth decimal and occasionally more. Re-fetch to check
provenance, not to replace the snapshot.

Usage:
    python3 tools/fetch_data.py            # writes reference/data/monthly-adjusted-close.csv
    python3 tools/fetch_data.py --out X    # writes somewhere else for comparison
"""
import argparse
import datetime as dt
import pathlib

import pandas as pd
import yfinance as yf

TICKERS = ["SPY", "TLT", "GLD", "USO"]
FIRST_PRICE = "2022-12-31"   # base price only; the first return month is 2023-01
LAST_PRICE = "2026-09-30"    # the dataset ends here
ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "reference" / "data" / "monthly-adjusted-close.csv"
LOG = ROOT / "reference" / "data" / "fetch-log.txt"


def fetch() -> pd.DataFrame:
    raw = yf.download(
        TICKERS,
        start="2022-12-01",
        end="2026-10-03",
        interval="1d",
        auto_adjust=True,   # adjusted close: dividends and splits applied
        progress=False,
    )
    close = raw["Close"] if isinstance(raw.columns, pd.MultiIndex) else raw
    close = close[TICKERS].dropna(how="all")
    monthly = close.resample("ME").last()          # last available trading day of each month
    monthly = monthly.loc[FIRST_PRICE:LAST_PRICE]
    monthly.index = monthly.index.strftime("%Y-%m-%d")
    monthly.index.name = "Date"
    return monthly.round(4)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    args = parser.parse_args()
    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    monthly = fetch()
    monthly.to_csv(out)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    line = (
        f"{stamp}  yfinance {yf.__version__}  pandas {pd.__version__}  "
        f"rows {len(monthly)}  first {monthly.index[0]}  last {monthly.index[-1]}  -> {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}\n"
    )
    if out == DEFAULT_OUT:
        LOG.parent.mkdir(parents=True, exist_ok=True)
        with LOG.open("a") as fh:
            fh.write(line)
    print(line, end="")


if __name__ == "__main__":
    main()
