#!/usr/bin/env python3
# -*- coding: utf-8; py-indent-offset:4 -*-

from qa_dataprovider.ib_dataprovider import IBDataProvider
from qa_dataprovider.csv_dataprovider import CsvFileDataProvider
from qa_dataprovider.web_dataprovider import CachedWebDataProvider

AVAILABLE_PROVIDERS = ['google', 'yahoo','stooq','ib','ig','sql','quandl','nasdaq','infront']


class Factory:

    @staticmethod
    def make_provider( provider, clear_cache=False, get_quotes=False, **kwargs):
        if provider == 'ib':
            return IBDataProvider(expire_days=0, clear_cache=clear_cache)

        elif provider == 'quandl':
            return CsvFileDataProvider(
                [
                    '../../quandl/iwm',
                    '../quandl/iwm',
                    '../../quandl/spy',
                    '../quandl/spy',
                    '../../quandl/ndx',
                    '../quandl/ndx'
                ])

        elif provider == 'infront':
            return CsvFileDataProvider(
                [
                    '../../infront',
                    '../infront'
                ],
                prefix=['NSQ', 'NYS', 'NYSF', 'SSE', ''] if kwargs.get('prefix') is None else kwargs.get('prefix')
            )

        elif provider == 'nasdaq':
            return CsvFileDataProvider(
                [
                    '../../nasdaq',
                    '../infront'
                ])

        elif provider == 'stooq':
            return CsvFileDataProvider(
                [
                    '../../stooq',
                    '../stooq'
                ])

        elif provider == 'sql':
            raise Exception("Not implemented yet")

        elif provider == 'ig':
            raise Exception("Not implemented yet")

        else:
            return CachedWebDataProvider(provider, expire_days=0, get_quotes=get_quotes)

