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
        self.party_id = row_data[0].value
        self.ticker_symbol = row_data[1].value
        self.exchange_cd = row_data[2].value
        self.publish_date = row_data[3].value
        self.end_date_rep = row_data[4].value
        self.end_date = row_data[5].value
        self.report_type = row_data[6].value
        self.fiscal_period = row_data[7].value
        self.merged_flag = row_data[8].value
        self.t_revenue = row_data[9].value
        self.revenue = row_data[10].value
        self.int_income = row_data[11].value
        self.prem_earned = row_data[12].value
        self.commis_income = row_data[13].value
        self.spec_tor = row_data[14].value
        self.ator = row_data[15].value
        self.t_cogs = row_data[16].value
        self.cogs = row_data[17].value
        self.int_exp = row_data[18].value
        self.commis_exp = row_data[19].value
        self.prem_refund = row_data[20].value
        self.n_compens_payout = row_data[21].value
        self.reser_insur_contr = row_data[22].value
        self.policy_div_payt = row_data[23].value
        self.reinsur_exp = row_data[24].value
        self.biz_tax_surchg = row_data[25].value
        self.sell_exp = row_data[26].value
        self.admin_exp = row_data[27].value
        self.finan_exp = row_data[28].value
        self.assets_impair_loss = row_data[29].value
        self.spec_toc = row_data[30].value
        self.atoc = row_data[31].value
        self.f_value_chg_gain = row_data[32].value
        self.invest_income = row_data[33].value
        self.a_j_invest_income = row_data[34].value
        self.forex_gain = row_data[35].value
        self.oth_effect_op = row_data[36].value
        self.assets_disp_gain = row_data[37].value
        self.ae_effect_op = row_data[38].value
        self.oth_gain = row_data[39].value
        self.operate_profit = row_data[40].value
        self.noperate_income = row_data[41].value
        self.noperate_exp = row_data[42].value
        self.nca_disploss = row_data[43].value
        self.oth_effect_tp = row_data[44].value
        self.ae_effect_tp = row_data[45].value
        self.t_profit = row_data[46].value
        self.income_tax = row_data[47].value
        self.oth_effect_np = row_data[48].value
        self.ae_effect_np = row_data[49].value
        self.n_income = row_data[50].value
        self.going_concern_ni = row_data[51].value
        self.quit_concern_ni = row_data[52].value
        self.n_income_attr_p = row_data[53].value
        self.n_income_bma = row_data[54].value
        self.minority_gain = row_data[55].value
        self.oth_effect_npp = row_data[56].value
        self.ae_effect_npp = row_data[57].value
        self.basic_eps = row_data[58].value
        self.diluted_eps = row_data[59].value
        self.oth_compr_income = row_data[60].value
        self.oth_effect_ci = row_data[61].value
        self.ae_effect_ci = row_data[62].value
        self.t_compr_income = row_data[63].value
        self.compr_inc_attr_p = row_data[64].value
        self.compr_inc_attr_m_s = row_data[65].value
        self.oth_effect_pci = row_data[66].value
        self.ae_effect_pci = row_data[67].value

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
        self.party_id = row_data[0].value
        self.ticker_symbol = row_data[1].value
        self.exchange_cd = row_data[2].value
        self.publish_date = row_data[3].value
        self.end_date_rep = row_data[4].value
        self.end_date = row_data[5].value
        self.report_type = row_data[6].value
        self.fiscal_period = row_data[7].value
        self.merged_flag = row_data[8].value
        self.revenue = row_data[9].value
        self.n_int_income = row_data[10].value
        self.int_income = row_data[11].value
        self.int_exp = row_data[12].value
        self.n_commis_income = row_data[13].value
        self.commis_income = row_data[14].value
        self.commis_exp = row_data[15].value
        self.invest_income = row_data[16].value
        self.a_j_invest_income = row_data[17].value
        self.f_value_chg_gain = row_data[18].value
        self.forex_gain = row_data[19].value
        self.assets_disp_gain = row_data[20].value
        self.oth_gain = row_data[21].value
        self.oth_oper_rev = row_data[22].value
        self.spec_or = row_data[23].value
        self.aor = row_data[24].value
        self.cogs = row_data[25].value
        self.biz_tax_surchg = row_data[26].value
        self.genl_admin_exp = row_data[27].value
        self.assets_impair_loss = row_data[28].value
        self.oth_oper_costs = row_data[29].value
        self.spec_oc = row_data[30].value
        self.aoc = row_data[31].value
        self.oth_effect_op = row_data[32].value
        self.ae_effect_op = row_data[33].value
        self.operate_profit = row_data[34].value
        self.noperate_income = row_data[35].value
        self.noperate_exp = row_data[36].value
        self.oth_effect_tp = row_data[37].value
        self.ae_effect_tp = row_data[38].value
        self.t_profit = row_data[39].value
        self.income_tax = row_data[40].value
        self.oth_effect_np = row_data[41].value
        self.ae_effect_np = row_data[42].value
        self.n_income = row_data[43].value
        self.going_concern_ni = row_data[44].value
        self.quit_concern_ni = row_data[45].value
        self.n_income_attr_p = row_data[46].value
        self.minority_gain = row_data[47].value
        self.oth_effect_npp = row_data[48].value
        self.ae_effect_npp = row_data[49].value
        self.basic_eps = row_data[50].value
        self.diluted_eps = row_data[51].value
        self.oth_compr_income = row_data[52].value
        self.oth_effect_ci = row_data[53].value
        self.ae_effect_ci = row_data[54].value
        self.t_compr_income = row_data[55].value
        self.compr_inc_attr_p = row_data[56].value
        self.compr_inc_attr_m_s = row_data[57].value
        self.oth_effect_pci = row_data[58].value
        self.ae_effect_pci = row_data[59].value

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
        self.party_id = row_data[0].value
        self.ticker_symbol = row_data[1].value
        self.exchange_cd = row_data[2].value
        self.publish_date = row_data[3].value
        self.end_date_rep = row_data[4].value
        self.end_date = row_data[5].value
        self.report_type = row_data[6].value
        self.fiscal_period = row_data[7].value
        self.merged_flag = row_data[8].value
        self.revenue = row_data[9].value
        self.prem_earned = row_data[10].value
        self.gross_prem_writ = row_data[11].value
        self.reins_income = row_data[12].value
        self.reinsur = row_data[13].value
        self.une_prem_reser = row_data[14].value
        self.f_value_chg_gain = row_data[15].value
        self.invest_income = row_data[16].value
        self.a_j_invest_income = row_data[17].value
        self.forex_gain = row_data[18].value
        self.assets_disp_gain = row_data[19].value
        self.oth_gain = row_data[20].value
        self.oth_oper_rev = row_data[21].value
        self.spec_or = row_data[22].value
        self.aor = row_data[23].value
        self.cogs = row_data[24].value
        self.prem_refund = row_data[25].value
        self.compens_payout = row_data[26].value
        self.compens_payout_refu = row_data[27].value
        self.reser_insur_liab = row_data[28].value
        self.insur_liab_reser_refu = row_data[29].value
        self.policy_div_payt = row_data[30].value
        self.reinsur_exp = row_data[31].value
        self.biz_tax_surchg = row_data[32].value
        self.commis_exp = row_data[33].value
        self.genl_admin_exp = row_data[34].value
        self.reins_cost_refund = row_data[35].value
        self.oth_oper_costs = row_data[36].value
        self.assets_impair_loss = row_data[37].value
        self.spec_oc = row_data[38].value
        self.aoc = row_data[39].value
        self.oth_effect_op = row_data[40].value
        self.ae_effect_op = row_data[41].value
        self.operate_profit = row_data[42].value
        self.noperate_income = row_data[43].value
        self.noperate_exp = row_data[44].value
        self.oth_effect_tp = row_data[45].value
        self.ae_effect_tp = row_data[46].value
        self.t_profit = row_data[47].value
        self.income_tax = row_data[48].value
        self.oth_effect_np = row_data[49].value
        self.ae_effect_np = row_data[50].value
        self.n_income = row_data[51].value
        self.going_concern_ni = row_data[52].value
        self.quit_concern_ni = row_data[53].value
        self.n_income_attr_p = row_data[54].value
        self.minority_gain = row_data[55].value
        self.oth_effect_npp = row_data[56].value
        self.ae_effect_npp = row_data[57].value
        self.basic_eps = row_data[58].value
        self.diluted_eps = row_data[59].value
        self.oth_compr_income = row_data[60].value
        self.oth_effect_ci = row_data[61].value
        self.ae_effect_ci = row_data[62].value
        self.t_compr_income = row_data[63].value
        self.compr_inc_attr_p = row_data[64].value
        self.compr_inc_attr_m_s = row_data[65].value
        self.oth_effect_pci = row_data[66].value
        self.ae_effect_pci = row_data[67].value

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
        self.party_id = row_data[0].value
        self.ticker_symbol = row_data[1].value
        self.exchange_cd = row_data[2].value
        self.publish_date = row_data[3].value
        self.end_date_rep = row_data[4].value
        self.end_date = row_data[5].value
        self.report_type = row_data[6].value
        self.fiscal_period = row_data[7].value
        self.merged_flag = row_data[8].value
        self.revenue = row_data[9].value
        self.n_commis_income = row_data[10].value
        self.n_sec_ta_income = row_data[11].value
        self.n_undwrt_sec_income = row_data[12].value
        self.n_trust_income = row_data[13].value
        self.n_int_income = row_data[14].value
        self.invest_income = row_data[15].value
        self.a_j_invest_income = row_data[16].value
        self.f_value_chg_gain = row_data[17].value
        self.forex_gain = row_data[18].value
        self.assets_disp_gain = row_data[19].value
        self.oth_gain = row_data[20].value
        self.oth_oper_rev = row_data[21].value
        self.spec_or = row_data[22].value
        self.aor = row_data[23].value
        self.cogs = row_data[24].value
        self.biz_tax_surchg = row_data[25].value
        self.genl_admin_exp = row_data[26].value
        self.assets_impair_loss = row_data[27].value
        self.oth_oper_costs = row_data[28].value
        self.spec_oc = row_data[29].value
        self.aoc = row_data[30].value
        self.oth_effect_op = row_data[31].value
        self.ae_effect_op = row_data[32].value
        self.operate_profit = row_data[33].value
        self.noperate_income = row_data[34].value
        self.noperate_exp = row_data[35].value
        self.oth_effect_tp = row_data[36].value
        self.ae_effect_tp = row_data[37].value
        self.t_profit = row_data[38].value
        self.income_tax = row_data[39].value
        self.oth_effect_np = row_data[40].value
        self.ae_effect_np = row_data[41].value
        self.n_income = row_data[42].value
        self.going_concern_ni = row_data[43].value
        self.quit_concern_ni = row_data[44].value
        self.n_income_attr_p = row_data[45].value
        self.minority_gain = row_data[46].value
        self.oth_effect_npp = row_data[47].value
        self.ae_effect_npp = row_data[48].value
        self.basic_eps = row_data[49].value
        self.diluted_eps = row_data[50].value
        self.oth_compr_income = row_data[51].value
        self.oth_effect_ci = row_data[52].value
        self.ae_effect_ci = row_data[53].value
        self.t_compr_income = row_data[54].value
        self.compr_inc_attr_p = row_data[55].value
        self.compr_inc_attr_m_s = row_data[56].value
        self.oth_effect_pci = row_data[57].value
        self.ae_effect_pci = row_data[58].value

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
