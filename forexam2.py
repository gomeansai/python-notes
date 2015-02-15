# -*- coding: utf-8 -*-
"""
Created on Thu Jan 01 21:59:51 2015

@author: tianyi
"""


pi = 0
sign = 1
divisor = 1

for i in range(1,3):
    pi += (4 * sign) / divisor
    sign *= -1
    divisor += 2

print pi