#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: CashFlowStatement.py

@time: 7/3/18 7:47 PM

@desc:

"""
import xlrd

from yuce.data.company_operating.model.orig.finan_data.CashFlowStatement import GeneralBusiness, Bank, Insurance, Securities
from yuce.data.constraint.Const import Const


def read_excel():
    workbook = xlrd.open_workbook(Const.file_finan_cash_flow_statement)
    print(workbook.sheet_names())
    general_business_sheet = workbook.sheet_by_name('General Business')
    bank_sheet = workbook.sheet_by_name('Bank')
    insurance_sheet = workbook.sheet_by_name('Insurance')
    securities_sheet = workbook.sheet_by_name('Securities')
    general_business_lst = []
    bank_lst = []
    insurance_lst = []
    securities_lst = []

    for row in range(1, general_business_sheet.nrows):
        row_data = general_business_sheet.row(row)
        general_business_lst.append(GeneralBusiness(row_data))

    for row in range(1, bank_sheet.nrows):
        row_data = bank_sheet.row(row)
        bank_lst.append(Bank(row_data))

    for row in range(1, insurance_sheet.nrows):
        row_data = insurance_sheet.row(row)
        insurance_lst.append(Insurance(row_data))

    for row in range(1, securities_sheet.nrows):
        row_data = securities_sheet.row(row)
        securities_lst.append(Securities(row_data))

    return general_business_lst, bank_lst, insurance_lst, securities_lst


if __name__ == '__main__':
    general_business_lst, bank_lst, insurance_lst, securities_lst = read_excel()
    for data in general_business_lst:
        print(data)
