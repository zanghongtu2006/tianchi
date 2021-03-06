#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: MacroIndustry.py

@time: 7/2/18 8:29 PM

@desc:

"""
import xlrd

from yuce.data.company_operating.model.orig.MacroIndustry import IndicInfo, IndicData
from yuce.data.constraint.Const import Const


def read_excel():
    workbook = xlrd.open_workbook(Const.file_new_macro_inststry_20180613)
    print(workbook.sheet_names())
    indic_info_sheet = workbook.sheet_by_name('INDIC_INFO')
    indic_info_lst = []
    for row in range(indic_info_sheet.nrows):
        if row == 0:
            continue
        row_data = indic_info_sheet.row(row)
        indic_info = IndicInfo(row_data[0], row_data[1], row_data[2], row_data[3], row_data[4])
        indic_info_lst.append(indic_info)

    indic_data_sheet = workbook.sheet_by_name('INDIC_DATA')
    indic_data_lst = []
    for row in range(indic_data_sheet.nrows):
        if row == 0:
            continue
        row_data = indic_data_sheet.row(row)
        indic_data = IndicData(row_data[0], row_data[1], row_data[2], row_data[3], row_data[4])
        indic_data_lst.append(indic_data)

    return indic_info_lst, indic_data_lst


if __name__ == '__main__':
    info_list, data_list = read_excel()
    for data in info_list:
        print(data)
