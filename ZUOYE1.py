# -*- coding: utf-8 -*-
"""
Created on Mon Jan 05 08:44:27 2015

@author: tianyi
"""

x = int(raw_input('input x:'))

def hanoi(n, A, B, C):

    
    if n == 1:
        print "Move", n, 'from', A, 'to', C  #移动过程

    else:
        hanoi(n - 1, A, C, B) #将前 n-1 个盘子， 通过 C， 从 A 移动到 B
        print 'Move', n,'from', A, 'to', C  #移动过程 只剩一个盘子
        hanoi(n - 1, B, A, C) # 将前 n-1 个盘子， 通过 A， 从 B 移动到 C


hanoi(x, 'A', 'B', 'C')