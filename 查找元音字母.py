# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 22:25:52 2015

@author: tianyi
"""
m = raw_input('input string:')


def vowles_count(s):
    count = 0
    for c in s:
        if c in 'aeiouAEIOU':
            count += 1
            
    return count

print vowles_count(m)