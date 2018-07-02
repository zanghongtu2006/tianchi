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

    def __init__(self, party_id, ticker_symbol, exchange_cd, publish_date, end_date_rep, end_date,
                 report_type, fiscal_period, merged_flag, cash_c_equiv, sett_prov, loan_to_oth_bank_fi,
                 deriv_assets, trading_fa, notes_peceiv, ar, prepayment, premium_receiv,
                 reinsur_receiv, reinsur_reser_receiv, int_receiv, div_receiv, oth_receiv, pur_resale_fa,
                 inventories, assets_held_for_sale, nca_within_1y, oth_ca, cae, caa,
                 t_ca, disbur_la, avail_for_sale_fa, htm_invest, lt_receiv, lt_equity_invest,
                 invest_real_estate, fixed_assets, cip, const_materials, fixed_assets_disp, produc_biol_assets,
                 oil_and_gas_assets, intan_assets, r_d, goodwill, lt_amor_exp, defer_tax_assets,
                 oth_nca, ncae, ncaa, t_nca, ae, aa,
                 t_assets, st_borr, cb_borr, depos, loan_fr_oth_bank_fi, trading_fl,
                 deriv_liab, notes_payable, ap, advance_receipts, sold_for_repur_fa, commis_payable,
                 payroll_payable, taxes_payable, int_payable, div_payable, oth_payable, reinsur_payable,
                 insur_reser, funds_sec_trad_agen, funds_sec_undw_agen, liab_held_for_sale, ncl_within_1y, accrued_exp,
                 oth_cl, cle, cla, t_cl, lt_borr, bond_payable,
                 preferred_stock_l, perpetual_bond_l, lt_payable, lt_payroll_payable, specific_payables, estimated_liab,
                 defer_revenue, defer_tax_liab, oth_ncl, ncle, ncla, t_ncl,
                 le, la, t_liab, paid_in_capital, oth_equity_instr, preferred_stock_e,
                 perpetual_bond_e, capital_reser, treasury_share, oth_compre_income, special_reser, surplus_reser,
                 ordin_risk_reser, retained_earnings, forex_differ, see, sea, t_equity_attr_p,
                 minority_int, oth_effect_se, oth_effect_sa, t_sh_equity, lee, lea,
                 t_liab_equity) -> None:
        self.party_id = party_id
        self.ticker_symbol = ticker_symbol
        self.exchange_cd = exchange_cd
        self.publish_date = publish_date
        self.end_date_rep = end_date_rep
        self.end_date = end_date
        self.report_type = report_type
        self.fiscal_period = fiscal_period
        self.merged_flag = merged_flag
        self.cash_c_equiv = cash_c_equiv
        self.sett_prov = sett_prov
        self.loan_to_oth_bank_fi = loan_to_oth_bank_fi
        self.deriv_assets = deriv_assets
        self.trading_fa = trading_fa
        self.notes_peceiv = notes_peceiv
        self.ar = ar
        self.prepayment = prepayment
        self.premium_receiv = premium_receiv
        self.reinsur_receiv = reinsur_receiv
        self.reinsur_reser_receiv = reinsur_reser_receiv
        self.int_receiv = int_receiv
        self.div_receiv = div_receiv
        self.oth_receiv = oth_receiv
        self.pur_resale_fa = pur_resale_fa
        self.inventories = inventories
        self.assets_held_for_sale = assets_held_for_sale
        self.nca_within_1y = nca_within_1y
        self.oth_ca = oth_ca
        self.cae = cae
        self.caa = caa
        self.t_ca = t_ca
        self.disbur_la = disbur_la
        self.avail_for_sale_fa = avail_for_sale_fa
        self.htm_invest = htm_invest
        self.lt_receiv = lt_receiv
        self.lt_equity_invest = lt_equity_invest
        self.invest_real_estate = invest_real_estate
        self.fixed_assets = fixed_assets
        self.cip = cip
        self.const_materials = const_materials
        self.fixed_assets_disp = fixed_assets_disp
        self.produc_biol_assets = produc_biol_assets
        self.oil_and_gas_assets = oil_and_gas_assets
        self.intan_assets = intan_assets
        self.r_d = r_d
        self.goodwill = goodwill
        self.lt_amor_exp = lt_amor_exp
        self.defer_tax_assets = defer_tax_assets
        self.oth_nca = oth_nca
        self.ncae = ncae
        self.ncaa = ncaa
        self.t_nca = t_nca
        self.ae = ae
        self.aa = aa
        self.t_assets = t_assets
        self.st_borr = st_borr
        self.cb_borr = cb_borr
        self.depos = depos
        self.loan_fr_oth_bank_fi = loan_fr_oth_bank_fi
        self.trading_fl = trading_fl
        self.deriv_liab = deriv_liab
        self.notes_payable = notes_payable
        self.ap = ap
        self.advance_receipts = advance_receipts
        self.sold_for_repur_fa = sold_for_repur_fa
        self.commis_payable = commis_payable
        self.payroll_payable = payroll_payable
        self.taxes_payable = taxes_payable
        self.int_payable = int_payable
        self.div_payable = div_payable
        self.oth_payable = oth_payable
        self.reinsur_payable = reinsur_payable
        self.insur_reser = insur_reser
        self.funds_sec_trad_agen = funds_sec_trad_agen
        self.funds_sec_undw_agen = funds_sec_undw_agen
        self.liab_held_for_sale = liab_held_for_sale
        self.ncl_within_1y = ncl_within_1y
        self.accrued_exp = accrued_exp
        self.oth_cl = oth_cl
        self.cle = cle
        self.cla = cla
        self.t_cl = t_cl
        self.lt_borr = lt_borr
        self.bond_payable = bond_payable
        self.preferred_stock_l = preferred_stock_l
        self.perpetual_bond_l = perpetual_bond_l
        self.lt_payable = lt_payable
        self.lt_payroll_payable = lt_payroll_payable
        self.specific_payables = specific_payables
        self.estimated_liab = estimated_liab
        self.defer_revenue = defer_revenue
        self.defer_tax_liab = defer_tax_liab
        self.oth_ncl = oth_ncl
        self.ncle = ncle
        self.ncla = ncla
        self.t_ncl = t_ncl
        self.le = le
        self.la = la
        self.t_liab = t_liab
        self.paid_in_capital = paid_in_capital
        self.oth_equity_instr = oth_equity_instr
        self.preferred_stock_e = preferred_stock_e
        self.perpetual_bond_e = perpetual_bond_e
        self.capital_reser = capital_reser
        self.treasury_share = treasury_share
        self.oth_compre_income = oth_compre_income
        self.special_reser = special_reser
        self.surplus_reser = surplus_reser
        self.ordin_risk_reser = ordin_risk_reser
        self.retained_earnings = retained_earnings
        self.forex_differ = forex_differ
        self.see = see
        self.sea = sea
        self.t_equity_attr_p = t_equity_attr_p
        self.minority_int = minority_int
        self.oth_effect_se = oth_effect_se
        self.oth_effect_sa = oth_effect_sa
        self.t_sh_equity = t_sh_equity
        self.lee = lee
        self.lea = lea
        self.t_liab_equity = t_liab_equity


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
    def __init__(self, party_id,
                 ticker_symbol,
                 exchange_cd,
                 publish_date,
                 end_date_rep,
                 end_date,
                 report_type,
                 fiscal_period,
                 merged_flag,
                 c_reser_cb,
                 depos_in_oth_bfi,
                 preci_metals,
                 loan_to_oth_bank_fi,
                 trading_fa,
                 deriv_assets,
                 pur_resale_fa,
                 int_receiv,
                 disbur_la,
                 finan_lease_receiv,
                 avail_for_sale_fa,
                 htm_invest,
                 invest_as_receiv,
                 lt_equity_invest,
                 invest_real_estate,
                 fixed_assets,
                 cip,
                 intan_assets,
                 goodwill,
                 defer_tax_assets,
                 oth_assets,
                 ae,
                 aa,
                 t_assets,
                 cb_borr,
                 depos_fr_oth_bfi,
                 loan_fr_oth_bank_fi,
                 trading_fl,
                 deriv_liab,
                 sold_for_repur_fa,
                 depos,
                 payroll_payable,
                 taxes_payable,
                 int_payable,
                 estimated_liab,
                 bond_payable,
                 preferred_stock_l,
                 perpetual_bond_l,
                 defer_tax_liab,
                 oth_liab,
                 le,
                 la,
                 t_liab,
                 paid_in_capital,
                 oth_equity_instr,
                 preferred_stock_e,
                 perpetual_bond_e,
                 capital_reser,
                 treasury_share,
                 oth_compre_income,
                 surplus_reser,
                 ordin_risk_reser,
                 retained_earnings,
                 forex_differ,
                 see,
                 sea,
                 t_equity_attr_p,
                 minority_int,
                 oth_effect_se,
                 oth_effect_sa,
                 t_sh_equity,
                 lee,
                 lea,
                 t_liab_equity) -> None:
        self.party_id = party_id
        self.ticker_symbol = ticker_symbol
        self.exchange_cd = exchange_cd
        self.publish_date = publish_date
        self.end_date_rep = end_date_rep
        self.end_date = end_date
        self.report_type = report_type
        self.fiscal_period = fiscal_period
        self.merged_flag = merged_flag
        self.c_reser_cb = c_reser_cb
        self.depos_in_oth_bfi = depos_in_oth_bfi
        self.preci_metals = preci_metals
        self.loan_to_oth_bank_fi = loan_to_oth_bank_fi
        self.trading_fa = trading_fa
        self.deriv_assets = deriv_assets
        self.pur_resale_fa = pur_resale_fa
        self.int_receiv = int_receiv
        self.disbur_la = disbur_la
        self.finan_lease_receiv = finan_lease_receiv
        self.avail_for_sale_fa = avail_for_sale_fa
        self.htm_invest = htm_invest
        self.invest_as_receiv = invest_as_receiv
        self.lt_equity_invest = lt_equity_invest
        self.invest_real_estate = invest_real_estate
        self.fixed_assets = fixed_assets
        self.cip = cip
        self.intan_assets = intan_assets
        self.goodwill = goodwill
        self.defer_tax_assets = defer_tax_assets
        self.oth_assets = oth_assets
        self.ae = ae
        self.aa = aa
        self.t_assets = t_assets
        self.cb_borr = cb_borr
        self.depos_fr_oth_bfi = depos_fr_oth_bfi
        self.loan_fr_oth_bank_fi = loan_fr_oth_bank_fi
        self.trading_fl = trading_fl
        self.deriv_liab = deriv_liab
        self.sold_for_repur_fa = sold_for_repur_fa
        self.depos = depos
        self.payroll_payable = payroll_payable
        self.taxes_payable = taxes_payable
        self.int_payable = int_payable
        self.estimated_liab = estimated_liab
        self.bond_payable = bond_payable
        self.preferred_stock_l = preferred_stock_l
        self.perpetual_bond_l = perpetual_bond_l
        self.defer_tax_liab = defer_tax_liab
        self.oth_liab = oth_liab
        self.le = le
        self.la = la
        self.t_liab = t_liab
        self.paid_in_capital = paid_in_capital
        self.oth_equity_instr = oth_equity_instr
        self.preferred_stock_e = preferred_stock_e
        self.perpetual_bond_e = perpetual_bond_e
        self.capital_reser = capital_reser
        self.treasury_share = treasury_share
        self.oth_compre_income = oth_compre_income
        self.surplus_reser = surplus_reser
        self.ordin_risk_reser = ordin_risk_reser
        self.retained_earnings = retained_earnings
        self.forex_differ = forex_differ
        self.see = see
        self.sea = sea
        self.t_equity_attr_p = t_equity_attr_p
        self.minority_int = minority_int
        self.oth_effect_se = oth_effect_se
        self.oth_effect_sa = oth_effect_sa
        self.t_sh_equity = t_sh_equity
        self.lee = lee
        self.lea = lea
        self.t_liab_equity = t_liab_equity

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

    def __init__(self, party_id,
                 ticker_symbol,
                 exchange_cd,
                 publish_date,
                 end_date_rep,
                 end_date,
                 report_type,
                 fiscal_period,
                 merged_flag,
                 cash_c_equiv,
                 loan_to_oth_bank_fi,
                 trading_fa,
                 deriv_assets,
                 pur_resale_fa,
                 int_receiv,
                 premium_receiv,
                 subrog_reco_receiv,
                 reinsur_receiv,
                 rr_reins_une_prem,
                 rr_reins_outstd_cla,
                 rr_reins_lins_liab,
                 rr_reins_lthins_liab,
                 ph_pledge_loans,
                 fixed_term_depos,
                 avail_for_sale_fa,
                 htm_invest,
                 lt_equity_invest,
                 refund_cap_depos,
                 invest_real_estate,
                 fixed_assets,
                 intan_assets,
                 indep_acc_assets,
                 defer_tax_assets,
                 oth_assets,
                 ae,
                 aa,
                 t_assets,
                 st_borr,
                 loan_fr_oth_bank_fi,
                 trading_fl,
                 deriv_liab,
                 sold_for_repur_fa,
                 prem_receiv_adva,
                 commis_payable,
                 reinsur_payable,
                 payroll_payable,
                 taxes_payable,
                 indem_acc_payable,
                 policy_div_payable,
                 ph_invest,
                 reser_une_prem,
                 reser_outstd_claims,
                 reser_lins_liab,
                 reser_lthins_liab,
                 lt_borr,
                 bond_payable,
                 preferred_stock_l,
                 perpetual_bond_l,
                 indept_acc_liab,
                 defer_tax_liab,
                 oth_liab,
                 le,
                 la,
                 t_liab,
                 paid_in_capital,
                 oth_equity_instr,
                 preferred_stock_e,
                 perpetual_bond_e,
                 capital_reser,
                 treasury_share,
                 oth_compre_income,
                 surplus_reser,
                 ordin_risk_reser,
                 retained_earnings,
                 forex_differ,
                 see,
                 sea,
                 t_equity_attr_p,
                 minority_int,
                 oth_effect_se,
                 oth_effect_sa,
                 t_sh_equity,
                 lee,
                 lea,
                 t_liab_equity) -> None:
        self.party_id = party_id
        self.ticker_symbol = ticker_symbol
        self.exchange_cd = exchange_cd
        self.publish_date = publish_date
        self.end_date_rep = end_date_rep
        self.end_date = end_date
        self.report_type = report_type
        self.fiscal_period = fiscal_period
        self.merged_flag = merged_flag
        self.cash_c_equiv = cash_c_equiv
        self.loan_to_oth_bank_fi = loan_to_oth_bank_fi
        self.trading_fa = trading_fa
        self.deriv_assets = deriv_assets
        self.pur_resale_fa = pur_resale_fa
        self.int_receiv = int_receiv
        self.premium_receiv = premium_receiv
        self.subrog_reco_receiv = subrog_reco_receiv
        self.reinsur_receiv = reinsur_receiv
        self.rr_reins_une_prem = rr_reins_une_prem
        self.rr_reins_outstd_cla = rr_reins_outstd_cla
        self.rr_reins_lins_liab = rr_reins_lins_liab
        self.rr_reins_lthins_liab = rr_reins_lthins_liab
        self.ph_pledge_loans = ph_pledge_loans
        self.fixed_term_depos = fixed_term_depos
        self.avail_for_sale_fa = avail_for_sale_fa
        self.htm_invest = htm_invest
        self.lt_equity_invest = lt_equity_invest
        self.refund_cap_depos = refund_cap_depos
        self.invest_real_estate = invest_real_estate
        self.fixed_assets = fixed_assets
        self.intan_assets = intan_assets
        self.indep_acc_assets = indep_acc_assets
        self.defer_tax_assets = defer_tax_assets
        self.oth_assets = oth_assets
        self.ae = ae
        self.aa = aa
        self.t_assets = t_assets
        self.st_borr = st_borr
        self.loan_fr_oth_bank_fi = loan_fr_oth_bank_fi
        self.trading_fl = trading_fl
        self.deriv_liab = deriv_liab
        self.sold_for_repur_fa = sold_for_repur_fa
        self.prem_receiv_adva = prem_receiv_adva
        self.commis_payable = commis_payable
        self.reinsur_payable = reinsur_payable
        self.payroll_payable = payroll_payable
        self.taxes_payable = taxes_payable
        self.indem_acc_payable = indem_acc_payable
        self.policy_div_payable = policy_div_payable
        self.ph_invest = ph_invest
        self.reser_une_prem = reser_une_prem
        self.reser_outstd_claims = reser_outstd_claims
        self.reser_lins_liab = reser_lins_liab
        self.reser_lthins_liab = reser_lthins_liab
        self.lt_borr = lt_borr
        self.bond_payable = bond_payable
        self.preferred_stock_l = preferred_stock_l
        self.perpetual_bond_l = perpetual_bond_l
        self.indept_acc_liab = indept_acc_liab
        self.defer_tax_liab = defer_tax_liab
        self.oth_liab = oth_liab
        self.le = le
        self.la = la
        self.t_liab = t_liab
        self.paid_in_capital = paid_in_capital
        self.oth_equity_instr = oth_equity_instr
        self.preferred_stock_e = preferred_stock_e
        self.perpetual_bond_e = perpetual_bond_e
        self.capital_reser = capital_reser
        self.treasury_share = treasury_share
        self.oth_compre_income = oth_compre_income
        self.surplus_reser = surplus_reser
        self.ordin_risk_reser = ordin_risk_reser
        self.retained_earnings = retained_earnings
        self.forex_differ = forex_differ
        self.see = see
        self.sea = sea
        self.t_equity_attr_p = t_equity_attr_p
        self.minority_int = minority_int
        self.oth_effect_se = oth_effect_se
        self.oth_effect_sa = oth_effect_sa
        self.t_sh_equity = t_sh_equity
        self.lee = lee
        self.lea = lea
        self.t_liab_equity = t_liab_equity

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

    def __init__(self, party_id,
                 ticker_symbol,
                 exchange_cd,
                 publish_date,
                 end_date_rep,
                 end_date,
                 report_type,
                 fiscal_period,
                 merged_flag,
                 cash_c_equiv,
                 client_depos,
                 sett_prov,
                 client_prov,
                 loan_to_oth_bank_fi,
                 trading_fa,
                 deriv_assets,
                 pur_resale_fa,
                 int_receiv,
                 refund_depos,
                 avail_for_sale_fa,
                 htm_invest,
                 lt_equity_invest,
                 invest_real_estate,
                 fixed_assets,
                 intan_assets,
                 transac_seat_fee,
                 defer_tax_assets,
                 oth_assets,
                 ae,
                 aa,
                 t_assets,
                 st_borr,
                 pledge_borr,
                 loan_fr_oth_bank_fi,
                 trading_fl,
                 deriv_liab,
                 sold_for_repur_fa,
                 funds_sec_trad_agen,
                 funds_sec_undw_agen,
                 payroll_payable,
                 taxes_payable,
                 int_payable,
                 estimated_liab,
                 lt_borr,
                 bond_payable,
                 preferred_stock_l,
                 perpetual_bond_l,
                 defer_tax_liab,
                 oth_liab,
                 le,
                 la,
                 t_liab,
                 paid_in_capital,
                 oth_equity_instr,
                 preferred_stock_e,
                 perpetual_bond_e,
                 capital_reser,
                 treasury_share,
                 oth_compre_income,
                 surplus_reser,
                 ordin_risk_reser,
                 transac_risk_reser,
                 retained_earnings,
                 forex_differ,
                 see,
                 sea,
                 t_equity_attr_p,
                 minority_int,
                 oth_effect_se,
                 oth_effect_sa,
                 t_sh_equity,
                 lee,
                 lea,
                 t_liab_equity
                 ) -> None:
        self.party_id = party_id
        self.ticker_symbol = ticker_symbol
        self.exchange_cd = exchange_cd
        self.publish_date = publish_date
        self.end_date_rep = end_date_rep
        self.end_date = end_date
        self.report_type = report_type
        self.fiscal_period = fiscal_period
        self.merged_flag = merged_flag
        self.cash_c_equiv = cash_c_equiv
        self.client_depos = client_depos
        self.sett_prov = sett_prov
        self.client_prov = client_prov
        self.loan_to_oth_bank_fi = loan_to_oth_bank_fi
        self.trading_fa = trading_fa
        self.deriv_assets = deriv_assets
        self.pur_resale_fa = pur_resale_fa
        self.int_receiv = int_receiv
        self.refund_depos = refund_depos
        self.avail_for_sale_fa = avail_for_sale_fa
        self.htm_invest = htm_invest
        self.lt_equity_invest = lt_equity_invest
        self.invest_real_estate = invest_real_estate
        self.fixed_assets = fixed_assets
        self.intan_assets = intan_assets
        self.transac_seat_fee = transac_seat_fee
        self.defer_tax_assets = defer_tax_assets
        self.oth_assets = oth_assets
        self.ae = ae
        self.aa = aa
        self.t_assets = t_assets
        self.st_borr = st_borr
        self.pledge_borr = pledge_borr
        self.loan_fr_oth_bank_fi = loan_fr_oth_bank_fi
        self.trading_fl = trading_fl
        self.deriv_liab = deriv_liab
        self.sold_for_repur_fa = sold_for_repur_fa
        self.funds_sec_trad_agen = funds_sec_trad_agen
        self.funds_sec_undw_agen = funds_sec_undw_agen
        self.payroll_payable = payroll_payable
        self.taxes_payable = taxes_payable
        self.int_payable = int_payable
        self.estimated_liab = estimated_liab
        self.lt_borr = lt_borr
        self.bond_payable = bond_payable
        self.preferred_stock_l = preferred_stock_l
        self.perpetual_bond_l = perpetual_bond_l
        self.defer_tax_liab = defer_tax_liab
        self.oth_liab = oth_liab
        self.le = le
        self.la = la
        self.t_liab = t_liab
        self.paid_in_capital = paid_in_capital
        self.oth_equity_instr = oth_equity_instr
        self.preferred_stock_e = preferred_stock_e
        self.perpetual_bond_e = perpetual_bond_e
        self.capital_reser = capital_reser
        self.treasury_share = treasury_share
        self.oth_compre_income = oth_compre_income
        self.surplus_reser = surplus_reser
        self.ordin_risk_reser = ordin_risk_reser
        self.transac_risk_reser = transac_risk_reser
        self.retained_earnings = retained_earnings
        self.forex_differ = forex_differ
        self.see = see
        self.sea = sea
        self.t_equity_attr_p = t_equity_attr_p
        self.minority_int = minority_int
        self.oth_effect_se = oth_effect_se
        self.oth_effect_sa = oth_effect_sa
        self.t_sh_equity = t_sh_equity
        self.lee = lee
        self.lea = lea
        self.t_liab_equity = t_liab_equity

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
