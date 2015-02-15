# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 00:02:51 2015

@author: tianyi
"""

for c in range (36):
    for r in range(36):
        if c * 2 + r * 4 == 94 and c + r == 35:
            print "the number of chicken is" , c
            print "the number of rabbits is" , r