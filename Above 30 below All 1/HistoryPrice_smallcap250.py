from datetime import date
import sys
import pandas as pd
from nsepy import get_history


def process_trade(trade_list):
    with open('smallcap250.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print('This message will be written to a file.')
        for trade in trade_list:
            data = get_history(symbol=trade, start=date(2020, 1, 1), end=date.today())
            df =""
            df = pd.DataFrame(data, columns=['Symbol', 'Series', 'Prev Close', 'Close', 'Volume'])
            df7 = pd.DataFrame(data, columns=['Close'])
            short_rolling3 = df7.rolling(window=3).mean()
            df['avgPrice3'] = short_rolling3
            short_rolling7 = df7.rolling(window=7).mean()
            df['avgPrice7'] = short_rolling7
            short_rolling30 = df7.rolling(window=30).mean()
            df['avgPrice30'] = short_rolling30
            short_rolling50 = df7.rolling(window=50).mean()
            df['avgPrice50'] = short_rolling50
            short_rolling200 = df7.rolling(window=200).mean()
            df['avgPrice200'] = short_rolling200

            ds = ""
            for i in df.index:
                if df.loc[i, 'avgPrice7'] >= df.loc[i, 'Close'] >= df.loc[i, 'avgPrice30'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice200'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice50']:

                    ls = str(i) + ": " + str(df.loc[i, 'Symbol']) \
                         + " Close: " + str(df.loc[i, 'Close']) \
                         + " avgPrice7 " + str(round(df.loc[i, 'avgPrice7'])) \
                         + " avgPrice30 " + str(round(df.loc[i, 'avgPrice30'])) \
                         + " avgPrice50 " + str(round(df.loc[i, 'avgPrice50'])) \
                         + " avgPrice200 " + str(round(df.loc[i, 'avgPrice200'])) \
                         + " Vol " + str(round(df.loc[i, 'Volume']))
                    ds = ds + ls + '\n'
                    ls = ''
            print(ds)
            # sys.stdout = original_std_out

        # Large Cap
trade_list = ['TATACOFFEE','IOB','TATAINVEST','GRAPHITE','CSBBANK','VMART','VTL','RITES','RHIM','ASTRAZEN','SOBHA','MMTC','IBREALEST','FINPIPE','CHAMBLFERT','INDOCO','ITI','SHYAMMETL','RALLIS','JMFINANCIL','MTARTECH','DBL','CHEMPLASTS','CASTROLIND','INFIBEAM','REDINGTON','NETWORK18','UCOBANK','DHANI','HINDCOPPER','SJVN','AMBER','BSE','ASAHIINDIA','LAXMIMACH','FACT','BIRLACORPN','JAMNAAUTO','AVANTIFEED','UFLEX','SPARC','KEI','TCIEXP','SHARDACROP','PVR','MAZDOCK','RCF','IDBI','MANAPPURAM','JUSTDIAL','BORORENEW','NAZARA','CUB','FDC','PCBL','IBULHSGFIN','CANFINHOME','KALYANKJIL','CGCL','BBTC','BDL','LATENTVIEW','FSL','SAPPHIRE','STLTECH','GRINFRA','HFCL','BCG','EPL','IDFC','GESHIP','INDIACEM','KARURVYSYA','METROPOLIS','SYMPHONY','GNFC','RAINBOW','POWERINDIA','HUDCO','HGS','RBLBANK','TV18BRDCST','HIKAL','PRIVISCL','VAIBHAVGBL','GRANULES','BASF','ZENSARTECH','TCNSBRANDS','IIFL','PPLPHARMA','INTELLECT','AARTIDRUGS','PNBHOUSING','DELTACORP','GODFRYPHLP','SUZLON','SHILPAMED','SONATSOFTW','EQUITASBNK']

process_trade(trade_list)
