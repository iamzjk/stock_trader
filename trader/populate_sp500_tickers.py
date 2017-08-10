#!/usr/bin/env python3.5
"""
    Purpose:
        Scrape SP500 stock symbols and sectors from wikipedia
        (http://en.wikipedia.org/wiki/List_of_S%26P_500_companies),
        and store to mongo (stock.sp500)
"""

import logging
import urllib.request
import datetime
from collections import OrderedDict

from pymongo import MongoClient
from bs4 import BeautifulSoup

from config import Config


def populate_sp500():
    sp500 = scrape_list()
    store_sp500_symbols_to_mongo(sp500)


def scrape_list():
    url = "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=hdr)
    page = urllib.request.urlopen(req)
    soup = BeautifulSoup(page, 'lxml')

    table = soup.find('table', {'class': 'wikitable sortable'})
    rows = table.findAll('tr')

    report_date = int(str(datetime.date.today()).replace('-', ''))

    header = [
        'ticker', 'security', 'sec_filings', 'sector', 'sub_industry',
        'address', 'first_added_date', 'cik'
    ]

    sp500 = []
    for row in rows:

        col = row.findAll('td')
        if len(col) > 0:
            values = [
                None if value.string is None
                else value.string.strip() for value in col
            ]
            stock = OrderedDict(zip(header, values))
            del stock['sec_filings']
            stock['report_date'] = report_date
            sp500.append(stock)

    return sp500


def store_sp500_symbols_to_mongo(sp500):
    client = MongoClient(Config.MONGO_MLAB_URI)
    db = client.stock_trader

    report_date = sp500[0]['report_date']
    db.sp500.delete_many({'report_date': report_date})
    db.sp500.insert_many(sp500)


def read_sp500_tickers_from_mongo(report_date):
    """

    Args:
        report_date: YYYY-MM-DD
    """
    client = MongoClient(Config.MONGO_MLAB_URI)
    db = client.stock_trader

    report_date = int(report_date.replace('-', ''))
    data = db.sp500.find(
        {'report_date': report_date},
        {'ticker': 1, '_id': 0}
    )

    return [item['ticker'] for item in list(data)]


if __name__ == '__main__':
    try:
        populate_sp500()
    except Exception as err:
        logging.error(err, exc_info=True)
