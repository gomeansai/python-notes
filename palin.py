# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 23:31:04 2015

@author: tianyi
"""

num = 151
num_p = 0
num_t = num 

while num_t != 0:
    num_p = num_p * 10 + num_t % 10
    num_t = num_t / 10
    
if num == num_p:
    print " is a palin"
else:
    print "no"