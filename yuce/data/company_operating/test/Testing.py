#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: Testing.py

@time: 7/7/18 6:38 PM

@desc:

"""

import time

str = '2016-03-31'
print(time.strptime(str, '%Y-%M-%d'))
print(time.mktime(time.strptime(str, '%Y-%M-%d')))
print('%Y-%M-%d', time.strptime(str, '%Y-%M-%d'))
