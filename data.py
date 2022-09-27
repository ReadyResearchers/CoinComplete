import pandas as pd
from binance.client import Client
from bot import api_key, secret_key
import time
from datetime import datetime
import plotly.graph_objects as go

client = Client(api_key, secret_key)

coins = ['BTC','ETH']

merge = False
for coin in coins:
    print(f'gathering {coin}...')
    start_str = 'Sep 16, 2022'
    end_str = 'Sep 26, 2022'

    klines = client.get_historical_klines(symbol=f'{coin}USDT', 
                                          interval=client.KLINE_INTERVAL_1MINUTE, 
                                          start_str=start_str,
                                          end_str=end_str)
    cols = ['OpenTime',
            f'{coin}-USD_Open',
            f'{coin}-USD_High',
            f'{coin}-USD_Low',
            f'{coin}-USD_Close',
            f'{coin}-USD_volume',
            'CloseTime',
            f'{coin}-QuoteAssetVolume',
            f'{coin}-NumberOfTrades',
            f'{coin}-TBBAV',
            f'{coin}-TBQAV',
            f'{coin}-ignore']

    coin_df = pd.DataFrame(klines,columns=cols)
    
    if merge == True:
        all_coins_df = pd.merge(coin_df,all_coins_df,how='inner',on=['OpenTime','CloseTime'])
    else:
        all_coins_df = coin_df
        merge = True
        
    time.sleep(10)

all_coins_df['OpenTime'] = [datetime.fromtimestamp(ts / 1000) for ts in all_coins_df['OpenTime']]
all_coins_df['CloseTime'] = [datetime.fromtimestamp(ts / 1000) for ts in all_coins_df['CloseTime']]

for col in all_coins_df.columns:
    if not 'Time' in col:
        all_coins_df[col] = all_coins_df[col].astype(float)

fig = go.Figure(data=[go.Candlestick(x=all_coins_df['OpenTime'],
                open=all_coins_df['BTC-USD_Open'],
                high=all_coins_df['BTC-USD_High'],
                low=all_coins_df['BTC-USD_Low'],
                close=all_coins_df['BTC-USD_Close'])])

fig2 = go.Figure(data=[go.Candlestick(x=all_coins_df['OpenTime'],
                open=all_coins_df['ETH-USD_Open'],
                high=all_coins_df['ETH-USD_High'],
                low=all_coins_df['ETH-USD_Low'],
                close=all_coins_df['ETH-USD_Close'])])


fig.show()
fig2.show()

all_coins_df.to_csv('crypto_data.csv',index=False)