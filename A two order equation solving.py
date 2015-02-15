# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 09:33:59 2014

@author: tianyi
"""

import math


while True:

    a = float(raw_input('a:'))
    b = float(raw_input('b:'))
    c = float(raw_input('c:'))
    if a != 0:
        delta = b ** 2 - 4 * a * c 
        if delta < 0:
            print 'no solution'
        elif delta == 0:
            s = -b / (2 * a)
            print 's', s
        else:
            root = math.sqrt(delta)
            s1 = (-b + root) / (2 * a * c)
            s2 = (-b - root) / (2 * a * c)
            print s1, s2
    ch = raw_input('Quit?:')
    if ch == 'q':
        break