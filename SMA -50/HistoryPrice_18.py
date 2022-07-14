from datetime import date
import sys
import pandas as pd
from nsepy import get_history

import numpy as np

def process_trade(trade_list):
    with open('SMA_filename18.txt', 'w') as f:
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

trade_list =['VTL','SEQUENT','NLCINDIA','REDINGTON','CANFINHOME','BSOFT','MAHINDCIE','ELGIEQUIP','ROSSARI','SUPPETRO','PRSMJOHNSN','BALRAMCHIN','AVANTIFEED','LAXMIMACH','WESTLIFE','SUNCLAYLTD','PRINCEPIPE','WOCKPHARMA','JCHAC','SONATSOFTW','PNBHOUSING','TV18BRDCST','ZENSARTECH','GMMPFAUDLR','RVNL','ORIENTELEC','VARROC','RITES','ICICIBANK','GNFC','TEAMLEASE','PNCINFRA','SOLARA','RALLIS','KALPATPOWR','EIHOTEL','KNRCON','GESHIP','THYROCARE','FDC','HEIDELBERG','GARFIBRES','FINCABLES','EDELWEISS','KPITTECH','JYOTHYLAB','BRIGADE','VMART','VAKRANGEE','TATAINVEST','INFIBEAM','CENTURYTEX','CEATLTD','INDIACEM','UJJIVANSFB','LUXIND','JUSTDIAL','ADVENZYMES']

process_trade(trade_list)
