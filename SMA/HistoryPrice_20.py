from datetime import date
import sys
import pandas as pd
from nsepy import get_history

import numpy as np

def process_trade(trade_list):
    with open('filename20.txt', 'w') as f:
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
            df = df.dropna()
            df['Signal'] = 0.0
            df['Signal'] = np.where(df['avgPrice20'] > df['avgPrice50'], 1.0, 0.0)
            df['Position'] = df['Signal'].diff()
            print(df)
            print('-----------------------------------------------')

trade_list =['JKPAPER','INGERRAND','VENKEYS','SCHNEIDER','RAYMOND','ASHOKA','DISHTV','HUHTAMAKI','BALMLAWRIE','SHOPERSTOP','HSCL','HAL','MAHSEAMLES','JTEKTINDIA','GRSE','RCF','GEPIL','IEX','TATAMOTORS','VEDL','FCONSUMER','DRREDDY','BLISSGVS','SCI','ACC','SAIL','CUB','MRF','STAR','PFC','KEC','SFL','NCC','TCS','KSB','IOB','RAIN','BSE','NH','ITI','LTI','IGL','SIS','HEG','BDL','PVR','MGL','KEI','EPL','BEL','UPL','MMTC','IDEA','LT']
process_trade(trade_list)
