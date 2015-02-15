# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 00:33:36 2015

@author: tianyi
"""

x = float(raw_input("please input x:"))
low = 0
high = x
guess = (low + high) / 2

while abs(guess ** 2 - x) > 1e-5:

    if guess ** 2 < x:
        low = guess
    else:
        high = guess
    
    guess = (low + high) / 2

print guess