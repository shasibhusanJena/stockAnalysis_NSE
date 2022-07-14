from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np

def process_trade(trade_list):
    with open('SMA_filename14.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print('This message will be written to a file.')
        for trade in trade_list:
            data = get_history(symbol=trade, start=date(2019, 1, 1), end=date.today())
            df = pd.DataFrame(data, columns=['Symbol', 'Series', 'Close', 'Volume'])
            df7 = pd.DataFrame(data, columns=['Close'])
            short_rolling20 = df7.rolling(window=20).mean()
            df['avgPrice20'] = short_rolling20
            short_rolling50 = df7.rolling(window=50).mean()
            df['avgPrice50'] = short_rolling50
            short_rolling200 = df7.rolling(window=200).mean()
            df['avgPrice200'] = short_rolling200
            df = df.dropna()
            df['Signal'] = 0.0
            df['Signal'] = np.where((df['avgPrice20'] > df['avgPrice50']) & (df['avgPrice50'] < df['avgPrice200']), 1.0, 0.0)
            df['Position'] = df['Signal'].diff()
            print(df.tail(30))
            print('-----------------------------------------------')

trade_list=['DBL','ISEC','FSL','MCX','RELIANCE','HINDUNILVR','IOC','HDFC','KOTAKBANK','BAJFINANCE','SBIN','BHARTIARTL','HCLTECH','ASIANPAINT','AXISBANK','MARUTI','DMART','ULTRACEMCO','JSWSTEEL','BAJAJFINSV','ADANIGREEN','SUNPHARMA','NESTLEIND','ADANIPORTS','ATGL','ADANIENT','TATASTEEL','ONGC','HDFCLIFE','HINDZINC','ADANITRANS','TITAN','POWERGRID','BAJAJ-AUTO','DIVISLAB','NTPC','SHREECEM','SBILIFE','GRASIM','TECHM','DABUR','BPCL','SBICARD','PIDILITIND','M&M','HINDALCO','COALINDIA','BRITANNIA','ICICIPRULI','GODREJCP','INDUSINDBK','CIPLA','MOTHERSUMI','BERGEPAINT','INDUSTOWER','GAIL','EICHERMOT','SIEMENS','ICICIGI','DLF','INDIGO','HAVELLS','AMBUJACEM','CADILAHC','MARICO','NAUKRI','AUROPHARMA','TATACONSUM','HDFCAMC','HEROMOTOCO','LUPIN','NMDC','JINDALSTEL','MUTHOOTFIN','BANDHANBNK','APOLLOHOSP','CHOLAFIN','BIOCON','TORNTPHARM','PGHH','IDBI','COLPAL','BOSCHLTD','MCDOWELL-N','PIIND','BAJAJHLDNG','PNB','PEL','SRF','HONAUT','HINDPETRO','GUJGASLTD','BANKBARODA','MINDTREE','PETRONET','JUBLFOOD','GICRE','BALKRISIND','IDFCFIRSTB','CONCOR','ALKEM','GODREJPROP','MPHASIS','ABBOTINDIA','ASHOKLEY','YESBANK','PAGEIND','TATAPOWER','SRTRANSFIN','UBL','VOLTAS','KANSAINER','ASTRAL','MFSL']

process_trade(trade_list)
