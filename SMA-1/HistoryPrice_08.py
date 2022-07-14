from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np

def process_trade(trade_list):
    with open('SMA2_filename08.txt', 'w') as f:
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
trade_list = ['GINNIFILA',
              'EROSMEDIA',
              'VINYLINDIA',
              'BANSWRAS',
              'RAJTV',
              'ASTRON',
              'NILAINFRA',
              'GUJAPOLLO',
              'PRECOT',
              'UFO',
              'ZODIACLOTH',
              'DCMNVL',
              'RHFL',
              'MANGALAM',
              'SALZERELEC',
              'MAZDA',
              'RAMASTEEL',
              'GOODLUCK',
              'HIRECT',
              'MOLDTECH',
              'ABAN',
              'SAKHTISUG',
              'MBAPL',
              'MAJESCO',
              'INDOTECH',
              'KOTHARIPET',
              'MBLINFRA',
              'KREBSBIO',
              'CAREERP',
              'DPWIRES',
              'WINDMACHIN',
              'DUCON',
              'SELAN',
              'GPTINFRA',
              'STARPAPER',
              'BASML',
              'SHIVAMAUTO',
              'KILITCH',
              'DONEAR',
              'WEBELSOLAR',
              'ROHLTD',
              'SHIVATEX',
              'NDL',
              'GAMMNINFRA',
              'VIDEOIND',
              'INSPIRISYS',
              'SKMEGGPROD',
              'APOLLO',
              'ESSARSHPNG',
              'MCL',
              'CHEMFAB',
              'VIVIMEDLAB',
              'SMSLIFE',
              'OSWALAGRO',
              'EMKAY',
              'ARROWGREEN',
              'MAANALU',
              'SHYAMCENT',
              'MBECL',
              'RUCHIRA',
              '20MICRONS',
              'DENORA',
              'REVATHI',
              'BROOKS',
              'ELECTHERM',
              'BALLARPUR',
              'APOLSINHOT',
              'NDRAUTO',
              'XPROINDIA',
              'CREATIVE',
              'GREENPOWER',
              'RANEENGINE',
              'ALPHAGEO',
              'NITCO',
              'AHLEAST',
              'MARALOVER',
              'PILITA',
              'KAKATCEM',
              'COMPINFO',
              'STEL',
              'IVC',
              'VERTOZ',
              'PREMEXPLN',
              'HUBTOWN',
              'HINDMOTORS',
              'ELGIRUBCO',
              'TPLPLASTEH',
              'MODIRUBBER',
              'ORBTEXP',
              'EMMBI',
              'CORALFINAC',
              'PRIMESECU',
              'WELINV',
              'BPL',
              'MINDTECK',
              'CAPTRUST',
              'AKSHOPTFBR',
              'TIL',
              'RUCHINFRA',
              'INDTERRAIN'
              ]

process_trade(trade_list)
