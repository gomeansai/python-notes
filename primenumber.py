# -*- coding: utf-8 -*-
"""
Created on Sat Jan 03 10:21:20 2015

@author: tianyi
"""
while True:
    
    
    x = int(raw_input("input x:"))
    
    for i in range(2,x):
        if x % i == 0:
            print "not prime"
            break
    else:
        print "prime number"
        
    ch = raw_input('quit?:')
    if ch ==  "q":
        break
