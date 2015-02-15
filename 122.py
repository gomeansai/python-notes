# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 09:18:07 2014

@author: tianyi
"""

seconds = int(raw_input('input the seconds:'))
h = seconds / 3600
m = (seconds - h * 3600 ) /  60
s = seconds - h * 3600 - m * 60 
print h , m , s