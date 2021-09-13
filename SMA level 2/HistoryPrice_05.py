from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np

def process_trade(trade_list):
    with open('filename05.txt', 'w') as f:
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
trade_list = ['DYNAMATECH',
              'ADORWELD',
              'SUTLEJTEX',
              'SALASAR',
              'RANEHOLDIN',
              'XCHANGING',
              'NAGAFERT',
              'JAYBARMARU',
              'SIRCA',
              'DVL',
              'RCOM',
              'UNIENTER',
              'SANGHVIMOV',
              'TEXRAIL',
              'KICL',
              'RADIOCITY',
              'ASALCBR',
              'CENTENKA',
              'NSIL',
              'PGEL',
              'SKIPPER',
              'SNOWMAN',
              'NELCO',
              'DECCANCE',
              'ARSHIYA',
              'ENIL',
              'EXPLEOSOL',
              'ANUP',
              'TAJGVK',
              'INDNIPPON',
              'WENDT',
              'PATELENG',
              'TEXINFRA',
              'TWL',
              'VHL',
              'NITINSPIN',
              'HEXATRADEX',
              'BINDALAGRO',
              'PRECAM',
              'GFLLIMITED',
              'INDRAMEDCO',
              'SPENCERS',
              'VLSFINANCE',
              'ZENTEC',
              'BBL',
              'VADILALIND',
              'KOKUYOCMLN',
              'RPGLIFE',
              'NATHBIOGEN',
              'EBIXFOREX',
              'KITEX',
              'SMLISUZU',
              'SUMMITSEC',
              'MONTECARLO',
              'VISHNU',
              'RBL',
              'GOKEX',
              'KANORICHEM',
              'PLASTIBLEN',
              'MUTHOOTCAP',
              'STERTOOLS',
              'JASH',
              'ORIENTHOT',
              'AMBIKCO',
              'STCINDIA',
              'CANTABIL',
              'LINCOLN',
              'THEMISMED',
              'UNIVCABLES',
              'BALAJITELE',
              'RSWM',
              'KELLTONTEC',
              'HMVL',
              'KABRAEXTRU',
              'MUNJALAU',
              'ALLSEC',
              'MIRZAINT',
              'CEREBRAINT',
              'HLVLTD',
              'SREINFRA',
              'SAKSOFT',
              'UNITECH',
              'NELCAST',
              'RICOAUTO',
              'MANINDS',
              'JAYAGROGN',
              'HTMEDIA',
              'KUANTUM',
              'ORIENTPPR',
              'ASIANTILES',
              'GALLANTT',
              'BALAXI',
              'ZUARI',
              'CENTUM',
              'SANDESH',
              'EVERESTIND',
              'NAVKARCORP',
              'CONTROLPR',
              'VIMTALABS',
              'TFCILTD'
              ]

process_trade(trade_list)
