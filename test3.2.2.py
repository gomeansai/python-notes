# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 20:21:19 2014

@author: tianyi
"""

num = 9
count = 0
 
while num > 0:
    if num % 2 == 0:
        num /= 2
    elif num % 3 == 0:
        num /= 3
    else:
        num -= 1
    count += 1
     
print count