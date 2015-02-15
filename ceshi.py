# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 12:59:18 2015

@author: tianyi
"""

x = 1
 
def fun(x):
    global x
    x = 2
 
fun(x)
 
print x