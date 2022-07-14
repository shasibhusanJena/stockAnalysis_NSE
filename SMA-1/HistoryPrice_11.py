from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np
def process_trade(trade_list):
    with open('SMA2_filename11.txt', 'w') as f:
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
trade_list = ['SUPERSPIN',
              'KEYFINSERV',
              'MADHAV',
              'MADHUCON',
              'BLBLIMITED',
              'NIBL',
              'ZENITHEXPO',
              'SUPREMEINF',
              'TIMESGTY',
              'MANUGRAPH',
              'CELEBRITY',
              'NITINFIRE',
              'CUBEXTUB',
              'VAISHALI',
              'SPMLINFRA',
              'OILCOUNTUB',
              'SANGINITA',
              'GAL',
              'EDUCOMP',
              'SUMIT',
              'GUJRAFFIA',
              'GOENKA',
              'SGL',
              'NEXTMEDIA',
              'VASWANI',
              'BEARDSELL',
              'TMRVL',
              'JPOLYINVST',
              'BANARBEADS',
              'ROHITFERRO',
              'TNTELE',
              'TIRUPATIFL',
              'NAGREEKEXP',
              'EXCEL',
              'DNAMEDIA',
              'COX&KINGS',
              'ORIENTALTL',
              'KSERASERA',
              'EASTSILK',
              'VIVIDHA',
              'METALFORGE',
              'AGROPHOS',
              'RKDL',
              'KGL',
              'MAGNUM',
              'MOHITIND',
              'MUKANDENGG',
              'SEPOWER',
              'PEARLPOLY',
              'SHAHALLOYS',
              'TIJARIA',
              'TGBHOTELS',
              'OISL',
              'KOHINOOR',
              'PRAKASHSTL',
              'AGRITECH',
              'MANGTIMBER',
              'GOLDTECH',
              'ADROITINFO',
              '21STCENMGM',
              'ANKITMETAL',
              'INDSWFTLTD',
              'BURNPUR',
              'ARIHANT',
              'DIAPOWER',
              'SPYL',
              'RMCL',
              'SETUINFRA',
              'COUNCODOS',
              'BCP',
              'GAYAHWS',
              'ATLASCYCLE',
              'SOMATEX',
              'PATSPINLTD',
              'SILLYMONKS',
              'WILLAMAGOR',
              'TANTIACONS',
              'KARMAENG',
              'INFOMEDIA',
              'JIYAECO',
              'BALKRISHNA',
              'SHIRPUR-G',
              'AUTOLITIND',
              'NATNLSTEEL',
              'CALSOFT',
              'KHANDSE',
              'OMKARCHEM',
              'ARCOTECH',
              'ZODJRDMKJ',
              'SHYAMTEL',
              'LYPSAGEMS',
              'SCAPDVR',
              'VICEROY',
              'NKIND',
              'CASTEXTECH',
              'SYNCOM',
              'HBSL',
              'MOHOTAIND',
              'EMCO',
              'WSI']

process_trade(trade_list)
