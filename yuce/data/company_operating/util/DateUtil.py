#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: DateUtil.py

@time: 7/7/18 6:44 PM

@desc:

"""

import time


def day2num(day_str):
    return time.mktime(time.strptime(day_str, "%Y-%m-%d"))


def num2day(day_num):
    return time.strftime("%Y-%m-%d", time.localtime(day_num))
