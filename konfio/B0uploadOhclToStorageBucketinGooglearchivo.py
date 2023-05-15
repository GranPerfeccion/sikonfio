

import firebase_admin
from firebase_admin import credentials, storage
import pandas as pd
import io
import plotly.graph_objects as go
from pycoingecko import CoinGeckoAPI

# Initialize Firebase
cred = credentials.Certificate("/Users/samantabhadra/sikonfio/Konfio/sikonfio.json")
default_app = firebase_admin.initialize_app(cred, {'storageBucket': "sikonfio.appspot.com"})

# Initialize CoinGeckoAPI
cg = CoinGeckoAPI()

# Fetch data from CoinGeckoAPI
ohlc = cg.get_coin_ohlc_by_id(id="bitcoin", vs_currency="usd", days="max")
ohlc_df = pd.DataFrame(ohlc, columns=["date", "open", "high", "low", "close"])
ohlc_df["date"] = pd.to_datetime(ohlc_df["date"], unit="ms")

# Store data in an Excel file
output = io.BytesIO()
ohlc_df.to_excel(output, index=False, sheet_name="Sheet1")

# Upload the Excel file to the Firebase Storage bucket
output.seek(0)  # Reset the file position to the beginning
bucket = storage.bucket()
blob = bucket.blob("ohlc_data.xlsx")
blob.upload_from_file(output, content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

# Plot the OHLC data
fig = go.Figure(data=go.Ohlc(x=ohlc_df['date'],
                             open=ohlc_df['open'],
                             high=ohlc_df['high'],
                             low=ohlc_df['low'],
                             close=ohlc_df['close']))
fig.show()
