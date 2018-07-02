# -*- coding: utf-8 -*-
import sys


class Const:
    base_data_dir = sys.path[1] + '/yuce/[Add April May] FDDC_financial_data_20180613'
    finan_data_dir = base_data_dir + '/[New] Financial Data_20180613'

    file_new_company_operating_20180613 = base_data_dir + '/[New] Company Operating_2018613.xlsx'
    file_new_macro_inststry_20180613 = base_data_dir + '/[New] Macro&Industry_20180613.xlsx'
    file_new_market_data_20180613 = base_data_dir + '/[New] Market Data_20180613.xlsx'

    file_finan_balance = finan_data_dir + '/Balance Sheet.xls'
    file_finan_cash_flow_statement = finan_data_dir + 'Cash Flow Statement.xls'
    file_finan_data_dictionary = finan_data_dir + 'Data Dictionary_5.29.xlsx'
    file_finan_incom_statement = finan_data_dir + 'Income Statement.xls'
