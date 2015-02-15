# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 09:40:32 2015

@author: ty
"""

def f1 (my_dict):
    temp = 0
    for value in my_dict.values():
        temp = temp + value
    return temp
 
a_dict={'bill':1,'rich':2,'fred':10,'walter':20}
print f1(a_dict)