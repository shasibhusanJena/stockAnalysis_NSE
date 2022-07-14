from datetime import date
import sys
import pandas as pd
from nsepy import get_history
import numpy as np
def process_trade(trade_list):
    with open('SMA2_filename03.txt', 'w') as f:
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
trade_list = ['MUKANDLTD',
              'JMCPROJECT',
              'SHARDAMOTR',
              'KCP',
              'NUCLEUS',
              'KIRIINDUS',
              'GTPL',
              'ORISSAMINE',
              'CENTRUM',
              'ACCELYA',
              'TIMETECHNO',
              'GATI',
              'DBCORP',
              'ANANTRAJ',
              'HIMATSEIDE',
              'RAMCOSYS',
              'FORCEMOT',
              'GEOJITFSL',
              'INOXWIND',
              'GENUSPOWER',
              'RSYSTEMS',
              'DOLLAR',
              'BFUTILITIE',
              'TIPSINDLTD',
              'BOMDYEING',
              'WSTCSTPAPR',
              'ADFFOODS',
              'MMFL',
              'TVTODAY',
              'SASKEN',
              'CIGNITITEC',
              'GUFICBIO',
              'GABRIEL',
              'TEJASNET',
              'COSMOFILMS',
              'CONFIPET',
              'VSTTILLERS',
              'JAGRAN',
              'FMGOETZE',
              'DPSCLTD',
              'RAJRATAN',
              'QUICKHEAL',
              'KSL',
              'KIRLOSIND',
              'USHAMART',
              'NBVENTURES',
              'KOLTEPATIL',
              'VINDHYATEL',
              'APCOTEXIND',
              'PFOCUS',
              'JISLDVREQS',
              'JISLJALEQS',
              'ELECTCAST',
              'WELENT',
              'PUNJABCHEM',
              'OMAXE',
              'SUNDARMHLD',
              'DIAMONDYD',
              'IGARASHI',
              'PSPPROJECT',
              'HINDOILEXP',
              '3IINFOTECH',
              'TVSSRICHAK',
              'HSIL',
              'IMFA',
              'ARVINDFASN',
              'PANAMAPET',
              'JAYNECOIND',
              'EXCELINDUS',
              'MANINFRA',
              'GALLISPAT',
              'OPTIEMUS',
              'ITDCEM',
              'SAFARI',
              'KESORAMIND',
              'TIRUMALCHM',
              'JKIL',
              'SMSPHARMA',
              'ASTRAMICRO',
              'SSWL',
              'SANDHAR',
              'ELECON',
              'HBLPOWER',
              'ANDHRSUGAR',
              'FLFL',
              'CAPACITE',
              'VOLTAMP',
              'INDORAMA',
              'NACLIND',
              'TATAMTRDVR',
              'SIYSIL',
              'MANALIPETC',
              'INSECTICID',
              'SUNFLAG',
              'IFGLEXPOR',
              'WONDERLA',
              'ONMOBILE',
              'LGBBROSLTD',
              'LUMAXIND',
              'SHAKTIPUMP'
              ]

process_trade(trade_list)
