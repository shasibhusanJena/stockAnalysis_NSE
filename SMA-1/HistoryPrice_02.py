from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np

def process_trade(trade_list):
    with open('SMA2_filename02.txt', 'w') as f:
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
trade_list = ['RPOWER',
              'JKPAPER',
              'MARKSANS',
              'DALMIASUG',
              'GDL',
              'KIRLOSENG',
              'BORORENEW',
              'GET&D',
              'TATAMETALI',
              'MEGH',
              'RELIGARE',
              'ITDC',
              'TECHNOE',
              'HIL',
              'GREENLAM',
              'JPASSOCIAT',
              'MAHLIFE',
              'ICRA',
              'MAITHANALL',
              'MOREPENLAB',
              'TCI',
              'BEPL',
              'GREENPANEL',
              'PTC',
              'HGINFRA',
              'LAOPALA',
              'ORIENTCEM',
              'IFCI',
              'OAL',
              'ESABINDIA',
              'J&KBANK',
              'HCG',
              'NEULANDLAB',
              'SURYAROSNI',
              'GTLINFRA',
              'SOMANYCERA',
              'JAICORPLTD',
              'GHCL',
              'KENNAMET',
              'ASTEC',
              'BAJAJHIND',
              'INEOSSTYRO',
              'ACE',
              'SAGCEM',
              'DEN',
              'PDSMFL',
              'AHLUCONT',
              'DAAWAT',
              'PAISALO',
              'BOROLTD',
              'VRLLOG',
              'CAMLINFINE',
              'GREENPLY',
              'DHAMPURSUG',
              'PRICOLLTD',
              'SHK',
              'RAMCOIND',
              'THOMASCOOK',
              'PANACEABIO',
              'TINPLATE',
              'SHIL',
              'IIFLSEC',
              'MATRIMONY',
              'ARVIND',
              'UNICHEMLAB',
              'VESUVIUS',
              'EVEREADY',
              'SARDAEN',
              'REPCOHOME',
              'BANARISUG',
              'PURVA',
              'ATFL',
              'RKFORGE',
              'MAYURUNIQ',
              'HERITGFOOD',
              'HCC',
              'WABAG',
              'FILATEX',
              'SWARAJENG',
              'MSTCLTD',
              'CARERATING',
              'HESTERBIO',
              'SHALBY',
              'INDIAGLYCO',
              'RELINFRA',
              'PILANIINVS',
              'OLECTRA',
              'SUBROS',
              'CHENNPETRO',
              'SHRIPISTON',
              'JBMA',
              'GLOBUSSPR',
              'APARINDS',
              'AMRUTANJAN',
              'SOTL',
              'DFMFOODS',
              'AUTOAXLES',
              'NEOGEN',
              'IGPL'
              ]

process_trade(trade_list)
