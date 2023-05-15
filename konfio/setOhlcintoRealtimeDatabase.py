import firebase_admin
from pycoingecko import CoinGeckoAPI
import pandas as pd
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase
cred = credentials.Certificate("/Users/samantabhadra/sikonfio/Konfio/sikonfio.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sikonfio-default-rtdb.firebaseio.com/'
})

# Initialize CoinGeckoAPI
cg = CoinGeckoAPI()

# Fetch data from CoinGeckoAPI
ohlc = cg.get_coin_ohlc_by_id(id="bitcoin", vs_currency="usd", days="max")
ohlc_df = pd.DataFrame(ohlc, columns=["date", "open", "high", "low", "close"])
ohlc_df["date"] = pd.to_datetime(ohlc_df["date"], unit="ms")
ohlc_df["date"] = ohlc_df["date"].dt.strftime('%Y-%m-%d %H:%M:%S')  # Convert to string representation

# Convert DataFrame to dictionary
ohlc_dict = ohlc_df.to_dict(orient='records')

# Reference to the database root
ref = db.reference('/')

# Set the 'ohlc_data' node with the OHLC data
ref.child('ohlc_data').set(ohlc_dict)
