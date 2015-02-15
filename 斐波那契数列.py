# -*- coding: utf-8 -*-
"""
Created on Sun Jan 04 21:18:01 2015

@author: tianyi
"""

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(raw_input('input n:'))

for i in range(1,11):
    if fib(i) < n:
        print i, fib(i)
    
