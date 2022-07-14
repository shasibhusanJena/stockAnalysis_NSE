from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np
def process_trade(trade_list):
    with open('SMA2_filename04.txt', 'w') as f:
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
trade_list = ['MOLDTKPAC',
              'SADBHAV',
              'BFINVEST',
              'NRBBEARING',
              'DWARKESH',
              'WHEELS',
              'CLNINDIA',
              'SANGHIIND',
              'JINDWORLD',
              'GOCLCORP',
              'ASHIANA',
              'APOLLOPIPE',
              'BLS',
              'PRAKASH',
              'PNBGILTS',
              'DOLAT',
              'MTNL',
              'TIIL',
              'ASHAPURMIN',
              'RAMKY',
              'BUTTERFLY',
              'BODALCHEM',
              'KINGFA',
              'PARAGMILK',
              'BCG',
              '5PAISA',
              'GIPCL',
              'PCJEWELLER',
              'SESHAPAPER',
              'PFS',
              'VIDHIING',
              'APEX',
              'HONDAPOWER',
              'JETAIRWAYS',
              'VISAKAIND',
              'SHREDIGCEM',
              'SEAMECLTD',
              'SADBHIN',
              'POWERMECH',
              'NXTDIGITAL',
              'BHAGERIA',
              'THANGAMAYL',
              'RIIL',
              'SUVEN',
              'AVTNPL',
              'ESTER',
              'GANECOS',
              'BANCOINDIA',
              'DIGISPICE',
              'GMBREW',
              'GOLDIAM',
              'INDIANHUME',
              'DREDGECORP',
              'SHANTIGEAR',
              'DATAMATICS',
              'EIHAHOTELS',
              'TNPL',
              'KKCL',
              'MPSLTD',
              'TNPETRO',
              'SPIC',
              'KARDA',
              'DCW',
              'ALICON',
              'LUMAXTECH',
              'TTKHLTCARE',
              'POKARNA',
              'OCCL',
              'AARTISURF',
              'ANDHRAPAP',
              'AJMERA',
              'MAXVIL',
              'EKC',
              'SASTASUNDR',
              'RGL',
              'SRIPIPES',
              'KOPRAN',
              'SHANKARA',
              'VSSL',
              'FIEMIND',
              'MANGCHEFER',
              'NECLIFE',
              'APTECHT',
              'GULPOLY',
              'NCLIND',
              'MANGLMCEM',
              'INFOBEAN',
              'GNA',
              'SATIA',
              'FCL',
              'UTTAMSUGAR',
              'APCL',
              'GICHSGFIN',
              'FOSECOIND',
              'IMPAL',
              'GRAVITA',
              'TAKE',
              'EMAMIPAP',
              'AVADHSUGAR',
              'NAHARSPING'
              ]

process_trade(trade_list)
