import pandas as pd
from binance.client import Client
from keys import api_key, secret_key
import time
from datetime import datetime
import plotly.graph_objects as go
from ta import add_all_ta_features
import warnings
import plotly.express as px
from plot_utils import shade_plot
import os
from sklearn.decomposition import PCA

warnings.filterwarnings('ignore')

api_secret = secret_key

client = Client(api_key, secret_key,tld="us")

coins = ['BTC','ETH']

merge = False
for coin in coins:
    print(f'getting {coin}...')
    start_str = 'Jan 1, 2016'
    end_str = 'Mar 20, 2023'

    klines = client.get_historical_klines(symbol=f'{coin}USDT', interval=client.KLINE_INTERVAL_1HOUR, start_str=start_str, end_str=end_str)
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

    coin_data = pd.DataFrame(klines,columns=cols)
    
    coin_data['OpenTime'] = [datetime.fromtimestamp(ts / 1000) for ts in coin_data['OpenTime']]
    coin_data['CloseTime'] = [datetime.fromtimestamp(ts / 1000) for ts in coin_data['CloseTime']]
    
    for col in coin_data.columns:
        if not 'Time' in col:
            coin_data[col] = coin_data[col].astype(float)
    
    coin_data.to_csv(f'.//data//{coin}_2021_1y.csv')

data_path = './/data//'
symbols = ['BTC','ETH']
filenames = os.listdir(data_path)

cols = ['volume_cmf',
                'volume_mfi',
                'volatility_dcp',
                'trend_psar_down_indicator',
                'trend_psar_up_indicator',
                'trend_stc',
                'momentum_rsi',
                'momentum_stoch_rsi',
                'momentum_stoch_rsi_k',
                'momentum_stoch_rsi_d',
                'momentum_stoch']

hours = 4
Xs = []
ys = []
for file in filenames:
    df = pd.read_csv(f'{data_path}{file}')
    symbol = file.split('_')[0]
    
    print(f'preprocessing {symbol}...')
    
    dts = []
    for i in range(len(df)):
        dts.append(datetime.strptime(df['OpenTime'].iloc[i].split('.')[0], '%Y-%m-%d %H:%M:%S'))
    
    df['OpenTime'] = dts
    
    dts = []
    for i in range(len(df)):
        dts.append(datetime.strptime(df['CloseTime'].iloc[i].split('.')[0], '%Y-%m-%d %H:%M:%S'))
    
    df['CloseTime'] = dts
    
    #Sell at open of future hour, buy at close
    labels = []
    for i in range(len(df)-hours):
        labels.append(df[f'{symbol}-USD_Open'].iloc[i+hours] / df[f'{symbol}-USD_Close'].iloc[i])
    
    df = df.head(len(df)-hours)
    df['label'] = labels
    
    add_all_ta_features(df,
                   open=f'{symbol}-USD_Open',
                   close=f'{symbol}-USD_Close',
                   high=f'{symbol}-USD_High',
                   low=f'{symbol}-USD_Low',
                   volume=f'{symbol}-USD_volume',
                   fillna=True)
    
    df = df[50:].reset_index(drop=True)
    df_pca = df[cols]
    
    X = (df_pca-df_pca.min())/(df_pca.max()-df_pca.min())
    Xs.append(X)
    
    y = df['label']
    ys.append(y)

X = pd.concat(Xs)
y = pd.concat(ys) 


pca = PCA(n_components=2)
pca.fit(X)
pcas = pd.DataFrame(pca.transform(X),columns=['pca1','pca2'])
pcas['profit / loss'] = list(y)

pcas_fit = pcas[(pcas['profit / loss'] < 0.99) | (pcas['profit / loss'] > 1.01)]

fig = px.scatter(pcas_fit,
           x='pca1',
           y='pca2',
           color='profit / loss',
           color_continuous_scale='RdBu',
           range_color=[0.97,1.03],
           color_continuous_midpoint=1,
                template="plotly_dark")
fig.show()

shade_plot(pcas,'pca1','pca2','profit / loss',50)
