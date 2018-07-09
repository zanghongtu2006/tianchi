#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: Income.py

@time: 7/7/18 7:00 PM

@desc:

"""
from yuce.data.company_operating.util import DateUtil

"""
营收: REVENUE
编号: TICKET_SYMBOL.EXCHANGE_CD
帐期: END_DATE(转数字), 按照END_DATE_REP时间去重,取END_DATE_REP大的那个
"""


class Income:
    def __init__(self, revenue, code, end_date, publish_date, report_type) -> None:
        self.revenue = revenue
        self.code = code
        self.end_date = end_date
        self.publish_date = publish_date
        self.report_type = report_type

    def __str__(self) -> str:
        return 'Income(revenue: %s, ' \
               'code: %s, ' \
               'report_type: %s, ' \
               'publish_date: %s, ' \
               'end_date: %s.)' % \
               (self.revenue, self.code, self.report_type,
                DateUtil.num2day(self.publish_date), DateUtil.num2day(self.end_date))
