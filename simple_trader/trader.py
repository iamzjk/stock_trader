#!/usr/bin/env python3.5
"""
	Trader Functions
"""

import pandas_datareader.data as web
import datetime


def read_data(symbol, start, end=None):
	"""
	Args:
		symbol (str): 'AAPL'
		start (str): 'YYYY-MM-DD'
		end (str): 'YYYY-MM-DD'

	Returns:
		dataframe
	"""

	start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
	today = datetime.datetime.today()
	end_date = datetime.datetime.strptime(end, '%Y-%m-%d') if end else today

	df_data = web.DataReader(symbol, 'google', start_date, end_date)

	return df_data


def find_events(df_data, lookback=20):
	"""
	Args:
		df_data (dataframe): output of read_data function
		lookback (int): how many days TAs look back

	Returns:
		dataframe
	"""

	df_data

if __name__ == '__main__':

	data = read_data('AAPL', '2017-05-01', '2017-06-01')
	print(data)