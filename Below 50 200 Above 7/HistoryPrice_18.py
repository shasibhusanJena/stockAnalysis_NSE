from datetime import date
import sys
import pandas as pd
import stockname as st
from nsepy import get_history


def process_trade(trade_list):
    with open('filename018.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print('This message will be written to a file.')
        for trade in trade_list:
            data = get_history(symbol=trade, start=date(2019, 1, 1), end=date.today())
            df = pd.DataFrame(data, columns=['Symbol', 'Series', 'Prev Close', 'Close', 'Volume'])
            df7 = pd.DataFrame(data, columns=['Close'])
            short_rolling3 = df7.rolling(window=3).mean()
            df['avgPrice3'] = short_rolling3
            short_rolling7 = df7.rolling(window=7).mean()
            df['avgPrice7'] = short_rolling7
            short_rolling50 = df7.rolling(window=50).mean()
            df['avgPrice50'] = short_rolling50
            short_rolling200 = df7.rolling(window=200).mean()
            df['avgPrice200'] = short_rolling200
            ds = ""
            for i in df.index:
                if df.loc[i, 'avgPrice7'] >= df.loc[i, 'Close'] <= df.loc[i, 'avgPrice50'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice200']:
                    ls = "index: " + str(i) + " Symbol: " \
                         + str(df.loc[i, 'Symbol']) \
                         + " Close: " + str(df.loc[i, 'Close']) \
                         + " avgPrice7 " + str(round(df.loc[i, 'avgPrice7'])) \
                         + " avgPrice50 " + str(round(df.loc[i, 'avgPrice50'])) \
                         + " avgPrice200 " + str(round(df.loc[i, 'avgPrice200'])) \
                         + " Volume " + str(round(df.loc[i, 'Volume']))
                    ds = ds + ls + '\n'
                    ls = ''
            print(ds)
            # sys.stdout = original_std_out


trade_list = st.filename018
process_trade(trade_list)
