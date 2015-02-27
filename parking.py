# -*- coding: utf-8 -*-
"""
Created on Mon Jan 05 00:28:03 2015

@author: tianyi
"""
"""随机停车数量"""
import random

def parking(low, high):
    if high - low < 1:
        return 0

    else:
        x = random.uniform(low,high - 1) #车头停靠位置
        return parking(low, x) + 1 + parking(x + 1, high)

s = 0
for i in range(1000):
    s += parking(0, 5)

s = s / 1000.0


print s



