from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np

def process_trade(trade_list):
    with open('SMA2_filename06.txt', 'w') as f:
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
