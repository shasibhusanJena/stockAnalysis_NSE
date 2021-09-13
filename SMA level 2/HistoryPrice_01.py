from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np


def process_trade(trade_list):
    with open('filename01.txt', 'w') as f:
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
trade_list = ['BLUECHIP',
              'SPCENET',
              'HAVISHA',
              'SABEVENTS',
              'GISOLUTION',
              'INTEGRA',
              'NORBTEAEXP',
              '3PLAND',
              'ZEEMEDIA',
              'SANGHVIFOR',
              'S&SPOWER',
              'SUBCAPCITY',
              'MASKINVEST',
              'KALYANI',
              'WIPL',
              'BIOFILCHEM',
              'LFIC',
              'SHIVAMILLS',
              'NIRAJISPAT',
              'HISARMETAL',
              'SUJANAUNI',
              'PROSEED',
              'METKORE',
              'DIGJAMLTD',
              'VIKASMCORP',
              'PRABHAT',
              'ADHUNIKIND',
              'CNOVAPETRO',
              'HARITASEAT',
              'KSK',
              'PSL',
              'CIMMCO',
              'DEEPIND',
              'SUBEX',
              'AIONJSW',
              'FAIRCHEM',
              'STRTECH',
              'ESSELPACK',
              'SELMCL',
              'JAIHINDPRO',
              'IBVENTURES',
              'UVSL',
              'HEXAWARE',
              'INFRATEL',
              'PARABDRUGS',
              'PAPERPROD',
              'IBULISL',
              'LAKSHVILAS',
              '8KMILES',
              'RTNINFRA',
              'OMMETALS',
              'CESCVENT',
              'GTNIND',
              'GARDENSILK',
              'JUBILANT',
              'GLOBOFFS',
              'ADANIGAS',
              'ORTINLABSS',
              'SEZAL',
              'ADANIPOWER',
              'MFSL',
              'RUCHI',
              'ZEEL',
              'KIOCL',
              'MAGMA',
              'SHRIRAMCIT',
              'CGPOWER',
              'TTML',
              'TATASTLBSL',
              'BIRLACORPN',
              'RENUKA',
              'FACT',
              'DBL',
              'PSB',
              'VTL',
              'PRAJIND',
              'HIKAL',
              'SAREGAMA',
              'MASTEK',
              'JSWHL',
              'HGS',
              'NEWGEN',
              'TIDEWATER',
              'GPIL',
              'TRIVENI',
              'RTNPOWER',
              'HATHWAY',
              'DEEPAKFERT',
              'ADVENZYMES',
              'INDOSTAR',
              'TATASTLLP',
              'HNDFDS',
              'AGCNET',
              'JPPOWER',
              'HMT',
              'NIITLTD',
              'KIRLFER',
              'RUPA',
              'ALLCARGO',
              'JINDALPOLY',
              'KIRLOSBROS',
              ]

process_trade(trade_list)
