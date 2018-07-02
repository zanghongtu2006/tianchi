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


