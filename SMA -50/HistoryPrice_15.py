from datetime import date
import sys
import pandas as pd
from nsepy import get_history


import numpy as np

def process_trade(trade_list):
    with open('SMA_filename15.txt', 'w') as f:
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

trade_list =['TATACOMM','OFSS','DALBHARAT','AARTIIND','BHARATFORG','TVSMOTOR','AUBANK','VBL','ABCAPITAL','3MINDIA','SUPREMEIND','WHIRLPOOL','SUNDARMFIN','IRCTC','TRENT','LTTS','LAURUSLABS','IPCALAB','RECLTD','NIACL','GLAXO','ATUL','DEEPAKNTR','NHPC','PFIZER','BAYERCROP','CANBK','CROMPTON','LALPATHLAB','TIINDIA','CUMMINSIND','DIXON','TATAELXSI','SYNGENE','INDIAMART','RAMCOCEM','BANKINDIA','RELAXO','MAXHEALTH','UNIONBANK','POLYCAB','NAM-INDIA','EMAMILTD','JKCEMENT','L&TFH','COROMANDEL','LICHSGFIN','COFORGE','BHEL','TORNTPOWER','OBEROIRLTY','SUNTV','JSWENERGY','M&MFIN','ENDURANCE','APLLTD','GILLETTE','ZEEL']

process_trade(trade_list)
