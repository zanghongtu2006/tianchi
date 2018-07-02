# -*- coding: utf-8 -*-
import sys

import xlrd

from yuce.data.company_operating.model.BaseCompanyOperating import BaseCompanyOperating
from yuce.data.constraint.Const import Const


def read_excel():
    workbook = xlrd.open_workbook(Const.file_new_company_operating_20180613)
    print(workbook.sheet_names())
    sheet_data = workbook.sheet_by_name('EN')
    data_lst = []
    for row in range(sheet_data.nrows):
        if row == 0:
            continue
        row_data = sheet_data.row(row)
        data = BaseCompanyOperating(row_data[0], row_data[1], row_data[2], row_data[3], row_data[4], row_data[5])
        data_lst.append(data)
    return data_lst


if __name__ == '__main__':
    print(sys.path)
    for data in read_excel():
        print(data)
