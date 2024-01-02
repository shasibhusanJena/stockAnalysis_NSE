from datetime import date
import sys
import pandas as pd
from nsepy import get_history
from nsepy.history import get_indices_price_list



def process_trade(trade_list):
    with open('filename11.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print('This message will be written to a file.')
        for trade in trade_list:
            data = get_indices_price_list(date(2019, 1, 1))
            print(data)



# Large Cap
trade_list = ['POWERGRID', 'ITC']

process_trade(trade_list)
