from datetime import date
import sys
import pandas as pd
from nsepy import get_history

def process_trade(trade_list):
    with open('filename19.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print('This message will be written to a file.')
        for trade in trade_list:
            data = get_history(symbol=trade, start=date(2017, 1, 1), end=date.today())
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
            ds =""
            for i in df.index:
                if df.loc[i, 'Close'] <= df.loc[i, 'avgPrice7'] and \
                        df.loc[i, 'Close'] >= df.loc[i, 'avgPrice30'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice180'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice45'] and \
                        df.loc[i, 'Close'] <= df.loc[i, 'avgPrice60']:
                    ls = "index: " + str(i) + " Symbol: " + str(df.loc[i, 'Symbol']) + " Close: " + str(
                        df.loc[i, 'Close']) + " avgPrice7 " + str(round(df.loc[i, 'avgPrice7'])) \
                         + " avgPrice30 " + str(round(df.loc[i, 'avgPrice30'])) + " avgPrice45 " + str(
                        round(df.loc[i, 'avgPrice45'])) + " avgPrice180 " + str(
                        round(df.loc[i, 'avgPrice180'])) + " avgPrice60 " + str(
                        round(df.loc[i, 'avgPrice60'])) + " Volume " + str(round(df.loc[i, 'Volume']))
                    ds = ds+ ls+'\n'
                    ls=''
            print(ds)
            #sys.stdout = original_std_out

trade_list =['BHARATRAS','BURGERKING','CERA','SWSOLAR','JKLAKSHMI','BEML','VSTIND','SPARC','KRBL','COCHINSHIP','JSL','VIPIND','ANGELBRKG','GPPL','MASFIN','HFCL','GODFRYPHLP','SUZLON','SOBHA','SUDARSCHEM','ECLERX','CAPLIPOINT','CSBBANK','KARURVYSYA','OIL','JSLHISAR','RESPONIND','ENGINERSIN','STARCEMENT','MAZDOCK','NETWORK18','MOIL','VALIANTORG','IRCON','GSFC','MAHSCOOTER','BAJAJCON','TASTYBITE','DELTACORP','MAHLOG','IFBIND','SPANDANA','HEMIPROP','WIPRO','KSCL','WELCORP','IOLCP','ORIENTREF','GAEL','SPICEJET','IRB','DHANUKA','MIDHANI','SUNTECK','TCIEXP','SHILPAMED','IBREALEST','NESCO','POLYPLEX','PHILIPCARB','GULFOILLUB','SUPRAJIT','ALEMBICLTD','INDOCO','VAIBHAVGBL','TRITURBINE','GUJALKALI','UFLEX','SWANENERGY','GREAVESCOT','NOCIL','TCNSBRANDS','INOXLEISUR','NILKAMAL','NFL','CCL','CHALET','JINDALSAW','JKTYRE','EQUITAS','DCAL','TATACOFFEE','JAMNAAUTO','ICIL','SHARDACROP','DCBBANK','LEMONTREE','MHRIL','MINDACORP','FRETAIL','UJJIVAN','LAOPALA']
process_trade(trade_list)
