#!/usr/bin/env python3
# -*- coding: utf-8; py-indent-offset:4 -*-

import logging
from datetime import datetime, timedelta


import dateutil.parser as dp
import numpy as np
import pandas as pd
import pandas_datareader
import pandas_datareader.data as web
import requests_cache
from ib_insync import IB, Stock
from pytz import timezone


from qa_dataprovider.generic_dataprovider import GenericDataProvider


class IBDataProvider(GenericDataProvider):

    CLIENT_ID = 0

    logging.basicConfig(level=logging.DEBUG, format='%(filename)s: %(message)s')
    logger = logging

    @staticmethod
    def get_unique_id():
        IBDataProvider.CLIENT_ID += 1
        return IBDataProvider.CLIENT_ID

    def __init__(self, host: str="127.0.0.1", port: int= 7496, timeout: int=10):
        self.client_id = IBDataProvider.get_unique_id()

        self.ib = IB()
        self.ib.connect(host, port, clientId=self.client_id, timeout=timeout)

    def _get_data_internal(self, ticker: str, from_date: str, to_date: str, timeframe: str) -> \
            pd.DataFrame:

        contract = Stock(ticker, 'SMART', 'USD')
        print("BEFORE")
        tmp = self.ib.reqHeadTimeStamp(contract, whatToShow='TRADES', useRTH=True)
        #bars = self.ib.reqHistoricalData(contract, endDateTime='', durationStr="1000 D",
        #                                 barSizeSetting='1 day', whatToShow="TRADES", useRTH=True)
        print("AFTER")
        print(tmp)
        #print(bars)
        return pd.DataFrame()

    def add_quotes(self, data, ticker):
        pass

    def _finish(self):
        self.ib.disconnect()

if __name__ == '__main__':
    ib = IBDataProvider()
    dailys = ib.get_data(['SPY'], '2010-01-01', '2016-12-31', max_workers=5, timeframe='week')
    print(dailys[0].tail())
    #print(dailys[1].tail())