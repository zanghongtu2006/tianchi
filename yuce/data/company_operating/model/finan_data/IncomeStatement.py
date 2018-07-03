#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: IncomeStatement.py

@time: 18-7-3 下午6:40

@desc:

"""


class GeneralBusiness:
    def __init__(self, row_data) -> None:
        self.party_id = row_data[0]
        self.ticker_symbol = row_data[1]
        self.exchange_cd = row_data[2]
        self.publish_date = row_data[3]
        self.end_date_rep = row_data[4]
        self.end_date = row_data[5]
        self.report_type = row_data[6]
        self.fiscal_period = row_data[7]
        self.merged_flag = row_data[8]
        self.t_revenue = row_data[9]
        self.revenue = row_data[10]
        self.int_income = row_data[11]
        self.prem_earned = row_data[12]
        self.commis_income = row_data[13]
        self.spec_tor = row_data[14]
        self.ator = row_data[15]
        self.t_cogs = row_data[16]
        self.cogs = row_data[17]
        self.int_exp = row_data[18]
        self.commis_exp = row_data[19]
        self.prem_refund = row_data[20]
        self.n_compens_payout = row_data[21]
        self.reser_insur_contr = row_data[22]
        self.policy_div_payt = row_data[23]
        self.reinsur_exp = row_data[24]
        self.biz_tax_surchg = row_data[25]
        self.sell_exp = row_data[26]
        self.admin_exp = row_data[27]
        self.finan_exp = row_data[28]
        self.assets_impair_loss = row_data[29]
        self.spec_toc = row_data[30]
        self.atoc = row_data[31]
        self.f_value_chg_gain = row_data[32]
        self.invest_income = row_data[33]
        self.a_j_invest_income = row_data[34]
        self.forex_gain = row_data[35]
        self.oth_effect_op = row_data[36]
        self.assets_disp_gain = row_data[37]
        self.ae_effect_op = row_data[38]
        self.oth_gain = row_data[39]
        self.operate_profit = row_data[40]
        self.noperate_income = row_data[41]
        self.noperate_exp = row_data[42]
        self.nca_disploss = row_data[43]
        self.oth_effect_tp = row_data[44]
        self.ae_effect_tp = row_data[45]
        self.t_profit = row_data[46]
        self.income_tax = row_data[47]
        self.oth_effect_np = row_data[48]
        self.ae_effect_np = row_data[49]
        self.n_income = row_data[50]
        self.going_concern_ni = row_data[51]
        self.quit_concern_ni = row_data[52]
        self.n_income_attr_p = row_data[53]
        self.n_income_bma = row_data[54]
        self.minority_gain = row_data[55]
        self.oth_effect_npp = row_data[56]
        self.ae_effect_npp = row_data[57]
        self.basic_eps = row_data[58]
        self.diluted_eps = row_data[59]
        self.oth_compr_income = row_data[60]
        self.oth_effect_ci = row_data[61]
        self.ae_effect_ci = row_data[62]
        self.t_compr_income = row_data[63]
        self.compr_inc_attr_p = row_data[64]
        self.compr_inc_attr_m_s = row_data[65]
        self.oth_effect_pci = row_data[66]
        self.ae_effect_pci = row_data[67]

    def __str__(self) -> str:
        return 'GeneralBusiness (' \
               'party_id: %s, ' \
               'ticker_symbol: %s, ' \
               'exchange_cd: %s, ' \
               'publish_date: %s, ' \
               'end_date_rep: %s, ' \
               'end_date: %s, ' \
               'report_type: %s, ' \
               'fiscal_period: %s, ' \
               'merged_flag: %s, ' \
               't_revenue: %s, ' \
               'revenue: %s, ' \
               'int_income: %s, ' \
               'prem_earned: %s, ' \
               'commis_income: %s, ' \
               'spec_tor: %s, ' \
               'ator: %s, ' \
               't_cogs: %s, ' \
               'cogs: %s, ' \
               'int_exp: %s, ' \
               'commis_exp: %s, ' \
               'prem_refund: %s, ' \
               'n_compens_payout: %s, ' \
               'reser_insur_contr: %s, ' \
               'policy_div_payt: %s, ' \
               'reinsur_exp: %s, ' \
               'biz_tax_surchg: %s, ' \
               'sell_exp: %s, ' \
               'admin_exp: %s, ' \
               'finan_exp: %s, ' \
               'assets_impair_loss: %s, ' \
               'spec_toc: %s, ' \
               'atoc: %s, ' \
               'f_value_chg_gain: %s, ' \
               'invest_income: %s, ' \
               'a_j_invest_income: %s, ' \
               'forex_gain: %s, ' \
               'oth_effect_op: %s, ' \
               'assets_disp_gain: %s, ' \
               'ae_effect_op: %s, ' \
               'oth_gain: %s, ' \
               'operate_profit: %s, ' \
               'noperate_income: %s, ' \
               'noperate_exp: %s, ' \
               'nca_disploss: %s, ' \
               'oth_effect_tp: %s, ' \
               'ae_effect_tp: %s, ' \
               't_profit: %s, ' \
               'income_tax: %s, ' \
               'oth_effect_np: %s, ' \
               'ae_effect_np: %s, ' \
               'n_income: %s, ' \
               'going_concern_ni: %s, ' \
               'quit_concern_ni: %s, ' \
               'n_income_attr_p: %s, ' \
               'n_income_bma: %s, ' \
               'minority_gain: %s, ' \
               'oth_effect_npp: %s, ' \
               'ae_effect_npp: %s, ' \
               'basic_eps: %s, ' \
               'diluted_eps: %s, ' \
               'oth_compr_income: %s, ' \
               'oth_effect_ci: %s, ' \
               'ae_effect_ci: %s, ' \
               't_compr_income: %s, ' \
               'compr_inc_attr_p: %s, ' \
               'compr_inc_attr_m_s: %s, ' \
               'oth_effect_pci: %s, ' \
               'ae_effect_pci: %s' \
               ')' % \
               (
                   self.party_id,
                   self.ticker_symbol,
                   self.exchange_cd,
                   self.publish_date,
                   self.end_date_rep,
                   self.end_date,
                   self.report_type,
                   self.fiscal_period,
                   self.merged_flag,
                   self.t_revenue,
                   self.revenue,
                   self.int_income,
                   self.prem_earned,
                   self.commis_income,
                   self.spec_tor,
                   self.ator,
                   self.t_cogs,
                   self.cogs,
                   self.int_exp,
                   self.commis_exp,
                   self.prem_refund,
                   self.n_compens_payout,
                   self.reser_insur_contr,
                   self.policy_div_payt,
                   self.reinsur_exp,
                   self.biz_tax_surchg,
                   self.sell_exp,
                   self.admin_exp,
                   self.finan_exp,
                   self.assets_impair_loss,
                   self.spec_toc,
                   self.atoc,
                   self.f_value_chg_gain,
                   self.invest_income,
                   self.a_j_invest_income,
                   self.forex_gain,
                   self.oth_effect_op,
                   self.assets_disp_gain,
                   self.ae_effect_op,
                   self.oth_gain,
                   self.operate_profit,
                   self.noperate_income,
                   self.noperate_exp,
                   self.nca_disploss,
                   self.oth_effect_tp,
                   self.ae_effect_tp,
                   self.t_profit,
                   self.income_tax,
                   self.oth_effect_np,
                   self.ae_effect_np,
                   self.n_income,
                   self.going_concern_ni,
                   self.quit_concern_ni,
                   self.n_income_attr_p,
                   self.n_income_bma,
                   self.minority_gain,
                   self.oth_effect_npp,
                   self.ae_effect_npp,
                   self.basic_eps,
                   self.diluted_eps,
                   self.oth_compr_income,
                   self.oth_effect_ci,
                   self.ae_effect_ci,
                   self.t_compr_income,
                   self.compr_inc_attr_p,
                   self.compr_inc_attr_m_s,
                   self.oth_effect_pci,
                   self.ae_effect_pci
               )


class Bank:
    def __init__(self, row_data) -> None:
        self.party_id = row_data[0]
        self.ticker_symbol = row_data[1]
        self.exchange_cd = row_data[2]
        self.publish_date = row_data[3]
        self.end_date_rep = row_data[4]
        self.end_date = row_data[5]
        self.report_type = row_data[6]
        self.fiscal_period = row_data[7]
        self.merged_flag = row_data[8]
        self.revenue = row_data[9]
        self.n_int_income = row_data[10]
        self.int_income = row_data[11]
        self.int_exp = row_data[12]
        self.n_commis_income = row_data[13]
        self.commis_income = row_data[14]
        self.commis_exp = row_data[15]
        self.invest_income = row_data[16]
        self.a_j_invest_income = row_data[17]
        self.f_value_chg_gain = row_data[18]
        self.forex_gain = row_data[19]
        self.assets_disp_gain = row_data[20]
        self.oth_gain = row_data[21]
        self.oth_oper_rev = row_data[22]
        self.spec_or = row_data[23]
        self.aor = row_data[24]
        self.cogs = row_data[25]
        self.biz_tax_surchg = row_data[26]
        self.genl_admin_exp = row_data[27]
        self.assets_impair_loss = row_data[28]
        self.oth_oper_costs = row_data[29]
        self.spec_oc = row_data[30]
        self.aoc = row_data[31]
        self.oth_effect_op = row_data[32]
        self.ae_effect_op = row_data[33]
        self.operate_profit = row_data[34]
        self.noperate_income = row_data[35]
        self.noperate_exp = row_data[36]
        self.oth_effect_tp = row_data[37]
        self.ae_effect_tp = row_data[38]
        self.t_profit = row_data[39]
        self.income_tax = row_data[40]
        self.oth_effect_np = row_data[41]
        self.ae_effect_np = row_data[42]
        self.n_income = row_data[43]
        self.going_concern_ni = row_data[44]
        self.quit_concern_ni = row_data[45]
        self.n_income_attr_p = row_data[46]
        self.minority_gain = row_data[47]
        self.oth_effect_npp = row_data[48]
        self.ae_effect_npp = row_data[49]
        self.basic_eps = row_data[50]
        self.diluted_eps = row_data[51]
        self.oth_compr_income = row_data[52]
        self.oth_effect_ci = row_data[53]
        self.ae_effect_ci = row_data[54]
        self.t_compr_income = row_data[55]
        self.compr_inc_attr_p = row_data[56]
        self.compr_inc_attr_m_s = row_data[57]
        self.oth_effect_pci = row_data[58]
        self.ae_effect_pci = row_data[59]

    def __str__(self) -> str:
        return 'Bank (' \
               'party_id: %s, ' \
               'ticker_symbol: %s, ' \
               'exchange_cd: %s, ' \
               'publish_date: %s, ' \
               'end_date_rep: %s, ' \
               'end_date: %s, ' \
               'report_type: %s, ' \
               'fiscal_period: %s, ' \
               'merged_flag: %s, ' \
               'revenue: %s, ' \
               'n_int_income: %s, ' \
               'int_income: %s, ' \
               'int_exp: %s, ' \
               'n_commis_income: %s, ' \
               'commis_income: %s, ' \
               'commis_exp: %s, ' \
               'invest_income: %s, ' \
               'a_j_invest_income: %s, ' \
               'f_value_chg_gain: %s, ' \
               'forex_gain: %s, ' \
               'assets_disp_gain: %s, ' \
               'oth_gain: %s, ' \
               'oth_oper_rev: %s, ' \
               'spec_or: %s, ' \
               'aor: %s, ' \
               'cogs: %s, ' \
               'biz_tax_surchg: %s, ' \
               'genl_admin_exp: %s, ' \
               'assets_impair_loss: %s, ' \
               'oth_oper_costs: %s, ' \
               'spec_oc: %s, ' \
               'aoc: %s, ' \
               'oth_effect_op: %s, ' \
               'ae_effect_op: %s, ' \
               'operate_profit: %s, ' \
               'noperate_income: %s, ' \
               'noperate_exp: %s, ' \
               'oth_effect_tp: %s, ' \
               'ae_effect_tp: %s, ' \
               't_profit: %s, ' \
               'income_tax: %s, ' \
               'oth_effect_np: %s, ' \
               'ae_effect_np: %s, ' \
               'n_income: %s, ' \
               'going_concern_ni: %s, ' \
               'quit_concern_ni: %s, ' \
               'n_income_attr_p: %s, ' \
               'minority_gain: %s, ' \
               'oth_effect_npp: %s, ' \
               'ae_effect_npp: %s, ' \
               'basic_eps: %s, ' \
               'diluted_eps: %s, ' \
               'oth_compr_income: %s, ' \
               'oth_effect_ci: %s, ' \
               'ae_effect_ci: %s, ' \
               't_compr_income: %s, ' \
               'compr_inc_attr_p: %s, ' \
               'compr_inc_attr_m_s: %s, ' \
               'oth_effect_pci: %s, ' \
               'ae_effect_pci: %s' \
               ')' % \
               (
                   self.party_id,
                   self.ticker_symbol,
                   self.exchange_cd,
                   self.publish_date,
                   self.end_date_rep,
                   self.end_date,
                   self.report_type,
                   self.fiscal_period,
                   self.merged_flag,
                   self.revenue,
                   self.n_int_income,
                   self.int_income,
                   self.int_exp,
                   self.n_commis_income,
                   self.commis_income,
                   self.commis_exp,
                   self.invest_income,
                   self.a_j_invest_income,
                   self.f_value_chg_gain,
                   self.forex_gain,
                   self.assets_disp_gain,
                   self.oth_gain,
                   self.oth_oper_rev,
                   self.spec_or,
                   self.aor,
                   self.cogs,
                   self.biz_tax_surchg,
                   self.genl_admin_exp,
                   self.assets_impair_loss,
                   self.oth_oper_costs,
                   self.spec_oc,
                   self.aoc,
                   self.oth_effect_op,
                   self.ae_effect_op,
                   self.operate_profit,
                   self.noperate_income,
                   self.noperate_exp,
                   self.oth_effect_tp,
                   self.ae_effect_tp,
                   self.t_profit,
                   self.income_tax,
                   self.oth_effect_np,
                   self.ae_effect_np,
                   self.n_income,
                   self.going_concern_ni,
                   self.quit_concern_ni,
                   self.n_income_attr_p,
                   self.minority_gain,
                   self.oth_effect_npp,
                   self.ae_effect_npp,
                   self.basic_eps,
                   self.diluted_eps,
                   self.oth_compr_income,
                   self.oth_effect_ci,
                   self.ae_effect_ci,
                   self.t_compr_income,
                   self.compr_inc_attr_p,
                   self.compr_inc_attr_m_s,
                   self.oth_effect_pci,
                   self.ae_effect_pci
               )


class Insurance:
    def __init__(self, row_data) -> None:
        self.party_id = row_data[0]
        self.ticker_symbol = row_data[1]
        self.exchange_cd = row_data[2]
        self.publish_date = row_data[3]
        self.end_date_rep = row_data[4]
        self.end_date = row_data[5]
        self.report_type = row_data[6]
        self.fiscal_period = row_data[7]
        self.merged_flag = row_data[8]
        self.revenue = row_data[9]
        self.prem_earned = row_data[10]
        self.gross_prem_writ = row_data[11]
        self.reins_income = row_data[12]
        self.reinsur = row_data[13]
        self.une_prem_reser = row_data[14]
        self.f_value_chg_gain = row_data[15]
        self.invest_income = row_data[16]
        self.a_j_invest_income = row_data[17]
        self.forex_gain = row_data[18]
        self.assets_disp_gain = row_data[19]
        self.oth_gain = row_data[20]
        self.oth_oper_rev = row_data[21]
        self.spec_or = row_data[22]
        self.aor = row_data[23]
        self.cogs = row_data[24]
        self.prem_refund = row_data[25]
        self.compens_payout = row_data[26]
        self.compens_payout_refu = row_data[27]
        self.reser_insur_liab = row_data[28]
        self.insur_liab_reser_refu = row_data[29]
        self.policy_div_payt = row_data[30]
        self.reinsur_exp = row_data[31]
        self.biz_tax_surchg = row_data[32]
        self.commis_exp = row_data[33]
        self.genl_admin_exp = row_data[34]
        self.reins_cost_refund = row_data[35]
        self.oth_oper_costs = row_data[36]
        self.assets_impair_loss = row_data[37]
        self.spec_oc = row_data[38]
        self.aoc = row_data[39]
        self.oth_effect_op = row_data[40]
        self.ae_effect_op = row_data[41]
        self.operate_profit = row_data[42]
        self.noperate_income = row_data[43]
        self.noperate_exp = row_data[44]
        self.oth_effect_tp = row_data[45]
        self.ae_effect_tp = row_data[46]
        self.t_profit = row_data[47]
        self.income_tax = row_data[48]
        self.oth_effect_np = row_data[49]
        self.ae_effect_np = row_data[50]
        self.n_income = row_data[51]
        self.going_concern_ni = row_data[52]
        self.quit_concern_ni = row_data[53]
        self.n_income_attr_p = row_data[54]
        self.minority_gain = row_data[55]
        self.oth_effect_npp = row_data[56]
        self.ae_effect_npp = row_data[57]
        self.basic_eps = row_data[58]
        self.diluted_eps = row_data[59]
        self.oth_compr_income = row_data[60]
        self.oth_effect_ci = row_data[61]
        self.ae_effect_ci = row_data[62]
        self.t_compr_income = row_data[63]
        self.compr_inc_attr_p = row_data[64]
        self.compr_inc_attr_m_s = row_data[65]
        self.oth_effect_pci = row_data[66]
        self.ae_effect_pci = row_data[67]

    def __str__(self) -> str:
        return 'Insurance (' \
               'party_id: %s ,' \
               'ticker_symbol: %s ,' \
               'exchange_cd: %s ,' \
               'publish_date: %s ,' \
               'end_date_rep: %s ,' \
               'end_date: %s ,' \
               'report_type: %s ,' \
               'fiscal_period: %s ,' \
               'merged_flag: %s ,' \
               'revenue: %s ,' \
               'prem_earned: %s ,' \
               'gross_prem_writ: %s ,' \
               'reins_income: %s ,' \
               'reinsur: %s ,' \
               'une_prem_reser: %s ,' \
               'f_value_chg_gain: %s ,' \
               'invest_income: %s ,' \
               'a_j_invest_income: %s ,' \
               'forex_gain: %s ,' \
               'assets_disp_gain: %s ,' \
               'oth_gain: %s ,' \
               'oth_oper_rev: %s ,' \
               'spec_or: %s ,' \
               'aor: %s ,' \
               'cogs: %s ,' \
               'prem_refund: %s ,' \
               'compens_payout: %s ,' \
               'compens_payout_refu: %s ,' \
               'reser_insur_liab: %s ,' \
               'insur_liab_reser_refu: %s ,' \
               'policy_div_payt: %s ,' \
               'reinsur_exp: %s ,' \
               'biz_tax_surchg: %s ,' \
               'commis_exp: %s ,' \
               'genl_admin_exp: %s ,' \
               'reins_cost_refund: %s ,' \
               'oth_oper_costs: %s ,' \
               'assets_impair_loss: %s ,' \
               'spec_oc: %s ,' \
               'aoc: %s ,' \
               'oth_effect_op: %s ,' \
               'ae_effect_op: %s ,' \
               'operate_profit: %s ,' \
               'noperate_income: %s ,' \
               'noperate_exp: %s ,' \
               'oth_effect_tp: %s ,' \
               'ae_effect_tp: %s ,' \
               't_profit: %s ,' \
               'income_tax: %s ,' \
               'oth_effect_np: %s ,' \
               'ae_effect_np: %s ,' \
               'n_income: %s ,' \
               'going_concern_ni: %s ,' \
               'quit_concern_ni: %s ,' \
               'n_income_attr_p: %s ,' \
               'minority_gain: %s ,' \
               'oth_effect_npp: %s ,' \
               'ae_effect_npp: %s ,' \
               'basic_eps: %s ,' \
               'diluted_eps: %s ,' \
               'oth_compr_income: %s ,' \
               'oth_effect_ci: %s ,' \
               'ae_effect_ci: %s ,' \
               't_compr_income: %s ,' \
               'compr_inc_attr_p: %s ,' \
               'compr_inc_attr_m_s: %s ,' \
               'oth_effect_pci: %s ,' \
               'ae_effect_pci: %s' \
               ')' % \
               (
                   self.party_id,
                   self.ticker_symbol,
                   self.exchange_cd,
                   self.publish_date,
                   self.end_date_rep,
                   self.end_date,
                   self.report_type,
                   self.fiscal_period,
                   self.merged_flag,
                   self.revenue,
                   self.prem_earned,
                   self.gross_prem_writ,
                   self.reins_income,
                   self.reinsur,
                   self.une_prem_reser,
                   self.f_value_chg_gain,
                   self.invest_income,
                   self.a_j_invest_income,
                   self.forex_gain,
                   self.assets_disp_gain,
                   self.oth_gain,
                   self.oth_oper_rev,
                   self.spec_or,
                   self.aor,
                   self.cogs,
                   self.prem_refund,
                   self.compens_payout,
                   self.compens_payout_refu,
                   self.reser_insur_liab,
                   self.insur_liab_reser_refu,
                   self.policy_div_payt,
                   self.reinsur_exp,
                   self.biz_tax_surchg,
                   self.commis_exp,
                   self.genl_admin_exp,
                   self.reins_cost_refund,
                   self.oth_oper_costs,
                   self.assets_impair_loss,
                   self.spec_oc,
                   self.aoc,
                   self.oth_effect_op,
                   self.ae_effect_op,
                   self.operate_profit,
                   self.noperate_income,
                   self.noperate_exp,
                   self.oth_effect_tp,
                   self.ae_effect_tp,
                   self.t_profit,
                   self.income_tax,
                   self.oth_effect_np,
                   self.ae_effect_np,
                   self.n_income,
                   self.going_concern_ni,
                   self.quit_concern_ni,
                   self.n_income_attr_p,
                   self.minority_gain,
                   self.oth_effect_npp,
                   self.ae_effect_npp,
                   self.basic_eps,
                   self.diluted_eps,
                   self.oth_compr_income,
                   self.oth_effect_ci,
                   self.ae_effect_ci,
                   self.t_compr_income,
                   self.compr_inc_attr_p,
                   self.compr_inc_attr_m_s,
                   self.oth_effect_pci,
                   self.ae_effect_pci
               )


class Securities:
    def __init__(self, row_data) -> None:
        self.party_id = row_data[0]
        self.ticker_symbol = row_data[1]
        self.exchange_cd = row_data[2]
        self.publish_date = row_data[3]
        self.end_date_rep = row_data[4]
        self.end_date = row_data[5]
        self.report_type = row_data[6]
        self.fiscal_period = row_data[7]
        self.merged_flag = row_data[8]
        self.revenue = row_data[9]
        self.n_commis_income = row_data[10]
        self.n_sec_ta_income = row_data[11]
        self.n_undwrt_sec_income = row_data[12]
        self.n_trust_income = row_data[13]
        self.n_int_income = row_data[14]
        self.invest_income = row_data[15]
        self.a_j_invest_income = row_data[16]
        self.f_value_chg_gain = row_data[17]
        self.forex_gain = row_data[18]
        self.assets_disp_gain = row_data[19]
        self.oth_gain = row_data[20]
        self.oth_oper_rev = row_data[21]
        self.spec_or = row_data[22]
        self.aor = row_data[23]
        self.cogs = row_data[24]
        self.biz_tax_surchg = row_data[25]
        self.genl_admin_exp = row_data[26]
        self.assets_impair_loss = row_data[27]
        self.oth_oper_costs = row_data[28]
        self.spec_oc = row_data[29]
        self.aoc = row_data[30]
        self.oth_effect_op = row_data[31]
        self.ae_effect_op = row_data[32]
        self.operate_profit = row_data[33]
        self.noperate_income = row_data[34]
        self.noperate_exp = row_data[35]
        self.oth_effect_tp = row_data[36]
        self.ae_effect_tp = row_data[37]
        self.t_profit = row_data[38]
        self.income_tax = row_data[39]
        self.oth_effect_np = row_data[40]
        self.ae_effect_np = row_data[41]
        self.n_income = row_data[42]
        self.going_concern_ni = row_data[43]
        self.quit_concern_ni = row_data[44]
        self.n_income_attr_p = row_data[45]
        self.minority_gain = row_data[46]
        self.oth_effect_npp = row_data[47]
        self.ae_effect_npp = row_data[48]
        self.basic_eps = row_data[49]
        self.diluted_eps = row_data[50]
        self.oth_compr_income = row_data[51]
        self.oth_effect_ci = row_data[52]
        self.ae_effect_ci = row_data[53]
        self.t_compr_income = row_data[54]
        self.compr_inc_attr_p = row_data[55]
        self.compr_inc_attr_m_s = row_data[56]
        self.oth_effect_pci = row_data[57]
        self.ae_effect_pci = row_data[58]

    def __str__(self) -> str:
        return 'Securities (' \
               'party_id: %s, ' \
               'ticker_symbol: %s, ' \
               'exchange_cd: %s, ' \
               'publish_date: %s, ' \
               'end_date_rep: %s, ' \
               'end_date: %s, ' \
               'report_type: %s, ' \
               'fiscal_period: %s, ' \
               'merged_flag: %s, ' \
               'revenue: %s, ' \
               'n_commis_income: %s, ' \
               'n_sec_ta_income: %s, ' \
               'n_undwrt_sec_income: %s, ' \
               'n_trust_income: %s, ' \
               'n_int_income: %s, ' \
               'invest_income: %s, ' \
               'a_j_invest_income: %s, ' \
               'f_value_chg_gain: %s, ' \
               'forex_gain: %s, ' \
               'assets_disp_gain: %s, ' \
               'oth_gain: %s, ' \
               'oth_oper_rev: %s, ' \
               'spec_or: %s, ' \
               'aor: %s, ' \
               'cogs: %s, ' \
               'biz_tax_surchg: %s, ' \
               'genl_admin_exp: %s, ' \
               'assets_impair_loss: %s, ' \
               'oth_oper_costs: %s, ' \
               'spec_oc: %s, ' \
               'aoc: %s, ' \
               'oth_effect_op: %s, ' \
               'ae_effect_op: %s, ' \
               'operate_profit: %s, ' \
               'noperate_income: %s, ' \
               'noperate_exp: %s, ' \
               'oth_effect_tp: %s, ' \
               'ae_effect_tp: %s, ' \
               't_profit: %s, ' \
               'income_tax: %s, ' \
               'oth_effect_np: %s, ' \
               'ae_effect_np: %s, ' \
               'n_income: %s, ' \
               'going_concern_ni: %s, ' \
               'quit_concern_ni: %s, ' \
               'n_income_attr_p: %s, ' \
               'minority_gain: %s, ' \
               'oth_effect_npp: %s, ' \
               'ae_effect_npp: %s, ' \
               'basic_eps: %s, ' \
               'diluted_eps: %s, ' \
               'oth_compr_income: %s, ' \
               'oth_effect_ci: %s, ' \
               'ae_effect_ci: %s, ' \
               't_compr_income: %s, ' \
               'compr_inc_attr_p: %s, ' \
               'compr_inc_attr_m_s: %s, ' \
               'oth_effect_pci: %s, ' \
               'ae_effect_pci: %s' \
               ')' % \
               (
                   self.party_id,
                   self.ticker_symbol,
                   self.exchange_cd,
                   self.publish_date,
                   self.end_date_rep,
                   self.end_date,
                   self.report_type,
                   self.fiscal_period,
                   self.merged_flag,
                   self.revenue,
                   self.n_commis_income,
                   self.n_sec_ta_income,
                   self.n_undwrt_sec_income,
                   self.n_trust_income,
                   self.n_int_income,
                   self.invest_income,
                   self.a_j_invest_income,
                   self.f_value_chg_gain,
                   self.forex_gain,
                   self.assets_disp_gain,
                   self.oth_gain,
                   self.oth_oper_rev,
                   self.spec_or,
                   self.aor,
                   self.cogs,
                   self.biz_tax_surchg,
                   self.genl_admin_exp,
                   self.assets_impair_loss,
                   self.oth_oper_costs,
                   self.spec_oc,
                   self.aoc,
                   self.oth_effect_op,
                   self.ae_effect_op,
                   self.operate_profit,
                   self.noperate_income,
                   self.noperate_exp,
                   self.oth_effect_tp,
                   self.ae_effect_tp,
                   self.t_profit,
                   self.income_tax,
                   self.oth_effect_np,
                   self.ae_effect_np,
                   self.n_income,
                   self.going_concern_ni,
                   self.quit_concern_ni,
                   self.n_income_attr_p,
                   self.minority_gain,
                   self.oth_effect_npp,
                   self.ae_effect_npp,
                   self.basic_eps,
                   self.diluted_eps,
                   self.oth_compr_income,
                   self.oth_effect_ci,
                   self.ae_effect_ci,
                   self.t_compr_income,
                   self.compr_inc_attr_p,
                   self.compr_inc_attr_m_s,
                   self.oth_effect_pci,
                   self.ae_effect_pci
               )
