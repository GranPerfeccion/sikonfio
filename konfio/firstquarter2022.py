from pycoingecko import CoinGeckoAPI
from datetime import datetime
import pandas as pd
from firebase import firebase

firebase = firebase.FirebaseApplication("https://sikonfio-default-rtdb.firebaseio.com/",None)

cg = CoinGeckoAPI()

dt = datetime(2022, 1, 1)

from_date = pd.Timestamp(dt.replace(day=1)).timestamp()
to_date = pd.Timestamp(dt.replace(month=dt.month + 3, day=1))
to_date = pd.Timestamp(to_date).timestamp()

print(from_date)
print(to_date)

ohlc = cg.get_coin_market_chart_range_by_id(
    id="bitcoin", vs_currency="usd", from_timestamp=from_date, to_timestamp=to_date,localization = False
)

ohlc_df = pd.DataFrame(ohlc)
ohlc_df.columns = ["prices", "market_caps", "total_volumes"]
ohlc_df[['date', 'price']] = ohlc_df["prices"].apply(lambda x: pd.Series(str(x).replace('[','').replace(']','').split(",")))
# ohlc_df['date'] = pd.to_datetime(ohlc_df['date'], unit="ms")
# print(ohlc_df[['date', 'price']])
ohlc_df['date'] = pd.to_datetime(ohlc_df['date'], unit='ms').dt.strftime('%d%b%Y')

postdata = ohlc_df[['date', 'price']].to_dict()

print(postdata)

# Assumes any auth/headers you need are already taken care of.
firebase.post('/firstquarter2022', postdata)
# print(postdata)