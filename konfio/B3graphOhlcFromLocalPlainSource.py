import pandas as pd
import plotly.graph_objects as go

# Read the OHLC data from the Excel file
ohlc_df = pd.read_excel("/Users/samantabhadra/sikonfio/Konfio/ohlc_data.xlsx", sheet_name="Sheet1")

# Plot the OHLC data
fig = go.Figure(data=go.Ohlc(x=ohlc_df['date'],
                             open=ohlc_df['open'],
                             high=ohlc_df['high'],
                             low=ohlc_df['low'],
                             close=ohlc_df['close']))
fig.show()