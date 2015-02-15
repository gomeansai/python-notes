# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 00:54:17 2014

@author: tianyi
"""

def f(n):
    if n==1:
        return 1047
    return (f(n-1)+1000)*1.047
    print f(n)