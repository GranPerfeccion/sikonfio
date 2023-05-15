import firebase_admin
from firebase_admin import credentials, db
import pandas as pd
import plotly.graph_objects as go

# Initialize Firebase
cred = credentials.Certificate("/Users/samantabhadra/sikonfio/Konfio/sikonfio.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://sikonfio-default-rtdb.firebaseio.com/'
})

# Reference to the database root
ref = db.reference('/')

# Retrieve the OHLC data from the database
ohlc_data = ref.child('ohlc_data').get()

# Convert the data to a DataFrame
ohlc_df = pd.DataFrame(ohlc_data)

# Convert the 'date' column to datetime type
ohlc_df['date'] = pd.to_datetime(ohlc_df['date'])

# Plot the OHLC data
fig = go.Figure(data=go.Ohlc(x=ohlc_df['date'],
                             open=ohlc_df['open'],
                             high=ohlc_df['high'],
                             low=ohlc_df['low'],
                             close=ohlc_df['close']))
fig.show()