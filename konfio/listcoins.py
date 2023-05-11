from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()

coins = cg.get_coins_list()
df=pd.DataFrame(coins)


df=pd.DataFrame(coins, columns=['id','name','symbol'])

print(df[df.apply(lambda row: row.astype(str).str.contains('bitcoin').any(), axis=1)])