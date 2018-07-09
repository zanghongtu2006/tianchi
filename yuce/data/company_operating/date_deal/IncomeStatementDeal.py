#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: IncomeStatementDeal.py

@time: 7/7/18 6:48 PM

@desc:

"""
import operator

from yuce.data.company_operating.data_init.finan_data import IncomeStatement
from yuce.data.company_operating.model.process.Income import Income
from yuce.data.company_operating.util.DateUtil import day2num

"""
帐期和类型的对应关系,用于校对数据是否正确
"""
check_dict = {
    '03-31': 'Q1',
    '06-30': 'S1',
    '09-30': 'Q3',
    '12-31': 'A'
}


def print_debug_data(income):
    """
    打印营收调试信息,仅供调试使用
    :param income: 营收信息(单条记录,对应excel数据一行)
    :return: 无
    """
    pass


def check_date_compare_type(income):
    """
    检查是否有财报帐期和财报类型对不上的结果
    规则: check_dict
    :param income: 营收结果集 { [code]=[end_date] = [Income]}
    :return: 无返回值,调试打印输出结果,当前所有数据无此类错误
    """
    print_debug_data(income)
    end_date_lst = income.end_date.split('-')
    check_key = '%s-%s' % (end_date_lst[1], end_date_lst[2])
    if operator.ne(check_dict.get(check_key), income.report_type):
        print(income)


def get_income():
    """
    Income Statement表General Business页的内容，整理后获取格式化后的季度营收
    营收: REVENUE
    编号: TICKET_SYMBOL.EXCHANGE_CD
    帐期: END_DATE(转数字), 按照END_DATE_REP时间去重,取END_DATE_REP大的那个
    账单类型: REPORT_TYPE
    账单发布时间: PUBLISH_DATE


    :return: { [code]=[end_date] = [Income]}
    """
    gb_lst = IncomeStatement.read_gb()
    result_lst = []
    result_dict = {}
    for data in gb_lst:
        code = '%s.%s' % (data.ticker_symbol, data.exchange_cd)
        key = '%s=%s' % (code, data.end_date)
        end_date_rep = day2num(data.end_date_rep)
        publish_date = day2num(data.publish_date)
        check_date_compare_type(data)
        income = Income(data.revenue, code, day2num(data.end_date), day2num(data.publish_date), data.report_type)
        result_lst.append(income)
        if key in result_dict:
            if end_date_rep == result_dict.get(key).end_date:
                if publish_date > result_dict.get(key).publish_date:
                    result_dict[key] = income
            elif end_date_rep > result_dict.get(key).end_date:
                result_dict[key] = income
        else:
            result_dict[key] = income
    return result_dict


def get_year_income():
    """
    整理财年数据
                                    result_dict
    {[code]: {                      code_dict
        [end_year] : {              year_dict
            [report_type]:[Income]
        }
    }}
    """
    dict_revenue = get_income()
    result_dict = {}
    for key in dict_revenue.keys():
        income = dict_revenue.get(key)
        key_lst = key.split("=")
        code = key_lst[0]
        year = key_lst[1].split("-")[0]

        code_dict = {}
        if code in result_dict:
            code_dict = result_dict.get(code)
        year_dict = {}
        if year in code_dict:
            year_dict = code_dict.get(year)
        year_dict[income.report_type] = income

        code_dict[year] = year_dict
        result_dict[code] = code_dict

    return result_dict


def analyse_year_income(result_dict):
    """
    分析全部结果集
    :param result_dict: 全部结果集
    :return: {[code]:[revenue]}
    """
    year_income_no_2018 = {}
    year_income_2018_no_2017 = {}

    for code in result_dict.keys():
        if '2018' not in result_dict.get(code).keys():
            year_income_no_2018[code] = result_dict.get(code)
        elif '2017' not in result_dict.get(code).keys():
            year_income_2018_no_2017[code] = result_dict.get(code)

    analyse_year_no_2018_income(year_income_no_2018)
    analyse_year_2018_no_2017_income(year_income_2018_no_2017)


def analyse_year_2018_no_2017_income(result_dict):
    """
    分析有2018年数据但是缺少2017年数据的
    :param result_dict: 有2018年数据但是缺少2017年数据的结果集
    :return:
    """
    for code in result_dict.keys():
        print('error: code:', code, result_dict.get(code))


def analyse_year_no_2018_income(result_dict):
    """
    分析缺少2018年数据的
    :param result_dict: 缺少2018年数据的结果集
    :return:
    """
    for code in result_dict.keys():
        if '2017' not in result_dict.get(code) or '2016' not in result_dict.get(code):
            # print('error: code:', code, result_dict.get(code))
            pass


result_dict = get_year_income()
analyse_year_income(result_dict)
