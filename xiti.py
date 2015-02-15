# -*- coding: utf-8 -*-
"""
Created on Sun Jan 04 00:13:55 2015

@author: tianyi
"""
def gcd(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        r = m % n
    return gcd(n, r)
print gcd(15, 36)