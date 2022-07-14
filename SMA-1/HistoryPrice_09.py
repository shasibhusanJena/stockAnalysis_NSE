from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np

def process_trade(trade_list):
    with open('SMA2_filename09.txt', 'w') as f:
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
trade_list = ['JMTAUTOLTD',
'EMAMIREAL',
'UNITEDTEA',
'PIONDIST',
'CLEDUCATE',
'LOVABLE',
'ALMONDZ',
'UMANGDAIRY',
'ASIANHOTNR',
'JOCIL',
'ARIES',
'NDGL',
'SUNDRMBRAK',
'LYKALABS',
'LGBFORGE',
'SUPERHOUSE',
'SEYAIND',
'PRAXIS',
'MACPOWER',
'SHREYANIND',
'REMSONSIND',
'RPPINFRA',
'TEXMOPIPES',
'ISFT',
'MANAKSTEEL',
'ROLTA',
'JHS',
'GROBTEA',
'PREMIERPOL',
'TRF',
'IITL',
'MAHAPEXLTD',
'SIGIND',
'ASPINWALL',
'INTENTECH',
'BHAGYANGR',
'JMA',
'PIONEEREMB',
'AUTOIND',
'SIMBHALS',
'DSSL',
'VIKASECO',
'MURUDCERA',
'ATLANTA',
'OPTOCIRCUI',
'BIGBLOC',
'BALPHARMA',
'VIKASPROP',
'TCIDEVELOP',
'VIPCLOTHNG',
'KANANIIND',
'AMJLAND',
'TTL',
'SHRENIK',
'ANSALAPI',
'CINELINE',
'OMAXAUTO',
'MAHASTEEL',
'WORTH',
'VIKASWSP',
'IVP',
'GRPLTD',
'PRAENG',
'NOIDATOLL',
'IL&FSTRANS',
'SITINET',
'SPLIL',
'INDOSOLAR',
'KECL',
'MANAKALUCO',
'PALREDTEC',
'BYKE',
'GILLANDERS',
'SOUTHWEST',
'DAMODARIND',
'KAMATHOTEL',
'ASAL',
'MIC',
'COMPUSOFT',
'DGCONTENT',
'PODDARHOUS',
'VISASTEEL',
'GSS',
'IZMO',
'A2ZINFRA',
'AUSOMENT',
'BEDMUTHA',
'CCHHL',
'ALPA',
'FMNL',
'SMARTLINK',
'SURANAT&P',
'JUMPNET',
'DHARSUGAR',
'KERNEX',
'SIL',
'AARVI',
'PKTEA',
'LOTUSEYE',
'SURYALAXMI'
]

process_trade(trade_list)
