#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: CashFlowStatement.py

@time: 18-7-3 下午6:39

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
        self.c_fr_sale_g_s = row_data[9]
        self.n_depos_incr_c_fi = row_data[10]
        self.n_incr_borr_fr_cb = row_data[11]
        self.n_inc_borr_oth_fi = row_data[12]
        self.prem_fr_orig_contr = row_data[13]
        self.n_reinsur_prem = row_data[14]
        self.n_inc_ph_depos_inv = row_data[15]
        self.n_inc_disp_trad_fa = row_data[16]
        self.ifc_cash_incr = row_data[17]
        self.n_inc_fr_borr = row_data[18]
        self.n_cap_incr_repur = row_data[19]
        self.refund_of_tax = row_data[20]
        self.c_fr_oth_operate_a = row_data[21]
        self.spec_ocif = row_data[22]
        self.aocif = row_data[23]
        self.c_inf_fr_operate_a = row_data[24]
        self.c_paid_g_s = row_data[25]
        self.n_inc_disbur_of_la = row_data[26]
        self.net_incr_depos_in_fi = row_data[27]
        self.orig_contr_c_indem = row_data[28]
        self.c_paid_ifc = row_data[29]
        self.c_paid_pol_div = row_data[30]
        self.c_paid_to_for_empl = row_data[31]
        self.c_paid_for_taxes = row_data[32]
        self.c_paid_for_oth_op_a = row_data[33]
        self.spec_ocof = row_data[34]
        self.aocof = row_data[35]
        self.c_outf_operate_a = row_data[36]
        self.anocf = row_data[37]
        self.n_cf_operate_a = row_data[38]
        self.proc_sell_invest = row_data[39]
        self.gain_invest = row_data[40]
        self.disp_fix_assets_oth = row_data[41]
        self.n_disp_subs_oth_biz_c = row_data[42]
        self.c_fr_oth_invest_a = row_data[43]
        self.spec_icif = row_data[44]
        self.aicif = row_data[45]
        self.c_inf_fr_invest_a = row_data[46]
        self.pur_fix_assets_oth = row_data[47]
        self.c_paid_invest = row_data[48]
        self.n_incr_pledge_loan = row_data[49]
        self.n_c_paid_acquis = row_data[50]
        self.c_paid_oth_invest_a = row_data[51]
        self.spec_icof = row_data[52]
        self.aicof = row_data[53]
        self.c_outf_fr_invest_a = row_data[54]
        self.anicf = row_data[55]
        self.n_cf_fr_invest_a = row_data[56]
        self.c_fr_cap_contr = row_data[57]
        self.c_fr_mino_s_subs = row_data[58]
        self.c_fr_borr = row_data[59]
        self.c_fr_issue_bond = row_data[60]
        self.c_fr_oth_finan_a = row_data[61]
        self.spec_fcif = row_data[62]
        self.afcif = row_data[63]
        self.c_inf_fr_finan_a = row_data[64]
        self.c_paid_for_debts = row_data[65]
        self.c_paid_div_prof_int = row_data[66]
        self.div_prof_subs_mino_s = row_data[67]
        self.c_paid_oth_finan_a = row_data[68]
        self.spec_fcof = row_data[69]
        self.afcof = row_data[70]
        self.c_outf_fr_finan_a = row_data[71]
        self.anfcf = row_data[72]
        self.n_cf_fr_finan_a = row_data[73]
        self.forex_effects = row_data[74]
        self.oth_effect_ce = row_data[75]
        self.ace = row_data[76]
        self.n_change_in_cash = row_data[77]
        self.n_ce_beg_bal = row_data[78]
        self.oth_effect_cei = row_data[79]
        self.acei = row_data[80]
        self.n_ce_end_bal = row_data[81]

    def __str__(self) -> str:
        return 'GeneralBusiness (' \
               'party_id %s, ' \
               'ticker_symbol %s, ' \
               'exchange_cd %s, ' \
               'publish_date %s, ' \
               'end_date_rep %s, ' \
               'end_date %s, ' \
               'report_type %s, ' \
               'fiscal_period %s, ' \
               'merged_flag %s, ' \
               'c_fr_sale_g_s %s, ' \
               'n_depos_incr_c_fi %s, ' \
               'n_incr_borr_fr_cb %s, ' \
               'n_inc_borr_oth_fi %s, ' \
               'prem_fr_orig_contr %s, ' \
               'n_reinsur_prem %s, ' \
               'n_inc_ph_depos_inv %s, ' \
               'n_inc_disp_trad_fa %s, ' \
               'ifc_cash_incr %s, ' \
               'n_inc_fr_borr %s, ' \
               'n_cap_incr_repur %s, ' \
               'refund_of_tax %s, ' \
               'c_fr_oth_operate_a %s, ' \
               'spec_ocif %s, ' \
               'aocif %s, ' \
               'c_inf_fr_operate_a %s, ' \
               'c_paid_g_s %s, ' \
               'n_inc_disbur_of_la %s, ' \
               'net_incr_depos_in_fi %s, ' \
               'orig_contr_c_indem %s, ' \
               'c_paid_ifc %s, ' \
               'c_paid_pol_div %s, ' \
               'c_paid_to_for_empl %s, ' \
               'c_paid_for_taxes %s, ' \
               'c_paid_for_oth_op_a %s, ' \
               'spec_ocof %s, ' \
               'aocof %s, ' \
               'c_outf_operate_a %s, ' \
               'anocf %s, ' \
               'n_cf_operate_a %s, ' \
               'proc_sell_invest %s, ' \
               'gain_invest %s, ' \
               'disp_fix_assets_oth %s, ' \
               'n_disp_subs_oth_biz_c %s, ' \
               'c_fr_oth_invest_a %s, ' \
               'spec_icif %s, ' \
               'aicif %s, ' \
               'c_inf_fr_invest_a %s, ' \
               'pur_fix_assets_oth %s, ' \
               'c_paid_invest %s, ' \
               'n_incr_pledge_loan %s, ' \
               'n_c_paid_acquis %s, ' \
               'c_paid_oth_invest_a %s, ' \
               'spec_icof %s, ' \
               'aicof %s, ' \
               'c_outf_fr_invest_a %s, ' \
               'anicf %s, ' \
               'n_cf_fr_invest_a %s, ' \
               'c_fr_cap_contr %s, ' \
               'c_fr_mino_s_subs %s, ' \
               'c_fr_borr %s, ' \
               'c_fr_issue_bond %s, ' \
               'c_fr_oth_finan_a %s, ' \
               'spec_fcif %s, ' \
               'afcif %s, ' \
               'c_inf_fr_finan_a %s, ' \
               'c_paid_for_debts %s, ' \
               'c_paid_div_prof_int %s, ' \
               'div_prof_subs_mino_s %s, ' \
               'c_paid_oth_finan_a %s, ' \
               'spec_fcof %s, ' \
               'afcof %s, ' \
               'c_outf_fr_finan_a %s, ' \
               'anfcf %s, ' \
               'n_cf_fr_finan_a %s, ' \
               'forex_effects %s, ' \
               'oth_effect_ce %s, ' \
               'ace %s, ' \
               'n_change_in_cash %s, ' \
               'n_ce_beg_bal %s, ' \
               'oth_effect_cei %s, ' \
               'acei %s, ' \
               'n_ce_end_bal %s, )' % \
               (self.party_id,
                self.ticker_symbol,
                self.exchange_cd,
                self.publish_date,
                self.end_date_rep,
                self.end_date,
                self.report_type,
                self.fiscal_period,
                self.merged_flag,
                self.c_fr_sale_g_s,
                self.n_depos_incr_c_fi,
                self.n_incr_borr_fr_cb,
                self.n_inc_borr_oth_fi,
                self.prem_fr_orig_contr,
                self.n_reinsur_prem,
                self.n_inc_ph_depos_inv,
                self.n_inc_disp_trad_fa,
                self.ifc_cash_incr,
                self.n_inc_fr_borr,
                self.n_cap_incr_repur,
                self.refund_of_tax,
                self.c_fr_oth_operate_a,
                self.spec_ocif,
                self.aocif,
                self.c_inf_fr_operate_a,
                self.c_paid_g_s,
                self.n_inc_disbur_of_la,
                self.net_incr_depos_in_fi,
                self.orig_contr_c_indem,
                self.c_paid_ifc,
                self.c_paid_pol_div,
                self.c_paid_to_for_empl,
                self.c_paid_for_taxes,
                self.c_paid_for_oth_op_a,
                self.spec_ocof,
                self.aocof,
                self.c_outf_operate_a,
                self.anocf,
                self.n_cf_operate_a,
                self.proc_sell_invest,
                self.gain_invest,
                self.disp_fix_assets_oth,
                self.n_disp_subs_oth_biz_c,
                self.c_fr_oth_invest_a,
                self.spec_icif,
                self.aicif,
                self.c_inf_fr_invest_a,
                self.pur_fix_assets_oth,
                self.c_paid_invest,
                self.n_incr_pledge_loan,
                self.n_c_paid_acquis,
                self.c_paid_oth_invest_a,
                self.spec_icof,
                self.aicof,
                self.c_outf_fr_invest_a,
                self.anicf,
                self.n_cf_fr_invest_a,
                self.c_fr_cap_contr,
                self.c_fr_mino_s_subs,
                self.c_fr_borr,
                self.c_fr_issue_bond,
                self.c_fr_oth_finan_a,
                self.spec_fcif,
                self.afcif,
                self.c_inf_fr_finan_a,
                self.c_paid_for_debts,
                self.c_paid_div_prof_int,
                self.div_prof_subs_mino_s,
                self.c_paid_oth_finan_a,
                self.spec_fcof,
                self.afcof,
                self.c_outf_fr_finan_a,
                self.anfcf,
                self.n_cf_fr_finan_a,
                self.forex_effects,
                self.oth_effect_ce,
                self.ace,
                self.n_change_in_cash,
                self.n_ce_beg_bal,
                self.oth_effect_cei,
                self.acei,
                self.n_ce_end_bal)


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
        self.n_depos_incr_c_fi = row_data[9]
        self.n_incr_borr_fr_cb = row_data[10]
        self.n_inc_borr_oth_fi = row_data[11]
        self.n_decr_in_disbur_of_la = row_data[12]
        self.net_decr_in_depos_in_fi = row_data[13]
        self.n_decr_loan_to_oth_fi = row_data[14]
        self.ifc_cash_incr = row_data[15]
        self.c_fr_oth_operate_a = row_data[16]
        self.spec_ocif = row_data[17]
        self.aocif = row_data[18]
        self.c_inf_fr_operate_a = row_data[19]
        self.n_depos_decr_fr_fi = row_data[20]
        self.n_decr_borr_fr_cb = row_data[21]
        self.n_decr_borr_fr_oth_fi = row_data[22]
        self.n_inc_disbur_of_la = row_data[23]
        self.net_incr_depos_in_fi = row_data[24]
        self.n_incr_loans_to_oth_fi = row_data[25]
        self.c_paid_ifc = row_data[26]
        self.c_paid_to_for_empl = row_data[27]
        self.c_paid_for_taxes = row_data[28]
        self.c_paid_for_oth_op_a = row_data[29]
        self.spec_ocof = row_data[30]
        self.aocof = row_data[31]
        self.c_outf_operate_a = row_data[32]
        self.anocf = row_data[33]
        self.n_cf_operate_a = row_data[34]
        self.proc_sell_invest = row_data[35]
        self.gain_invest = row_data[36]
        self.disp_fix_assets_oth = row_data[37]
        self.n_disp_subs_oth_biz_c = row_data[38]
        self.c_fr_oth_invest_a = row_data[39]
        self.spec_icif = row_data[40]
        self.aicif = row_data[41]
        self.c_inf_fr_invest_a = row_data[42]
        self.c_paid_invest = row_data[43]
        self.pur_fix_assets_oth = row_data[44]
        self.n_c_paid_acquis = row_data[45]
        self.c_paid_oth_invest_a = row_data[46]
        self.spec_icof = row_data[47]
        self.aicof = row_data[48]
        self.c_outf_fr_invest_a = row_data[49]
        self.anicf = row_data[50]
        self.n_cf_fr_invest_a = row_data[51]
        self.c_fr_cap_contr = row_data[52]
        self.c_fr_mino_s_subs = row_data[53]
        self.c_fr_issue_bond = row_data[54]
        self.c_fr_oth_finan_a = row_data[55]
        self.spec_fcif = row_data[56]
        self.afcif = row_data[57]
        self.c_inf_fr_finan_a = row_data[58]
        self.c_paid_for_debts = row_data[59]
        self.c_paid_div_prof_int = row_data[60]
        self.div_prof_subs_mino_s = row_data[61]
        self.c_paid_oth_finan_a = row_data[62]
        self.spec_fcof = row_data[63]
        self.afcof = row_data[64]
        self.c_outf_fr_finan_a = row_data[65]
        self.anfcf = row_data[66]
        self.n_cf_fr_finan_a = row_data[67]
        self.forex_effects = row_data[68]
        self.oth_effect_ce = row_data[69]
        self.ace = row_data[70]
        self.n_change_in_cash = row_data[71]
        self.n_ce_beg_bal = row_data[72]
        self.oth_effect_cei = row_data[73]
        self.acei = row_data[74]
        self.n_ce_end_bal = row_data[75]

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
               'n_depos_incr_c_fi: %s, ' \
               'n_incr_borr_fr_cb: %s, ' \
               'n_inc_borr_oth_fi: %s, ' \
               'n_decr_in_disbur_of_la: %s, ' \
               'net_decr_in_depos_in_fi: %s, ' \
               'n_decr_loan_to_oth_fi: %s, ' \
               'ifc_cash_incr: %s, ' \
               'c_fr_oth_operate_a: %s, ' \
               'spec_ocif: %s, ' \
               'aocif: %s, ' \
               'c_inf_fr_operate_a: %s, ' \
               'n_depos_decr_fr_fi: %s, ' \
               'n_decr_borr_fr_cb: %s, ' \
               'n_decr_borr_fr_oth_fi: %s, ' \
               'n_inc_disbur_of_la: %s, ' \
               'net_incr_depos_in_fi: %s, ' \
               'n_incr_loans_to_oth_fi: %s, ' \
               'c_paid_ifc: %s, ' \
               'c_paid_to_for_empl: %s, ' \
               'c_paid_for_taxes: %s, ' \
               'c_paid_for_oth_op_a: %s, ' \
               'spec_ocof: %s, ' \
               'aocof: %s, ' \
               'c_outf_operate_a: %s, ' \
               'anocf: %s, ' \
               'n_cf_operate_a: %s, ' \
               'proc_sell_invest: %s, ' \
               'gain_invest: %s, ' \
               'disp_fix_assets_oth: %s, ' \
               'n_disp_subs_oth_biz_c: %s, ' \
               'c_fr_oth_invest_a: %s, ' \
               'spec_icif: %s, ' \
               'aicif: %s, ' \
               'c_inf_fr_invest_a: %s, ' \
               'c_paid_invest: %s, ' \
               'pur_fix_assets_oth: %s, ' \
               'n_c_paid_acquis: %s, ' \
               'c_paid_oth_invest_a: %s, ' \
               'spec_icof: %s, ' \
               'aicof: %s, ' \
               'c_outf_fr_invest_a: %s, ' \
               'anicf: %s, ' \
               'n_cf_fr_invest_a: %s, ' \
               'c_fr_cap_contr: %s, ' \
               'c_fr_mino_s_subs: %s, ' \
               'c_fr_issue_bond: %s, ' \
               'c_fr_oth_finan_a: %s, ' \
               'spec_fcif: %s, ' \
               'afcif: %s, ' \
               'c_inf_fr_finan_a: %s, ' \
               'c_paid_for_debts: %s, ' \
               'c_paid_div_prof_int: %s, ' \
               'div_prof_subs_mino_s: %s, ' \
               'c_paid_oth_finan_a: %s, ' \
               'spec_fcof: %s, ' \
               'afcof: %s, ' \
               'c_outf_fr_finan_a: %s, ' \
               'anfcf: %s, ' \
               'n_cf_fr_finan_a: %s, ' \
               'forex_effects: %s, ' \
               'oth_effect_ce: %s, ' \
               'ace: %s, ' \
               'n_change_in_cash: %s, ' \
               'n_ce_beg_bal: %s, ' \
               'oth_effect_cei: %s, ' \
               'acei: %s, ' \
               'n_ce_end_bal: %s, ' \
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
                   self.n_depos_incr_c_fi,
                   self.n_incr_borr_fr_cb,
                   self.n_inc_borr_oth_fi,
                   self.n_decr_in_disbur_of_la,
                   self.net_decr_in_depos_in_fi,
                   self.n_decr_loan_to_oth_fi,
                   self.ifc_cash_incr,
                   self.c_fr_oth_operate_a,
                   self.spec_ocif,
                   self.aocif,
                   self.c_inf_fr_operate_a,
                   self.n_depos_decr_fr_fi,
                   self.n_decr_borr_fr_cb,
                   self.n_decr_borr_fr_oth_fi,
                   self.n_inc_disbur_of_la,
                   self.net_incr_depos_in_fi,
                   self.n_incr_loans_to_oth_fi,
                   self.c_paid_ifc,
                   self.c_paid_to_for_empl,
                   self.c_paid_for_taxes,
                   self.c_paid_for_oth_op_a,
                   self.spec_ocof,
                   self.aocof,
                   self.c_outf_operate_a,
                   self.anocf,
                   self.n_cf_operate_a,
                   self.proc_sell_invest,
                   self.gain_invest,
                   self.disp_fix_assets_oth,
                   self.n_disp_subs_oth_biz_c,
                   self.c_fr_oth_invest_a,
                   self.spec_icif,
                   self.aicif,
                   self.c_inf_fr_invest_a,
                   self.c_paid_invest,
                   self.pur_fix_assets_oth,
                   self.n_c_paid_acquis,
                   self.c_paid_oth_invest_a,
                   self.spec_icof,
                   self.aicof,
                   self.c_outf_fr_invest_a,
                   self.anicf,
                   self.n_cf_fr_invest_a,
                   self.c_fr_cap_contr,
                   self.c_fr_mino_s_subs,
                   self.c_fr_issue_bond,
                   self.c_fr_oth_finan_a,
                   self.spec_fcif,
                   self.afcif,
                   self.c_inf_fr_finan_a,
                   self.c_paid_for_debts,
                   self.c_paid_div_prof_int,
                   self.div_prof_subs_mino_s,
                   self.c_paid_oth_finan_a,
                   self.spec_fcof,
                   self.afcof,
                   self.c_outf_fr_finan_a,
                   self.anfcf,
                   self.n_cf_fr_finan_a,
                   self.forex_effects,
                   self.oth_effect_ce,
                   self.ace,
                   self.n_change_in_cash,
                   self.n_ce_beg_bal,
                   self.oth_effect_cei,
                   self.acei,
                   self.n_ce_end_bal
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
        self.n_depos_incr_c_fi = row_data[9]
        self.n_incr_borr_fr_cb = row_data[10]
        self.prem_fr_orig_contr = row_data[11]
        self.n_reinsur_prem = row_data[12]
        self.n_inc_ph_depos_inv = row_data[13]
        self.ifc_cash_incr = row_data[14]
        self.refund_of_tax = row_data[15]
        self.c_fr_oth_operate_a = row_data[16]
        self.spec_ocif = row_data[17]
        self.aocif = row_data[18]
        self.c_inf_fr_operate_a = row_data[19]
        self.n_inc_disbur_of_la = row_data[20]
        self.net_incr_depos_in_fi = row_data[21]
        self.orig_contr_c_indem = row_data[22]
        self.c_paid_ifc = row_data[23]
        self.c_paid_pol_div = row_data[24]
        self.c_paid_to_for_empl = row_data[25]
        self.c_paid_for_taxes = row_data[26]
        self.c_paid_for_oth_op_a = row_data[27]
        self.spec_ocof = row_data[28]
        self.aocof = row_data[29]
        self.c_outf_operate_a = row_data[30]
        self.anocf = row_data[31]
        self.n_cf_operate_a = row_data[32]
        self.proc_sell_invest = row_data[33]
        self.gain_invest = row_data[34]
        self.disp_fix_assets_oth = row_data[35]
        self.n_disp_subs_oth_biz_c = row_data[36]
        self.c_fr_oth_invest_a = row_data[37]
        self.spec_icif = row_data[38]
        self.aicif = row_data[39]
        self.c_inf_fr_invest_a = row_data[40]
        self.pur_fix_assets_oth = row_data[41]
        self.c_paid_invest = row_data[42]
        self.n_incr_pledge_loan = row_data[43]
        self.n_c_paid_acquis = row_data[44]
        self.c_paid_oth_invest_a = row_data[45]
        self.spec_icof = row_data[46]
        self.aicof = row_data[47]
        self.c_outf_fr_invest_a = row_data[48]
        self.anicf = row_data[49]
        self.n_cf_fr_invest_a = row_data[50]
        self.c_fr_cap_contr = row_data[51]
        self.c_fr_mino_s_subs = row_data[52]
        self.c_fr_borr = row_data[53]
        self.c_fr_issue_bond = row_data[54]
        self.c_fr_oth_finan_a = row_data[55]
        self.spec_fcif = row_data[56]
        self.afcif = row_data[57]
        self.c_inf_fr_finan_a = row_data[58]
        self.c_paid_for_debts = row_data[59]
        self.c_paid_div_prof_int = row_data[60]
        self.div_prof_subs_mino_s = row_data[61]
        self.c_paid_oth_finan_a = row_data[62]
        self.spec_fcof = row_data[63]
        self.afcof = row_data[64]
        self.c_outf_fr_finan_a = row_data[65]
        self.anfcf = row_data[66]
        self.n_cf_fr_finan_a = row_data[67]
        self.forex_effects = row_data[68]
        self.oth_effect_ce = row_data[69]
        self.ace = row_data[70]
        self.n_change_in_cash = row_data[71]
        self.n_ce_beg_bal = row_data[72]
        self.oth_effect_cei = row_data[73]
        self.acei = row_data[74]
        self.n_ce_end_bal = row_data[75]

    def __str__(self) -> str:
        return 'Insurance (' \
               'party_id: %s, ' \
               'ticker_symbol: %s, ' \
               'exchange_cd: %s, ' \
               'publish_date: %s, ' \
               'end_date_rep: %s, ' \
               'end_date: %s, ' \
               'report_type: %s, ' \
               'fiscal_period: %s, ' \
               'merged_flag: %s, ' \
               'n_depos_incr_c_fi: %s, ' \
               'n_incr_borr_fr_cb: %s, ' \
               'prem_fr_orig_contr: %s, ' \
               'n_reinsur_prem: %s, ' \
               'n_inc_ph_depos_inv: %s, ' \
               'ifc_cash_incr: %s, ' \
               'refund_of_tax: %s, ' \
               'c_fr_oth_operate_a: %s, ' \
               'spec_ocif: %s, ' \
               'aocif: %s, ' \
               'c_inf_fr_operate_a: %s, ' \
               'n_inc_disbur_of_la: %s, ' \
               'net_incr_depos_in_fi: %s, ' \
               'orig_contr_c_indem: %s, ' \
               'c_paid_ifc: %s, ' \
               'c_paid_pol_div: %s, ' \
               'c_paid_to_for_empl: %s, ' \
               'c_paid_for_taxes: %s, ' \
               'c_paid_for_oth_op_a: %s, ' \
               'spec_ocof: %s, ' \
               'aocof: %s, ' \
               'c_outf_operate_a: %s, ' \
               'anocf: %s, ' \
               'n_cf_operate_a: %s, ' \
               'proc_sell_invest: %s, ' \
               'gain_invest: %s, ' \
               'disp_fix_assets_oth: %s, ' \
               'n_disp_subs_oth_biz_c: %s, ' \
               'c_fr_oth_invest_a: %s, ' \
               'spec_icif: %s, ' \
               'aicif: %s, ' \
               'c_inf_fr_invest_a: %s, ' \
               'pur_fix_assets_oth: %s, ' \
               'c_paid_invest: %s, ' \
               'n_incr_pledge_loan: %s, ' \
               'n_c_paid_acquis: %s, ' \
               'c_paid_oth_invest_a: %s, ' \
               'spec_icof: %s, ' \
               'aicof: %s, ' \
               'c_outf_fr_invest_a: %s, ' \
               'anicf: %s, ' \
               'n_cf_fr_invest_a: %s, ' \
               'c_fr_cap_contr: %s, ' \
               'c_fr_mino_s_subs: %s, ' \
               'c_fr_borr: %s, ' \
               'c_fr_issue_bond: %s, ' \
               'c_fr_oth_finan_a: %s, ' \
               'spec_fcif: %s, ' \
               'afcif: %s, ' \
               'c_inf_fr_finan_a: %s, ' \
               'c_paid_for_debts: %s, ' \
               'c_paid_div_prof_int: %s, ' \
               'div_prof_subs_mino_s: %s, ' \
               'c_paid_oth_finan_a: %s, ' \
               'spec_fcof: %s, ' \
               'afcof: %s, ' \
               'c_outf_fr_finan_a: %s, ' \
               'anfcf: %s, ' \
               'n_cf_fr_finan_a: %s, ' \
               'forex_effects: %s, ' \
               'oth_effect_ce: %s, ' \
               'ace: %s, ' \
               'n_change_in_cash: %s, ' \
               'n_ce_beg_bal: %s, ' \
               'oth_effect_cei: %s, ' \
               'acei: %s, ' \
               'n_ce_end_bal: %s, ' \
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
                   self.n_depos_incr_c_fi,
                   self.n_incr_borr_fr_cb,
                   self.prem_fr_orig_contr,
                   self.n_reinsur_prem,
                   self.n_inc_ph_depos_inv,
                   self.ifc_cash_incr,
                   self.refund_of_tax,
                   self.c_fr_oth_operate_a,
                   self.spec_ocif,
                   self.aocif,
                   self.c_inf_fr_operate_a,
                   self.n_inc_disbur_of_la,
                   self.net_incr_depos_in_fi,
                   self.orig_contr_c_indem,
                   self.c_paid_ifc,
                   self.c_paid_pol_div,
                   self.c_paid_to_for_empl,
                   self.c_paid_for_taxes,
                   self.c_paid_for_oth_op_a,
                   self.spec_ocof,
                   self.aocof,
                   self.c_outf_operate_a,
                   self.anocf,
                   self.n_cf_operate_a,
                   self.proc_sell_invest,
                   self.gain_invest,
                   self.disp_fix_assets_oth,
                   self.n_disp_subs_oth_biz_c,
                   self.c_fr_oth_invest_a,
                   self.spec_icif,
                   self.aicif,
                   self.c_inf_fr_invest_a,
                   self.pur_fix_assets_oth,
                   self.c_paid_invest,
                   self.n_incr_pledge_loan,
                   self.n_c_paid_acquis,
                   self.c_paid_oth_invest_a,
                   self.spec_icof,
                   self.aicof,
                   self.c_outf_fr_invest_a,
                   self.anicf,
                   self.n_cf_fr_invest_a,
                   self.c_fr_cap_contr,
                   self.c_fr_mino_s_subs,
                   self.c_fr_borr,
                   self.c_fr_issue_bond,
                   self.c_fr_oth_finan_a,
                   self.spec_fcif,
                   self.afcif,
                   self.c_inf_fr_finan_a,
                   self.c_paid_for_debts,
                   self.c_paid_div_prof_int,
                   self.div_prof_subs_mino_s,
                   self.c_paid_oth_finan_a,
                   self.spec_fcof,
                   self.afcof,
                   self.c_outf_fr_finan_a,
                   self.anfcf,
                   self.n_cf_fr_finan_a,
                   self.forex_effects,
                   self.oth_effect_ce,
                   self.ace,
                   self.n_change_in_cash,
                   self.n_ce_beg_bal,
                   self.oth_effect_cei,
                   self.acei,
                   self.n_ce_end_bal
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
        self.n_inc_borr_oth_fi = row_data[9]
        self.n_inc_disp_trad_fa = row_data[10]
        self.n_inc_disp_fa_fs = row_data[11]
        self.ifc_cash_incr = row_data[12]
        self.n_inc_fr_borr = row_data[13]
        self.n_cap_incr_repur = row_data[14]
        self.refund_of_tax = row_data[15]
        self.c_fr_oth_operate_a = row_data[16]
        self.spec_ocif = row_data[17]
        self.aocif = row_data[18]
        self.c_inf_fr_operate_a = row_data[19]
        self.c_paid_ifc = row_data[20]
        self.c_paid_to_for_empl = row_data[21]
        self.c_paid_for_taxes = row_data[22]
        self.c_paid_for_oth_op_a = row_data[23]
        self.spec_ocof = row_data[24]
        self.aocof = row_data[25]
        self.c_outf_operate_a = row_data[26]
        self.anocf = row_data[27]
        self.n_cf_operate_a = row_data[28]
        self.proc_sell_invest = row_data[29]
        self.gain_invest = row_data[30]
        self.disp_fix_assets_oth = row_data[31]
        self.n_disp_subs_oth_biz_c = row_data[32]
        self.c_fr_oth_invest_a = row_data[33]
        self.spec_icif = row_data[34]
        self.aicif = row_data[35]
        self.c_inf_fr_invest_a = row_data[36]
        self.c_paid_invest = row_data[37]
        self.pur_fix_assets_oth = row_data[38]
        self.n_c_paid_acquis = row_data[39]
        self.c_paid_oth_invest_a = row_data[40]
        self.spec_icof = row_data[41]
        self.aicof = row_data[42]
        self.c_outf_fr_invest_a = row_data[43]
        self.anicf = row_data[44]
        self.n_cf_fr_invest_a = row_data[45]
        self.c_fr_cap_contr = row_data[46]
        self.c_fr_mino_s_subs = row_data[47]
        self.c_fr_borr = row_data[48]
        self.c_fr_issue_bond = row_data[49]
        self.c_fr_oth_finan_a = row_data[50]
        self.spec_fcif = row_data[51]
        self.afcif = row_data[52]
        self.c_inf_fr_finan_a = row_data[53]
        self.c_paid_for_debts = row_data[54]
        self.c_paid_div_prof_int = row_data[55]
        self.div_prof_subs_mino_s = row_data[56]
        self.c_paid_oth_finan_a = row_data[57]
        self.spec_fcof = row_data[58]
        self.afcof = row_data[59]
        self.c_outf_fr_finan_a = row_data[60]
        self.anfcf = row_data[61]
        self.n_cf_fr_finan_a = row_data[62]
        self.forex_effects = row_data[63]
        self.oth_effect_ce = row_data[64]
        self.ace = row_data[65]
        self.n_change_in_cash = row_data[66]
        self.n_ce_beg_bal = row_data[67]
        self.oth_effect_cei = row_data[68]
        self.acei = row_data[69]
        self.n_ce_end_bal = row_data[70]

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
               'n_inc_borr_oth_fi: %s, ' \
               'n_inc_disp_trad_fa: %s, ' \
               'n_inc_disp_fa_fs: %s, ' \
               'ifc_cash_incr: %s, ' \
               'n_inc_fr_borr: %s, ' \
               'n_cap_incr_repur: %s, ' \
               'refund_of_tax: %s, ' \
               'c_fr_oth_operate_a: %s, ' \
               'spec_ocif: %s, ' \
               'aocif: %s, ' \
               'c_inf_fr_operate_a: %s, ' \
               'c_paid_ifc: %s, ' \
               'c_paid_to_for_empl: %s, ' \
               'c_paid_for_taxes: %s, ' \
               'c_paid_for_oth_op_a: %s, ' \
               'spec_ocof: %s, ' \
               'aocof: %s, ' \
               'c_outf_operate_a: %s, ' \
               'anocf: %s, ' \
               'n_cf_operate_a: %s, ' \
               'proc_sell_invest: %s, ' \
               'gain_invest: %s, ' \
               'disp_fix_assets_oth: %s, ' \
               'n_disp_subs_oth_biz_c: %s, ' \
               'c_fr_oth_invest_a: %s, ' \
               'spec_icif: %s, ' \
               'aicif: %s, ' \
               'c_inf_fr_invest_a: %s, ' \
               'c_paid_invest: %s, ' \
               'pur_fix_assets_oth: %s, ' \
               'n_c_paid_acquis: %s, ' \
               'c_paid_oth_invest_a: %s, ' \
               'spec_icof: %s, ' \
               'aicof: %s, ' \
               'c_outf_fr_invest_a: %s, ' \
               'anicf: %s, ' \
               'n_cf_fr_invest_a: %s, ' \
               'c_fr_cap_contr: %s, ' \
               'c_fr_mino_s_subs: %s, ' \
               'c_fr_borr: %s, ' \
               'c_fr_issue_bond: %s, ' \
               'c_fr_oth_finan_a: %s, ' \
               'spec_fcif: %s, ' \
               'afcif: %s, ' \
               'c_inf_fr_finan_a: %s, ' \
               'c_paid_for_debts: %s, ' \
               'c_paid_div_prof_int: %s, ' \
               'div_prof_subs_mino_s: %s, ' \
               'c_paid_oth_finan_a: %s, ' \
               'spec_fcof: %s, ' \
               'afcof: %s, ' \
               'c_outf_fr_finan_a: %s, ' \
               'anfcf: %s, ' \
               'n_cf_fr_finan_a: %s, ' \
               'forex_effects: %s, ' \
               'oth_effect_ce: %s, ' \
               'ace: %s, ' \
               'n_change_in_cash: %s, ' \
               'n_ce_beg_bal: %s, ' \
               'oth_effect_cei: %s, ' \
               'acei: %s, ' \
               'n_ce_end_bal: %s, ' \
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
                   self.n_inc_borr_oth_fi,
                   self.n_inc_disp_trad_fa,
                   self.n_inc_disp_fa_fs,
                   self.ifc_cash_incr,
                   self.n_inc_fr_borr,
                   self.n_cap_incr_repur,
                   self.refund_of_tax,
                   self.c_fr_oth_operate_a,
                   self.spec_ocif,
                   self.aocif,
                   self.c_inf_fr_operate_a,
                   self.c_paid_ifc,
                   self.c_paid_to_for_empl,
                   self.c_paid_for_taxes,
                   self.c_paid_for_oth_op_a,
                   self.spec_ocof,
                   self.aocof,
                   self.c_outf_operate_a,
                   self.anocf,
                   self.n_cf_operate_a,
                   self.proc_sell_invest,
                   self.gain_invest,
                   self.disp_fix_assets_oth,
                   self.n_disp_subs_oth_biz_c,
                   self.c_fr_oth_invest_a,
                   self.spec_icif,
                   self.aicif,
                   self.c_inf_fr_invest_a,
                   self.c_paid_invest,
                   self.pur_fix_assets_oth,
                   self.n_c_paid_acquis,
                   self.c_paid_oth_invest_a,
                   self.spec_icof,
                   self.aicof,
                   self.c_outf_fr_invest_a,
                   self.anicf,
                   self.n_cf_fr_invest_a,
                   self.c_fr_cap_contr,
                   self.c_fr_mino_s_subs,
                   self.c_fr_borr,
                   self.c_fr_issue_bond,
                   self.c_fr_oth_finan_a,
                   self.spec_fcif,
                   self.afcif,
                   self.c_inf_fr_finan_a,
                   self.c_paid_for_debts,
                   self.c_paid_div_prof_int,
                   self.div_prof_subs_mino_s,
                   self.c_paid_oth_finan_a,
                   self.spec_fcof,
                   self.afcof,
                   self.c_outf_fr_finan_a,
                   self.anfcf,
                   self.n_cf_fr_finan_a,
                   self.forex_effects,
                   self.oth_effect_ce,
                   self.ace,
                   self.n_change_in_cash,
                   self.n_ce_beg_bal,
                   self.oth_effect_cei,
                   self.acei,
                   self.n_ce_end_bal
               )
