import plotly.graph_objects as go
import pandas as pd
from pycoingecko import CoinGeckoAPI
from datetime import datetime

cg = CoinGeckoAPI()

dt = datetime(2022, 1, 1)
from_date = pd.Timestamp(dt.replace(day=1)).timestamp()
to_date = pd.Timestamp(dt.replace(month=dt.month + 3, day=1)).timestamp()

ohlc = cg.get_coin_ohlc_by_id(id="bitcoin", vs_currency="usd", days="max")
ohlc_df = pd.DataFrame(ohlc)
ohlc_df.columns = ["date", "open", "high", "low", "close"]
ohlc_df["date"] = pd.to_datetime(ohlc_df["date"], unit="ms")

# Filter data for the first quarter of 2022
ohlc_df = ohlc_df[(ohlc_df["date"] >= pd.to_datetime(from_date, unit="s")) &
                  (ohlc_df["date"] < pd.to_datetime(to_date, unit="s"))]

fig = go.Figure(data=go.Ohlc(x=ohlc_df['date'],
                    open=ohlc_df['open'],
                    high=ohlc_df['high'],
                    low=ohlc_df['low'],
                    close=ohlc_df['close']))
fig.show()