#!/usr/bin/env python3.5
"""
    Trader Functions
"""

import pandas_datareader.data as web
import datetime


def read_data(symbols, start, end=None):
    """
    Args:
        symbols (list or str): 'AAPL', ['AAPL', 'F']
        start (str): 'YYYY-MM-DD'
        end (str): 'YYYY-MM-DD'

    Returns:
        panel or dataframe
    """    

    start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
    today = datetime.datetime.today()
    end_date = datetime.datetime.strptime(end, '%Y-%m-%d') if end else today

    pf = web.DataReader(symbols, 'google', start_date, end_date)

    return pf


def find_events(pf, lookback=20):
    """
    Args:
        pf (panel): output of read_data function
        lookback (int): how many days TAs look back

    Returns:
        dataframe
    """

    df_close = pd['Close']
    df_ma = pd.rolling_mean(df_close, lookback)
    df_std = pd.rolling_std(df_close, lookback)
    df_bollingerbands = (df_close - df_ma) / df_std


if __name__ == '__main__':

    data = read_data('AAPL', '2017-05-01', '2017-06-01')
    print(data)