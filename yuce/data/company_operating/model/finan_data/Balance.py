#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: Balance.py

@time: 7/2/18 9:18 PM

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
        self.cash_c_equiv = row_data[9]
        self.sett_prov = row_data[10]
        self.loan_to_oth_bank_fi = row_data[11]
        self.deriv_assets = row_data[12]
        self.trading_fa = row_data[13]
        self.notes_peceiv = row_data[14]
        self.ar = row_data[15]
        self.prepayment = row_data[16]
        self.premium_receiv = row_data[17]
        self.reinsur_receiv = row_data[18]
        self.reinsur_reser_receiv = row_data[19]
        self.int_receiv = row_data[20]
        self.div_receiv = row_data[21]
        self.oth_receiv = row_data[22]
        self.pur_resale_fa = row_data[23]
        self.inventories = row_data[24]
        self.assets_held_for_sale = row_data[25]
        self.nca_within_1y = row_data[26]
        self.oth_ca = row_data[27]
        self.cae = row_data[28]
        self.caa = row_data[29]
        self.t_ca = row_data[30]
        self.disbur_la = row_data[31]
        self.avail_for_sale_fa = row_data[32]
        self.htm_invest = row_data[33]
        self.lt_receiv = row_data[34]
        self.lt_equity_invest = row_data[35]
        self.invest_real_estate = row_data[36]
        self.fixed_assets = row_data[37]
        self.cip = row_data[38]
        self.const_materials = row_data[39]
        self.fixed_assets_disp = row_data[40]
        self.produc_biol_assets = row_data[41]
        self.oil_and_gas_assets = row_data[42]
        self.intan_assets = row_data[43]
        self.r_d = row_data[44]
        self.goodwill = row_data[45]
        self.lt_amor_exp = row_data[46]
        self.defer_tax_assets = row_data[47]
        self.oth_nca = row_data[48]
        self.ncae = row_data[49]
        self.ncaa = row_data[50]
        self.t_nca = row_data[51]
        self.ae = row_data[52]
        self.aa = row_data[53]
        self.t_assets = row_data[54]
        self.st_borr = row_data[55]
        self.cb_borr = row_data[56]
        self.depos = row_data[57]
        self.loan_fr_oth_bank_fi = row_data[58]
        self.trading_fl = row_data[59]
        self.deriv_liab = row_data[60]
        self.notes_payable = row_data[61]
        self.ap = row_data[62]
        self.advance_receipts = row_data[63]
        self.sold_for_repur_fa = row_data[64]
        self.commis_payable = row_data[65]
        self.payroll_payable = row_data[66]
        self.taxes_payable = row_data[67]
        self.int_payable = row_data[68]
        self.div_payable = row_data[69]
        self.oth_payable = row_data[70]
        self.reinsur_payable = row_data[71]
        self.insur_reser = row_data[72]
        self.funds_sec_trad_agen = row_data[73]
        self.funds_sec_undw_agen = row_data[74]
        self.liab_held_for_sale = row_data[75]
        self.ncl_within_1y = row_data[76]
        self.accrued_exp = row_data[77]
        self.oth_cl = row_data[78]
        self.cle = row_data[79]
        self.cla = row_data[80]
        self.t_cl = row_data[81]
        self.lt_borr = row_data[82]
        self.bond_payable = row_data[83]
        self.preferred_stock_l = row_data[84]
        self.perpetual_bond_l = row_data[85]
        self.lt_payable = row_data[86]
        self.lt_payroll_payable = row_data[87]
        self.specific_payables = row_data[88]
        self.estimated_liab = row_data[89]
        self.defer_revenue = row_data[90]
        self.defer_tax_liab = row_data[91]
        self.oth_ncl = row_data[92]
        self.ncle = row_data[93]
        self.ncla = row_data[94]
        self.t_ncl = row_data[95]
        self.le = row_data[96]
        self.la = row_data[97]
        self.t_liab = row_data[98]
        self.paid_in_capital = row_data[99]
        self.oth_equity_instr = row_data[100]
        self.preferred_stock_e = row_data[101]
        self.perpetual_bond_e = row_data[102]
        self.capital_reser = row_data[103]
        self.treasury_share = row_data[104]
        self.oth_compre_income = row_data[105]
        self.special_reser = row_data[106]
        self.surplus_reser = row_data[107]
        self.ordin_risk_reser = row_data[108]
        self.retained_earnings = row_data[109]
        self.forex_differ = row_data[110]
        self.see = row_data[111]
        self.sea = row_data[112]
        self.t_equity_attr_p = row_data[113]
        self.minority_int = row_data[114]
        self.oth_effect_se = row_data[115]
        self.oth_effect_sa = row_data[116]
        self.t_sh_equity = row_data[117]
        self.lee = row_data[118]
        self.lea = row_data[119]
        self.t_liab_equity = row_data[120]


    def __str__(self) -> str:
        return 'GeneralBusiness (party_id: %s, ticker_symbol: %s, exchange_cd: %s, publish_date: %s, end_date_rep: %s, ' \
               'end_date: %s,' \
               ' report_type: %s, fiscal_period: %s, merged_flag: %s, cash_c_equiv: %s, sett_prov: %s, ' \
               'loan_to_oth_bank_fi: %s, ' \
               'deriv_assets: %s, trading_fa: %s, notes_peceiv: %s, ar: %s, prepayment: %s, premium_receiv: %s, ' \
               'reinsur_receiv: %s, reinsur_reser_receiv: %s, int_receiv: %s, div_receiv: %s, oth_receiv: %s, ' \
               'pur_resale_fa: %s, ' \
               'inventories: %s, assets_held_for_sale: %s, nca_within_1y: %s, oth_ca: %s, cae: %s, caa: %s, ' \
               't_ca: %s, disbur_la: %s, avail_for_sale_fa: %s, htm_invest: %s, lt_receiv: %s, lt_equity_invest: %s, ' \
               'invest_real_estate: %s, fixed_assets: %s, cip: %s, const_materials: %s, fixed_assets_disp: %s, ' \
               'produc_biol_assets: %s, ' \
               'oil_and_gas_assets: %s, intan_assets: %s, r_d: %s, goodwill: %s, lt_amor_exp: %s, defer_tax_assets: %s, ' \
               'oth_nca: %s, ncae: %s, ncaa: %s, t_nca: %s, ae: %s, aa: %s, ' \
               't_assets: %s, st_borr: %s, cb_borr: %s, depos: %s, loan_fr_oth_bank_fi: %s, trading_fl: %s, ' \
               'deriv_liab: %s, notes_payable: %s, ap: %s, advance_receipts: %s, sold_for_repur_fa: %s, ' \
               'commis_payable: %s, ' \
               'payroll_payable: %s, taxes_payable: %s, int_payable: %s, div_payable: %s, oth_payable: %s, ' \
               'reinsur_payable: %s, ' \
               'insur_reser: %s, funds_sec_trad_agen: %s, funds_sec_undw_agen: %s, liab_held_for_sale: %s, ' \
               'ncl_within_1y: %s, accrued_exp: %s, ' \
               'oth_cl: %s, cle: %s, cla: %s, t_cl: %s, lt_borr: %s, bond_payable: %s, ' \
               'preferred_stock_l: %s, perpetual_bond_l: %s, lt_payable: %s, lt_payroll_payable: %s, ' \
               'specific_payables: %s, estimated_liab: %s, ' \
               'defer_revenue: %s, defer_tax_liab: %s, oth_ncl: %s, ncle: %s, ncla: %s, t_ncl: %s, ' \
               'le: %s, la: %s, t_liab: %s, paid_in_capital: %s, oth_equity_instr: %s, preferred_stock_e: %s, ' \
               'perpetual_bond_e: %s, capital_reser: %s, treasury_share: %s, oth_compre_income: %s, special_reser: %s, ' \
               'surplus_reser: %s, ' \
               'ordin_risk_reser: %s, retained_earnings: %s, forex_differ: %s, see: %s, sea: %s, t_equity_attr_p: %s, ' \
               'minority_int: %s, oth_effect_se: %s, oth_effect_sa: %s, t_sh_equity: %s, lee: %s, lea: %s,' \
               't_liab_equity: %s)' % \
               (self.party_id, self.ticker_symbol, self.exchange_cd, self.publish_date, self.end_date_rep, self.end_date,
                self.report_type, self.fiscal_period, self.merged_flag, self.cash_c_equiv, self.sett_prov,
                self.loan_to_oth_bank_fi,
                self.deriv_assets, self.trading_fa, self.notes_peceiv, self.ar, self.prepayment, self.premium_receiv,
                self.reinsur_receiv, self.reinsur_reser_receiv, self.int_receiv, self.div_receiv, self.oth_receiv,
                self.pur_resale_fa,
                self.inventories, self.assets_held_for_sale, self.nca_within_1y, self.oth_ca, self.cae, self.caa,
                self.t_ca, self.disbur_la, self.avail_for_sale_fa, self.htm_invest, self.lt_receiv, self.lt_equity_invest,
                self.invest_real_estate, self.fixed_assets, self.cip, self.const_materials, self.fixed_assets_disp,
                self.produc_biol_assets,
                self.oil_and_gas_assets, self.intan_assets, self.r_d, self.goodwill, self.lt_amor_exp,
                self.defer_tax_assets,
                self.oth_nca, self.ncae, self.ncaa, self.t_nca, self.ae, self.aa,
                self.t_assets, self.st_borr, self.cb_borr, self.depos, self.loan_fr_oth_bank_fi, self.trading_fl,
                self.deriv_liab, self.notes_payable, self.ap, self.advance_receipts, self.sold_for_repur_fa,
                self.commis_payable,
                self.payroll_payable, self.taxes_payable, self.int_payable, self.div_payable, self.oth_payable,
                self.reinsur_payable,
                self.insur_reser, self.funds_sec_trad_agen, self.funds_sec_undw_agen, self.liab_held_for_sale,
                self.ncl_within_1y,
                self.accrued_exp,
                self.oth_cl, self.cle, self.cla, self.t_cl, self.lt_borr, self.bond_payable,
                self.preferred_stock_l, self.perpetual_bond_l, self.lt_payable, self.lt_payroll_payable,
                self.specific_payables,
                self.estimated_liab,
                self.defer_revenue, self.defer_tax_liab, self.oth_ncl, self.ncle, self.ncla, self.t_ncl,
                self.le, self.la, self.t_liab, self.paid_in_capital, self.oth_equity_instr, self.preferred_stock_e,
                self.perpetual_bond_e, self.capital_reser, self.treasury_share, self.oth_compre_income, self.special_reser,
                self.surplus_reser,
                self.ordin_risk_reser, self.retained_earnings, self.forex_differ, self.see, self.sea, self.t_equity_attr_p,
                self.minority_int, self.oth_effect_se, self.oth_effect_sa, self.t_sh_equity, self.lee, self.lea,
                self.t_liab_equity)


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
        self.c_reser_cb = row_data[9]
        self.depos_in_oth_bfi = row_data[10]
        self.preci_metals = row_data[11]
        self.loan_to_oth_bank_fi = row_data[12]
        self.trading_fa = row_data[13]
        self.deriv_assets = row_data[14]
        self.pur_resale_fa = row_data[15]
        self.int_receiv = row_data[16]
        self.disbur_la = row_data[17]
        self.finan_lease_receiv = row_data[18]
        self.avail_for_sale_fa = row_data[19]
        self.htm_invest = row_data[20]
        self.invest_as_receiv = row_data[21]
        self.lt_equity_invest = row_data[22]
        self.invest_real_estate = row_data[23]
        self.fixed_assets = row_data[24]
        self.cip = row_data[25]
        self.intan_assets = row_data[26]
        self.goodwill = row_data[27]
        self.defer_tax_assets = row_data[28]
        self.oth_assets = row_data[29]
        self.ae = row_data[30]
        self.aa = row_data[31]
        self.t_assets = row_data[32]
        self.cb_borr = row_data[33]
        self.depos_fr_oth_bfi = row_data[34]
        self.loan_fr_oth_bank_fi = row_data[35]
        self.trading_fl = row_data[36]
        self.deriv_liab = row_data[37]
        self.sold_for_repur_fa = row_data[38]
        self.depos = row_data[39]
        self.payroll_payable = row_data[40]
        self.taxes_payable = row_data[41]
        self.int_payable = row_data[42]
        self.estimated_liab = row_data[43]
        self.bond_payable = row_data[44]
        self.preferred_stock_l = row_data[45]
        self.perpetual_bond_l = row_data[46]
        self.defer_tax_liab = row_data[47]
        self.oth_liab = row_data[48]
        self.le = row_data[49]
        self.la = row_data[50]
        self.t_liab = row_data[51]
        self.paid_in_capital = row_data[52]
        self.oth_equity_instr = row_data[53]
        self.preferred_stock_e = row_data[54]
        self.perpetual_bond_e = row_data[55]
        self.capital_reser = row_data[56]
        self.treasury_share = row_data[57]
        self.oth_compre_income = row_data[58]
        self.surplus_reser = row_data[59]
        self.ordin_risk_reser = row_data[60]
        self.retained_earnings = row_data[61]
        self.forex_differ = row_data[62]
        self.see = row_data[63]
        self.sea = row_data[64]
        self.t_equity_attr_p = row_data[65]
        self.minority_int = row_data[66]
        self.oth_effect_se = row_data[67]
        self.oth_effect_sa = row_data[68]
        self.t_sh_equity = row_data[69]
        self.lee = row_data[70]
        self.lea = row_data[71]
        self.t_liab_equity = row_data[72]

    def __str__(self) -> str:
        return 'Bank (party_id: %s,' \
               'ticker_symbol: %s,' \
               'exchange_cd: %s,' \
               'publish_date: %s,' \
               'end_date_rep: %s,' \
               'end_date: %s,' \
               'report_type: %s,' \
               'fiscal_period: %s,' \
               'merged_flag: %s,' \
               'c_reser_cb: %s,' \
               'depos_in_oth_bfi: %s,' \
               'preci_metals: %s,' \
               'loan_to_oth_bank_fi: %s,' \
               'trading_fa: %s,' \
               'deriv_assets: %s,' \
               'pur_resale_fa: %s,' \
               'int_receiv: %s,' \
               'disbur_la: %s,' \
               'finan_lease_receiv: %s,' \
               'avail_for_sale_fa: %s,' \
               'htm_invest: %s,' \
               'invest_as_receiv: %s,' \
               'lt_equity_invest: %s,' \
               'invest_real_estate: %s,' \
               'fixed_assets: %s,' \
               'cip: %s,' \
               'intan_assets: %s,' \
               'goodwill: %s,' \
               'defer_tax_assets: %s,' \
               'oth_assets: %s,' \
               'ae: %s,' \
               'aa: %s,' \
               't_assets: %s,' \
               'cb_borr: %s,' \
               'depos_fr_oth_bfi: %s,' \
               'loan_fr_oth_bank_fi: %s,' \
               'trading_fl: %s,' \
               'deriv_liab: %s,' \
               'sold_for_repur_fa: %s,' \
               'depos: %s,' \
               'payroll_payable: %s,' \
               'taxes_payable: %s,' \
               'int_payable: %s,' \
               'estimated_liab: %s,' \
               'bond_payable: %s,' \
               'preferred_stock_l: %s,' \
               'perpetual_bond_l: %s,' \
               'defer_tax_liab: %s,' \
               'oth_liab: %s,' \
               'le: %s,' \
               'la: %s,' \
               't_liab: %s,' \
               'paid_in_capital: %s,' \
               'oth_equity_instr: %s,' \
               'preferred_stock_e: %s,' \
               'perpetual_bond_e: %s,' \
               'capital_reser: %s,' \
               'treasury_share: %s,' \
               'oth_compre_income: %s,' \
               'surplus_reser: %s,' \
               'ordin_risk_reser: %s,' \
               'retained_earnings: %s,' \
               'forex_differ: %s,' \
               'see: %s,' \
               'sea: %s,' \
               't_equity_attr_p: %s,' \
               'minority_int: %s,' \
               'oth_effect_se: %s,' \
               'oth_effect_sa: %s,' \
               't_sh_equity: %s,' \
               'lee: %s,' \
               'lea: %s,' \
               't_liab_equity: %s)' % \
               (self.party_id,
                self.ticker_symbol,
                self.exchange_cd,
                self.publish_date,
                self.end_date_rep,
                self.end_date,
                self.report_type,
                self.fiscal_period,
                self.merged_flag,
                self.c_reser_cb,
                self.depos_in_oth_bfi,
                self.preci_metals,
                self.loan_to_oth_bank_fi,
                self.trading_fa,
                self.deriv_assets,
                self.pur_resale_fa,
                self.int_receiv,
                self.disbur_la,
                self.finan_lease_receiv,
                self.avail_for_sale_fa,
                self.htm_invest,
                self.invest_as_receiv,
                self.lt_equity_invest,
                self.invest_real_estate,
                self.fixed_assets,
                self.cip,
                self.intan_assets,
                self.goodwill,
                self.defer_tax_assets,
                self.oth_assets,
                self.ae,
                self.aa,
                self.t_assets,
                self.cb_borr,
                self.depos_fr_oth_bfi,
                self.loan_fr_oth_bank_fi,
                self.trading_fl,
                self.deriv_liab,
                self.sold_for_repur_fa,
                self.depos,
                self.payroll_payable,
                self.taxes_payable,
                self.int_payable,
                self.estimated_liab,
                self.bond_payable,
                self.preferred_stock_l,
                self.perpetual_bond_l,
                self.defer_tax_liab,
                self.oth_liab,
                self.le,
                self.la,
                self.t_liab,
                self.paid_in_capital,
                self.oth_equity_instr,
                self.preferred_stock_e,
                self.perpetual_bond_e,
                self.capital_reser,
                self.treasury_share,
                self.oth_compre_income,
                self.surplus_reser,
                self.ordin_risk_reser,
                self.retained_earnings,
                self.forex_differ,
                self.see,
                self.sea,
                self.t_equity_attr_p,
                self.minority_int,
                self.oth_effect_se,
                self.oth_effect_sa,
                self.t_sh_equity,
                self.lee,
                self.lea,
                self.t_liab_equity)


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
        self.cash_c_equiv = row_data[9]
        self.loan_to_oth_bank_fi = row_data[10]
        self.trading_fa = row_data[11]
        self.deriv_assets = row_data[12]
        self.pur_resale_fa = row_data[13]
        self.int_receiv = row_data[14]
        self.premium_receiv = row_data[15]
        self.subrog_reco_receiv = row_data[16]
        self.reinsur_receiv = row_data[17]
        self.rr_reins_une_prem = row_data[18]
        self.rr_reins_outstd_cla = row_data[19]
        self.rr_reins_lins_liab = row_data[20]
        self.rr_reins_lthins_liab = row_data[21]
        self.ph_pledge_loans = row_data[22]
        self.fixed_term_depos = row_data[23]
        self.avail_for_sale_fa = row_data[24]
        self.htm_invest = row_data[25]
        self.lt_equity_invest = row_data[26]
        self.refund_cap_depos = row_data[27]
        self.invest_real_estate = row_data[28]
        self.fixed_assets = row_data[29]
        self.intan_assets = row_data[30]
        self.indep_acc_assets = row_data[31]
        self.defer_tax_assets = row_data[32]
        self.oth_assets = row_data[33]
        self.ae = row_data[34]
        self.aa = row_data[35]
        self.t_assets = row_data[36]
        self.st_borr = row_data[37]
        self.loan_fr_oth_bank_fi = row_data[38]
        self.trading_fl = row_data[39]
        self.deriv_liab = row_data[40]
        self.sold_for_repur_fa = row_data[41]
        self.prem_receiv_adva = row_data[42]
        self.commis_payable = row_data[43]
        self.reinsur_payable = row_data[44]
        self.payroll_payable = row_data[45]
        self.taxes_payable = row_data[46]
        self.indem_acc_payable = row_data[47]
        self.policy_div_payable = row_data[48]
        self.ph_invest = row_data[49]
        self.reser_une_prem = row_data[50]
        self.reser_outstd_claims = row_data[51]
        self.reser_lins_liab = row_data[52]
        self.reser_lthins_liab = row_data[53]
        self.lt_borr = row_data[54]
        self.bond_payable = row_data[55]
        self.preferred_stock_l = row_data[56]
        self.perpetual_bond_l = row_data[57]
        self.indept_acc_liab = row_data[58]
        self.defer_tax_liab = row_data[59]
        self.oth_liab = row_data[60]
        self.le = row_data[61]
        self.la = row_data[62]
        self.t_liab = row_data[63]
        self.paid_in_capital = row_data[64]
        self.oth_equity_instr = row_data[65]
        self.preferred_stock_e = row_data[66]
        self.perpetual_bond_e = row_data[67]
        self.capital_reser = row_data[68]
        self.treasury_share = row_data[69]
        self.oth_compre_income = row_data[70]
        self.surplus_reser = row_data[71]
        self.ordin_risk_reser = row_data[72]
        self.retained_earnings = row_data[73]
        self.forex_differ = row_data[74]
        self.see = row_data[75]
        self.sea = row_data[76]
        self.t_equity_attr_p = row_data[77]
        self.minority_int = row_data[78]
        self.oth_effect_se = row_data[79]
        self.oth_effect_sa = row_data[80]
        self.t_sh_equity = row_data[81]
        self.lee = row_data[82]
        self.lea = row_data[83]
        self.t_liab_equity = row_data[84]

    def __str__(self) -> str:
        return 'Insurance (party_id: %s,' \
               'ticker_symbol: %s,' \
               'exchange_cd: %s,' \
               'publish_date: %s,' \
               'end_date_rep: %s,' \
               'end_date: %s,' \
               'report_type: %s,' \
               'fiscal_period: %s,' \
               'merged_flag: %s,' \
               'cash_c_equiv: %s,' \
               'loan_to_oth_bank_fi: %s,' \
               'trading_fa: %s,' \
               'deriv_assets: %s,' \
               'pur_resale_fa: %s,' \
               'int_receiv: %s,' \
               'premium_receiv: %s,' \
               'subrog_reco_receiv: %s,' \
               'reinsur_receiv: %s,' \
               'rr_reins_une_prem: %s,' \
               'rr_reins_outstd_cla: %s,' \
               'rr_reins_lins_liab: %s,' \
               'rr_reins_lthins_liab: %s,' \
               'ph_pledge_loans: %s,' \
               'fixed_term_depos: %s,' \
               'avail_for_sale_fa: %s,' \
               'htm_invest: %s,' \
               'lt_equity_invest: %s,' \
               'refund_cap_depos: %s,' \
               'invest_real_estate: %s,' \
               'fixed_assets: %s,' \
               'intan_assets: %s,' \
               'indep_acc_assets: %s,' \
               'defer_tax_assets: %s,' \
               'oth_assets: %s,' \
               'ae: %s,' \
               'aa: %s,' \
               't_assets: %s,' \
               'st_borr: %s,' \
               'loan_fr_oth_bank_fi: %s,' \
               'trading_fl: %s,' \
               'deriv_liab: %s,' \
               'sold_for_repur_fa: %s,' \
               'prem_receiv_adva: %s,' \
               'commis_payable: %s,' \
               'reinsur_payable: %s,' \
               'payroll_payable: %s,' \
               'taxes_payable: %s,' \
               'indem_acc_payable: %s,' \
               'policy_div_payable: %s,' \
               'ph_invest: %s,' \
               'reser_une_prem: %s,' \
               'reser_outstd_claims: %s,' \
               'reser_lins_liab: %s,' \
               'reser_lthins_liab: %s,' \
               'lt_borr: %s,' \
               'bond_payable: %s,' \
               'preferred_stock_l: %s,' \
               'perpetual_bond_l: %s,' \
               'indept_acc_liab: %s,' \
               'defer_tax_liab: %s,' \
               'oth_liab: %s,' \
               'le: %s,' \
               'la: %s,' \
               't_liab: %s,' \
               'paid_in_capital: %s,' \
               'oth_equity_instr: %s,' \
               'preferred_stock_e: %s,' \
               'perpetual_bond_e: %s,' \
               'capital_reser: %s,' \
               'treasury_share: %s,' \
               'oth_compre_income: %s,' \
               'surplus_reser: %s,' \
               'ordin_risk_reser: %s,' \
               'retained_earnings: %s,' \
               'forex_differ: %s,' \
               'see: %s,' \
               'sea: %s,' \
               't_equity_attr_p: %s,' \
               'minority_int: %s,' \
               'oth_effect_se: %s,' \
               'oth_effect_sa: %s,' \
               't_sh_equity: %s,' \
               'lee: %s,' \
               'lea: %s,' \
               't_liab_equity: %s)' % \
               (self.party_id,
                self.ticker_symbol,
                self.exchange_cd,
                self.publish_date,
                self.end_date_rep,
                self.end_date,
                self.report_type,
                self.fiscal_period,
                self.merged_flag,
                self.cash_c_equiv,
                self.loan_to_oth_bank_fi,
                self.trading_fa,
                self.deriv_assets,
                self.pur_resale_fa,
                self.int_receiv,
                self.premium_receiv,
                self.subrog_reco_receiv,
                self.reinsur_receiv,
                self.rr_reins_une_prem,
                self.rr_reins_outstd_cla,
                self.rr_reins_lins_liab,
                self.rr_reins_lthins_liab,
                self.ph_pledge_loans,
                self.fixed_term_depos,
                self.avail_for_sale_fa,
                self.htm_invest,
                self.lt_equity_invest,
                self.refund_cap_depos,
                self.invest_real_estate,
                self.fixed_assets,
                self.intan_assets,
                self.indep_acc_assets,
                self.defer_tax_assets,
                self.oth_assets,
                self.ae,
                self.aa,
                self.t_assets,
                self.st_borr,
                self.loan_fr_oth_bank_fi,
                self.trading_fl,
                self.deriv_liab,
                self.sold_for_repur_fa,
                self.prem_receiv_adva,
                self.commis_payable,
                self.reinsur_payable,
                self.payroll_payable,
                self.taxes_payable,
                self.indem_acc_payable,
                self.policy_div_payable,
                self.ph_invest,
                self.reser_une_prem,
                self.reser_outstd_claims,
                self.reser_lins_liab,
                self.reser_lthins_liab,
                self.lt_borr,
                self.bond_payable,
                self.preferred_stock_l,
                self.perpetual_bond_l,
                self.indept_acc_liab,
                self.defer_tax_liab,
                self.oth_liab,
                self.le,
                self.la,
                self.t_liab,
                self.paid_in_capital,
                self.oth_equity_instr,
                self.preferred_stock_e,
                self.perpetual_bond_e,
                self.capital_reser,
                self.treasury_share,
                self.oth_compre_income,
                self.surplus_reser,
                self.ordin_risk_reser,
                self.retained_earnings,
                self.forex_differ,
                self.see,
                self.sea,
                self.t_equity_attr_p,
                self.minority_int,
                self.oth_effect_se,
                self.oth_effect_sa,
                self.t_sh_equity,
                self.lee,
                self.lea,
                self.t_liab_equity)


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
        self.cash_c_equiv = row_data[9]
        self.client_depos = row_data[10]
        self.sett_prov = row_data[11]
        self.client_prov = row_data[12]
        self.loan_to_oth_bank_fi = row_data[13]
        self.trading_fa = row_data[14]
        self.deriv_assets = row_data[15]
        self.pur_resale_fa = row_data[16]
        self.int_receiv = row_data[17]
        self.refund_depos = row_data[18]
        self.avail_for_sale_fa = row_data[19]
        self.htm_invest = row_data[20]
        self.lt_equity_invest = row_data[21]
        self.invest_real_estate = row_data[22]
        self.fixed_assets = row_data[23]
        self.intan_assets = row_data[24]
        self.transac_seat_fee = row_data[25]
        self.defer_tax_assets = row_data[26]
        self.oth_assets = row_data[27]
        self.ae = row_data[28]
        self.aa = row_data[29]
        self.t_assets = row_data[30]
        self.st_borr = row_data[31]
        self.pledge_borr = row_data[32]
        self.loan_fr_oth_bank_fi = row_data[33]
        self.trading_fl = row_data[34]
        self.deriv_liab = row_data[35]
        self.sold_for_repur_fa = row_data[36]
        self.funds_sec_trad_agen = row_data[37]
        self.funds_sec_undw_agen = row_data[38]
        self.payroll_payable = row_data[39]
        self.taxes_payable = row_data[40]
        self.int_payable = row_data[41]
        self.estimated_liab = row_data[42]
        self.lt_borr = row_data[43]
        self.bond_payable = row_data[44]
        self.preferred_stock_l = row_data[45]
        self.perpetual_bond_l = row_data[46]
        self.defer_tax_liab = row_data[47]
        self.oth_liab = row_data[48]
        self.le = row_data[49]
        self.la = row_data[50]
        self.t_liab = row_data[51]
        self.paid_in_capital = row_data[52]
        self.oth_equity_instr = row_data[53]
        self.preferred_stock_e = row_data[54]
        self.perpetual_bond_e = row_data[55]
        self.capital_reser = row_data[56]
        self.treasury_share = row_data[57]
        self.oth_compre_income = row_data[58]
        self.surplus_reser = row_data[59]
        self.ordin_risk_reser = row_data[60]
        self.transac_risk_reser = row_data[61]
        self.retained_earnings = row_data[62]
        self.forex_differ = row_data[63]
        self.see = row_data[64]
        self.sea = row_data[65]
        self.t_equity_attr_p = row_data[66]
        self.minority_int = row_data[67]
        self.oth_effect_se = row_data[68]
        self.oth_effect_sa = row_data[69]
        self.t_sh_equity = row_data[70]
        self.lee = row_data[71]
        self.lea = row_data[72]
        self.t_liab_equity = row_data[73]

    def __str__(self) -> str:
        return 'Securities (party_id:%s ,' \
               'ticker_symbol:%s,' \
               'exchange_cd:%s,' \
               'publish_date:%s,' \
               'end_date_rep:%s,' \
               'end_date:%s,' \
               'report_type:%s,' \
               'fiscal_period:%s,' \
               'merged_flag:%s,' \
               'cash_c_equiv:%s,' \
               'client_depos:%s,' \
               'sett_prov:%s,' \
               'client_prov:%s,' \
               'loan_to_oth_bank_fi:%s,' \
               'trading_fa:%s,' \
               'deriv_assets:%s,' \
               'pur_resale_fa:%s,' \
               'int_receiv:%s,' \
               'refund_depos:%s,' \
               'avail_for_sale_fa:%s,' \
               'htm_invest:%s,' \
               'lt_equity_invest:%s,' \
               'invest_real_estate:%s,' \
               'fixed_assets:%s,' \
               'intan_assets:%s,' \
               'transac_seat_fee:%s,' \
               'defer_tax_assets:%s,' \
               'oth_assets:%s,' \
               'ae:%s,' \
               'aa:%s,' \
               't_assets:%s,' \
               'st_borr:%s,' \
               'pledge_borr:%s,' \
               'loan_fr_oth_bank_fi:%s,' \
               'trading_fl:%s,' \
               'deriv_liab:%s,' \
               'sold_for_repur_fa:%s,' \
               'funds_sec_trad_agen:%s,' \
               'funds_sec_undw_agen:%s,' \
               'payroll_payable:%s,' \
               'taxes_payable:%s,' \
               'int_payable:%s,' \
               'estimated_liab:%s,' \
               'lt_borr:%s,' \
               'bond_payable:%s,' \
               'preferred_stock_l:%s,' \
               'perpetual_bond_l:%s,' \
               'defer_tax_liab:%s,' \
               'oth_liab:%s,' \
               'le:%s,' \
               'la:%s,' \
               't_liab:%s,' \
               'paid_in_capital:%s,' \
               'oth_equity_instr:%s,' \
               'preferred_stock_e:%s,' \
               'perpetual_bond_e:%s,' \
               'capital_reser:%s,' \
               'treasury_share:%s,' \
               'oth_compre_income:%s,' \
               'surplus_reser:%s,' \
               'ordin_risk_reser:%s,' \
               'transac_risk_reser:%s,' \
               'retained_earnings:%s,' \
               'forex_differ:%s,' \
               'see:%s,' \
               'sea:%s,' \
               't_equity_attr_p:%s,' \
               'minority_int:%s,' \
               'oth_effect_se:%s,' \
               'oth_effect_sa:%s,' \
               't_sh_equity:%s,' \
               'lee:%s,' \
               'lea:%s,' \
               't_liab_equity:%s)' % \
               (self.party_id,
                self.ticker_symbol,
                self.exchange_cd,
                self.publish_date,
                self.end_date_rep,
                self.end_date,
                self.report_type,
                self.fiscal_period,
                self.merged_flag,
                self.cash_c_equiv,
                self.client_depos,
                self.sett_prov,
                self.client_prov,
                self.loan_to_oth_bank_fi,
                self.trading_fa,
                self.deriv_assets,
                self.pur_resale_fa,
                self.int_receiv,
                self.refund_depos,
                self.avail_for_sale_fa,
                self.htm_invest,
                self.lt_equity_invest,
                self.invest_real_estate,
                self.fixed_assets,
                self.intan_assets,
                self.transac_seat_fee,
                self.defer_tax_assets,
                self.oth_assets,
                self.ae,
                self.aa,
                self.t_assets,
                self.st_borr,
                self.pledge_borr,
                self.loan_fr_oth_bank_fi,
                self.trading_fl,
                self.deriv_liab,
                self.sold_for_repur_fa,
                self.funds_sec_trad_agen,
                self.funds_sec_undw_agen,
                self.payroll_payable,
                self.taxes_payable,
                self.int_payable,
                self.estimated_liab,
                self.lt_borr,
                self.bond_payable,
                self.preferred_stock_l,
                self.perpetual_bond_l,
                self.defer_tax_liab,
                self.oth_liab,
                self.le,
                self.la,
                self.t_liab,
                self.paid_in_capital,
                self.oth_equity_instr,
                self.preferred_stock_e,
                self.perpetual_bond_e,
                self.capital_reser,
                self.treasury_share,
                self.oth_compre_income,
                self.surplus_reser,
                self.ordin_risk_reser,
                self.transac_risk_reser,
                self.retained_earnings,
                self.forex_differ,
                self.see,
                self.sea,
                self.t_equity_attr_p,
                self.minority_int,
                self.oth_effect_se,
                self.oth_effect_sa,
                self.t_sh_equity,
                self.lee,
                self.lea,
                self.t_liab_equity)
