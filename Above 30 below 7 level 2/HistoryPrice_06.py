from datetime import date
import sys
import pandas as pd
from nsepy import get_history


def process_trade(trade_list):
    with open('filename06.txt', 'w') as f:
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
            short_rolling30 = df7.rolling(window=30).mean()
            df['avgPrice30'] = short_rolling30
            short_rolling45 = df7.rolling(window=45).mean()
            df['avgPrice45'] = short_rolling45
            short_rolling60 = df7.rolling(window=60).mean()
            df['avgPrice60'] = short_rolling60
            short_rolling180 = df7.rolling(window=180).mean()
            df['avgPrice180'] = short_rolling180
            ds = ""
            for i in df.index:
                # if df.loc[i, 'avgPrice30'] <= df.loc[i, 'Close'] >= df.loc[i, 'avgPrice7'] >= df.loc[i, 'avgPrice3'] and \
                if df.loc[i, 'avgPrice7'] >= df.loc[i, 'Close'] >= df.loc[i, 'avgPrice30'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice180'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice45'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice180'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice60']:
                    ls = "index: " + str(i) + " Symbol: " + str(df.loc[i, 'Symbol']) + " Close: " + str(
                        df.loc[i, 'Close']) + " avgPrice7 " + str(round(df.loc[i, 'avgPrice7'])) \
                         + " avgPrice30 " + str(round(df.loc[i, 'avgPrice30'])) + " avgPrice45 " + str(
                        round(df.loc[i, 'avgPrice45'])) + " avgPrice180 " + str(
                        round(df.loc[i, 'avgPrice180'])) + " avgPrice60 " + str(
                        round(df.loc[i, 'avgPrice60'])) + " Volume " + str(round(df.loc[i, 'Volume']))
                    ds = ds + ls + '\n'
                    ls = ''
            print(ds)
            # sys.stdout = original_std_out


# Large Cap
trade_list = ['RUSHIL',
              'XELPMOC',
              'TI',
              'DYNPRO',
              'ARMANFIN',
              'DBREALTY',
              'STEELXIND',
              'TDPOWERSYS',
              'MUNJALSHOW',
              'SPAL',
              'SRHHYPOLTD',
              'SHREEPUSHK',
              'SHALPAINTS',
              'BLKASHYAP',
              'KHADIM',
              'HCL-INSYS',
              'IFBAGRO',
              'PROZONINTU',
              'SATIN',
              'GANDHITUBE',
              'ZOTA',
              'WATERBASE',
              'TBZ',
              'ROSSELLIND',
              'FEL',
              'FELDVR',
              'INDSWFTLAB',
              'NBIFIN',
              'GAYAPROJ',
              'THEINVEST',
              'JAIBALAJI',
              'HITECHGEAR',
              'VENUSREM',
              'ZEELEARN',
              'VISHWARAJ',
              'RML',
              'PARSVNATH',
              'GOKULAGRO',
              'RELCAPITAL',
              'MADRASFERT',
              'PRECWIRE',
              'DHFL',
              'HITECH',
              'RANASUG',
              'GANESHHOUC',
              'ANDHRACEMT',
              'HERCULES',
              'GENESYS',
              'JUBLINDS',
              'DLINKINDIA',
              'MIRCELECTR',
              'SANGAMIND',
              'PITTIENG',
              'TCPLPACK',
              'PGIL',
              'HPL',
              'GSCLCEMENT',
              'MAGADSUGAR',
              'HINDCOMPOS',
              'SHRIRAMEPC',
              'ORIENTBELL',
              'MAHEPC',
              'ORICONENT',
              'BGRENERGY',
              'BHARATWIRE',
              'GTL',
              'ARTEMISMED',
              'SREEL',
              'CYBERTECH',
              'NDTV',
              'PENIND',
              'DICIND',
              'HINDNATGLS',
              'REPRO',
              'SORILINFRA',
              'KAYA',
              'KAMDHENU',
              'ASAHISONG',
              'MENONBE',
              'MEP',
              'ISMTLTD',
              'DHANBANK',
              'ATULAUTO',
              'MANAKSIA',
              'PPL',
              'ZUARIGLOB',
              'KDDL',
              'TRIL',
              'MSPL',
              'URJA',
              'NAHARPOLY',
              '63MOONS',
              'SHREYAS',
              'VIPULLTD',
              'BIRLATYRE',
              'VARDHACRLC',
              'ARVSMART',
              'VISHAL',
              'V2RETAIL',
              'UGARSUGAR'
              ]

process_trade(trade_list)
