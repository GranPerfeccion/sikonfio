from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()

coins = cg.get_coins_list()
df=pd.DataFrame(coins)


df=pd.DataFrame(coins, columns=['id','name','symbol'])

# https://www.coingecko.com/en/api/documentation
print(cg.get_coin_by_id(id='bitcoin'))

print(df[df.apply(lambda row: row.astype(str).str.contains('bitcoin').any(), axis=1)])
