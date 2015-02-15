# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 11:12:58 2015

@author: tianyi
"""

x = 2
count = 0

while count < 50 :
    for i in range(2,x):
        if x % i == 0:
            break
    else:
        print x
        count += 1
    x += 1
    