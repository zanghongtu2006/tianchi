#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: MarketData.py

@time: 7/2/18 8:56 PM

@desc:

"""


class MarketData:
    def __init__(self, security_id, ticker_symbol, end_date, close_price, turnover_vol, turnover_value, market_value,
                 type_id, type_name_en) -> None:
        self.security_id = security_id
        self.ticker_symbol = ticker_symbol
        self.end_date = end_date
        self.close_price = close_price
        self.turnover_vol = turnover_vol
        self.turnover_value = turnover_value
        self.market_value = market_value
        self.type_id = type_id
        self.type_name_en = type_name_en

    def __str__(self) -> str:
        return 'MarketData (security_id: %s, ticker_symbol: %s, end_date: %s, ' \
               'close_price: %s, turnover_value: %s, turnover_value: %s, ' \
               'market_value: %s, type_id:%s, type_name_en:%s)' % \
               (self.security_id, self.ticker_symbol, self.end_date,
                self.close_price, self.turnover_vol, self.turnover_value,
                self.market_value, self.type_id, self.type_name_en)


Market_Data_CN_EN_Mapping = {

}

Market_Data_EN_CN_Mapping = {

}
