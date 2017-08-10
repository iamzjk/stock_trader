#!/usr/bin/env python3.5
"""
    Trader Functions
"""

import datetime

import pandas as pd
import pandas_datareader.data as web

from populate_sp500_tickers import read_sp500_tickers_from_mongo


def read_data(tickers, start, end):
    """
    Args:
        tickers (list or str): 'AAPL', ['AAPL', 'F']
        start (str): 'YYYY-MM-DD'
        end (str): 'YYYY-MM-DD'

    Returns:
        panel or dataframe
    """

    start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(end, '%Y-%m-%d')

    pf = web.DataReader(tickers, 'google', start_date, end_date)

    return pf


def find_events(pf, lookback=20):
    """
    Create an event study with the signal being:
    Bollinger value for the equity today <= -2.0
    Bollinger value for the equity yesterday >= -2.0
    Bollinger value for SPY today >= 1.0 or 1.2

    Args:
        pf (panel): output of read_data function
        lookback (int): how many days TAs look back

    Returns:
        dataframe
    """

    df_close = pf['Close']
    df_ma = pd.rolling_mean(df_close, lookback)
    df_std = pd.rolling_std(df_close, lookback)
    df_bollingerbands = (df_close - df_ma) / df_std


if __name__ == '__main__':

    today = str(datetime.date.today())
    tickers = read_sp500_tickers_from_mongo(today)
    pf = read_data(tickers + ['SPY'], '2017-05-01', today)
    pass
