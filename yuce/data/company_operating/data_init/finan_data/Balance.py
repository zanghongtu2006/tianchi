#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: Balance.py

@time: 7/2/18 9:20 PM

@desc:

"""
import xlrd

from yuce.data.constraint.Const import Const


def read_excel():
    workbook = xlrd.open_workbook(Const.file_finan_balance)
    print(workbook.sheet_names())
    market_data_sheet = workbook.sheet_by_name('General Business')
    print(market_data_sheet.nrows, market_data_sheet.ncols)
    # market_data_lst = []
    # for row in range(market_data_sheet.nrows):
    #     if row == 0:
    #         continue
    #     row_data = market_data_sheet.row(row)
    #     market_data = MarketData(row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5],
    #                              row_data[6], row_data[7], row_data[8])
    #     market_data_lst.append(market_data)

    return market_data_lst


if __name__ == '__main__':
    market_data_lst = read_excel()
    for data in market_data_lst:
        print(data)
