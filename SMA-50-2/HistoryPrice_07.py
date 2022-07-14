from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np

def process_trade(trade_list):
    with open('SMA2_filename07.txt', 'w') as f:
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


# Large Cap
trade_list = ['NRAIL',
              'FSC',
              'HITECHCORP',
              'ORIENTABRA',
              'RUBYMILLS',
              'SCHAND',
              'AKASH',
              'PENINLAND',
              'TALBROAUTO',
              'HARRMALAYA',
              'JAGSNPHARM',
              'ASHIMASYN',
              'TRIGYN',
              'KOTHARIPRO',
              'SPTL',
              'AYMSYNTEX',
              'ARIHANTSUP',
              'AGARIND',
              'MAXIND',
              'JBFIND',
              'AURIONPRO',
              'UCALFUEL',
              'NIPPOBATRY',
              'ONWARDTEC',
              'CONSOFINVT',
              'JPINFRATEC',
              'VASCONEQ',
              'PDMJEPAPER',
              'MCLEODRUSS',
              'GVKPIL',
              'AIRAN',
              'GOACARBON',
              'TVSELECT',
              'JINDRILL',
              'MAWANASUG',
              'NAHARINDUS',
              'ALANKIT',
              'CEBBCO',
              'SWELECTES',
              'CREST',
              'SHEMAROO',
              'PPAP',
              'DHUNINV',
              'GKWLIMITED',
              'BRFL',
              'SARLAPOLY',
              'PTL',
              'GULFPETRO',
              'ADSL',
              'DTIL',
              'PARACABLES',
              'KCPSUGIND',
              'BIRLACABLE',
              'GEECEE',
              'AXISCADES',
              'LASA',
              'INVENTURE',
              'BAFNAPH',
              'SILINV',
              'KMSUGAR',
              'CUPID',
              'KOTARISUG',
              'BIRLAMONEY',
              'RNAVAL',
              'UNIVPHOTO',
              'ADVANIHOTR',
              'SETCO',
              'GOKUL',
              'KRISHANA',
              'JAYSREETEA',
              'FCSSOFT',
              'BIL',
              'RAMANEWS',
              'NAHARCAP',
              'AKSHARCHEM',
              'VETO',
              'GENUSPAPER',
              'SDBL',
              'MARATHON',
              'MAHESHWARI',
              'HDIL',
              'SAKAR',
              'REFEX',
              'WALCHANNAG',
              'SPECIALITY',
              'SAKUMA',
              'MMP',
              'CHEMBOND',
              'PODDARMENT',
              'LINCPEN',
              'LIBERTSHOE',
              'SINTEX',
              'ALBERTDAVD',
              'AHLWEST',
              'WANBURY',
              'SIMPLEXINF',
              'LSIL',
              'PONNIERODE',
              'EIMCOELECO',
              'BRNL'
              ]

process_trade(trade_list)
