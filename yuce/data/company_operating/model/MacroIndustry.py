#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: MacroIndustry.py

@time: 7/2/18 8:19 PM

@desc:

"""


# 指标
class IndicInfo:

    def __init__(self, indic_id, name_cn, frequency_cd, unit_cd, data_table) -> None:
        self.indic_id = indic_id
        self.name_cn = name_cn
        self.frequency_cd = frequency_cd
        self.unit_cd = unit_cd
        self.data_table = data_table

    def __str__(self) -> str:
        return 'IndicInfo (indic_id: %s, name_cn: %s, frequency_cd: %s, ' \
               'unit_cd: %s, data_table: %s)' % \
               (self.indic_id, self.name_cn, self.frequency_cd,
                self.unit_cd, self.data_table)


class IndicData:
    def __init__(self, indic_id, name_cn, frequency_cd, period_date, data_value) -> None:
        self.indic_id = indic_id
        self.name_cn = name_cn
        self.frequency_cd = frequency_cd
        self.period_date = period_date
        self.data_value = data_value

    def __str__(self) -> str:
        return 'IndicData (indic_id: %s, name_cn: %s, frequency_cd: %s, ' \
               'period_date: %s, data_value: %s)' % \
               (self.indic_id, self.name_cn, self.frequency_cd,
                self.period_date, self.data_value)


Indic_CN_EN_Mapping = {

}

Unit_CD_CN_EN_Mapping = {

}
