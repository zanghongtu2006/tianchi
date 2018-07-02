# -*- coding: utf-8 -*-

from enum import Enum


class UnitCD(Enum):
    # 架次
    sortie = 'sortie'
    # 人次
    person_time = 'person - time'
    # 百万人公里
    million_person_km = 'million person - km'
    # 辆
    car = 'car'
    # 人
    person = 'person'
    # 万人公里
    ten_thousand_person_km = 'ten thousand person - km'
    million_passenger_km = 'million passenger - km'
    ten_thousand_ton = 'ten thousand ton'
    ten_thousand_TEU = 'ten thousand TEU'
    ten_thousand_container = 'ten thousand container'
    ten_thousand_person = 'ten thousand person'
    million_seat_km = 'million seat - km'
    car_per_daily = 'car / daily'
    yuan = '￥'
    tom = 'ton'
    m2 = 'm2'


INDICT_NAME_CN_EN_MAPPING = {
    '白云机场: 飞机起降架次:当月值': 'Baiyun Airport: Aircraft take - off and landing times'
}

INDICT_NAME_EN_CN_MAPPING = {
    'Baiyun Airport: Aircraft take - off and landing times': '白云机场: 飞机起降架次:当月值'
}

UNIT_CD_CN_EN_MAPPING = {
    '架次': 'sortie'
}

UNIT_CD_EN_CN_MAPPING = {
    'sortie': '架次'
}
