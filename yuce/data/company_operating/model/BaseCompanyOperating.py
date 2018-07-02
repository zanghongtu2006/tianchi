# -*- coding: utf-8 -*-


class BaseCompanyOperating:
    def __init__(self, security_id, ticker_symbol, indic_name_en, end_date, value, unit_cd):
        # 证券代码
        self.security_id = security_id
        # 交易代码
        self.ticker_symbol = ticker_symbol
        # 指标
        self.indic_name_en = indic_name_en
        # 报告期
        self.end_date = end_date
        # 值
        self.value = value
        # 单位
        self.unit_cd = unit_cd

    def __str__(self) -> str:
        return 'CompanyOperating (security_id: %s, ticker_symbol: %s, indic_name_en: %s, ' \
               'end_date: %s, value: %s, unit_cd: %s)' % \
               (self.security_id, self.ticker_symbol, self.indic_name_en,
                self.end_date, self.value, self.unit_cd)
