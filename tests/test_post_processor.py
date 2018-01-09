#!/usr/bin/env python3
# -*- coding: utf-8; py-indent-offset:4 -*-

import unittest

from qa_dataprovider.csv_dataprovider import CsvFileDataProvider
import pandas as pd


class TestPostProcessor(unittest.TestCase):


    def test_filter_rth(self):
        provider = CsvFileDataProvider(["data"])

        df = provider.get_data(['AAPL_2017-11-03'], '2017-10-10', '2017-10-31', timeframe='5min', transform='5min', rth=True)[0]

        assert len(df.at_time('09:25:00')) == 0
        assert len(df.at_time('09:30:00')) > 0
        assert len(df.at_time('16:05:00')) == 0


    def test_resample_timeframe(self):
        provider = CsvFileDataProvider(["data"])
        df_list = provider.get_data(['AAPL_2018-01-06'], '2017-12-10', '2017-12-31', timeframe='5min', transform='1h', rth=True)
        df = df_list[0]

        # Assert 2017-12-29 09:30: O=170.71, H=170.71, L=169.71, C=169.93
        assert df.ix['2017-12-29 09:00:00']['Open'] == 170.71
        assert df.ix['2017-12-29 09:00:00']['High'] == 170.71
        assert df.ix['2017-12-29 09:00:00']['Low'] == 169.71
        assert df.ix['2017-12-29 09:00:00']['Close'] == 169.93

        # Assert 2017-12-29 10:00: O=169.92, H=169.95, L=169.31, C=169.64
        assert df.ix['2017-12-29 10:00:00']['Open'] == 169.92
        assert df.ix['2017-12-29 10:00:00']['High'] == 169.95
        assert df.ix['2017-12-29 10:00:00']['Low'] == 169.31
        assert df.ix['2017-12-29 10:00:00']['Close'] == 169.64

        # Assert 2017-12-29 16:00: O=169.23
        assert df.ix['2017-12-29 16:00:00']['Open'] == 169.23


if __name__ == '__main__':
    unittest.main()