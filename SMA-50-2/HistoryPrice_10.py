from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np
def process_trade(trade_list):
    with open('SMA2_filename10.txt', 'w') as f:
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
trade_list = ['LPDC',
              'AROGRANITE',
              'CINEVISTA',
              'LAMBODHARA',
              'TOKYOPLAST',
              'LIBAS',
              'PANACHE',
              'SAGARDEEP',
              'BHAGYAPROP',
              'INDBANK',
              'RAJSREESUG',
              'JYOTISTRUC',
              'INDIANCARD',
              'BHARATGEAR',
              'WEIZMANIND',
              'GEEKAYWIRE',
              'ONEPOINT',
              'SICAGEN',
              'RSSOFTWARE',
              'SUNDARAM',
              'MANAKCOAT',
              'KAPSTON',
              'GOLDENTOBC',
              'SALONA',
              'SICAL',
              'TOUCHWOOD',
              'NILASPACES',
              'MCDHOLDING',
              'SUMEETINDS',
              'GANGESSECU',
              'CORDSCABLE',
              'MUKTAARTS',
              'MOTOGENFIN',
              'CMICABLES',
              'TARMAT',
              'CTE',
              'PUNJLLOYD',
              'IL&FSENGG',
              'STEELCITY',
              'ABMINTLTD',
              'CENTEXT',
              'SHREERAMA',
              'SAMBHAAV',
              'ORIENTLTD',
              'KALYANIFRG',
              'PALASHSECU',
              'LOKESHMACH',
              'BAGFILMS',
              'ARCHIES',
              'DCM',
              'ROLLT',
              'JINDALPHOT',
              'TAINWALCHM',
              'MTEDUCARE',
              'INDOWIND',
              'NECCLTD',
              'MORARJEE',
              'TREJHARA',
              'IMAGICAA',
              'PRESSMN',
              'TERASOFT',
              'TOTAL',
              'ALKALI',
              'ANIKINDS',
              'ARCHIDPLY',
              'ARSSINFRA',
              'SKIL',
              'GLOBALVECT',
              'PATINTLOG',
              'FLEXITUFF',
              'UNIPLY',
              'MRO-TEK',
              'HOVS',
              'SOMICONVEY',
              'UNIVASTU',
              'SANWARIA',
              'PNC',
              'MEGASOFT',
              'SURANASOL',
              'SALSTEEL',
              'AMDIND',
              'MERCATOR',
              'UJAAS',
              'UTTAMSTL',
              'DELTAMAGNT',
              'ENERGYDEV',
              'BHANDARI',
              'BSL',
              'MALUPAPER',
              'KRIDHANINF',
              'BANG',
              'JITFINFRA',
              'TREEHOUSE',
              'INDOTHAI',
              'BVCL',
              'DBSTOCKBRO',
              'KWALITY',
              'AARVEEDEN',
              'VARDMNPOLY',
              'ANSALHSG']

process_trade(trade_list)
