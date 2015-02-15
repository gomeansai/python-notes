# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 21:17:07 2015

@author: ty
"""
import re

f = open('names.txt')

pattern = '(C.A)'

for line in f:
    name = line.strip()
    result = re.search(pattern, name)
    if result:
        print 'Find in {}'.format(name)
        
f.close