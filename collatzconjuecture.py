# -*- coding: utf-8 -*-
"""
Created on Fri Jan 02 21:34:48 2015

@author: tianyi
"""

n =  int(raw_input('input n:'))

while n != 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1
    print n
    