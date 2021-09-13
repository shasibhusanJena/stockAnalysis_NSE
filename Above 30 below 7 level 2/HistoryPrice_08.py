from datetime import date
import sys
import pandas as pd
from nsepy import get_history


def process_trade(trade_list):
    with open('filename08.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print('This message will be written to a file.')
        for trade in trade_list:
            data = get_history(symbol=trade, start=date(2018, 1, 1), end=date.today())
            df = pd.DataFrame(data, columns=['Symbol', 'Series', 'Prev Close', 'Close', 'Volume'])
            df7 = pd.DataFrame(data, columns=['Close'])
            short_rolling3 = df7.rolling(window=3).mean()
            df['avgPrice3'] = short_rolling3
            short_rolling7 = df7.rolling(window=7).mean()
            df['avgPrice7'] = short_rolling7
            short_rolling30 = df7.rolling(window=30).mean()
            df['avgPrice30'] = short_rolling30
            short_rolling45 = df7.rolling(window=45).mean()
            df['avgPrice45'] = short_rolling45
            short_rolling60 = df7.rolling(window=60).mean()
            df['avgPrice60'] = short_rolling60
            short_rolling180 = df7.rolling(window=180).mean()
            df['avgPrice180'] = short_rolling180
            ds = ""
            for i in df.index:
                # if df.loc[i, 'avgPrice30'] <= df.loc[i, 'Close'] >= df.loc[i, 'avgPrice7'] >= df.loc[i, 'avgPrice3'] and \
                if df.loc[i, 'avgPrice7'] >= df.loc[i, 'Close'] >= df.loc[i, 'avgPrice30'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice180'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice45'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice180'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice60']:
                    ls = "index: " + str(i) + " Symbol: " + str(df.loc[i, 'Symbol']) + " Close: " + str(
                        df.loc[i, 'Close']) + " avgPrice7 " + str(round(df.loc[i, 'avgPrice7'])) \
                         + " avgPrice30 " + str(round(df.loc[i, 'avgPrice30'])) + " avgPrice45 " + str(
                        round(df.loc[i, 'avgPrice45'])) + " avgPrice180 " + str(
                        round(df.loc[i, 'avgPrice180'])) + " avgPrice60 " + str(
                        round(df.loc[i, 'avgPrice60'])) + " Volume " + str(round(df.loc[i, 'Volume']))
                    ds = ds + ls + '\n'
                    ls = ''
            print(ds)
            # sys.stdout = original_std_out


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
