# -*- coding: utf-8 -*-
"""
Created on Sun Jan 04 21:27:40 2015

@author: tianyi
"""
x = int(raw_input('input x:'))

count = 0
def hanoi(n, A, B, C):
    global count
    
    if n == 1:
        print "move", n, 'from', A, 'to', C  #移动过程
        count += 1
    else:
        hanoi(n - 1, A, C, B) #将前 n-1 个盘子， 通过 C， 从 A 移动到 B
        print 'move', n,'from', A, 'to', C  #移动过程 只剩一个盘子
        count += 1
        hanoi(n - 1, B, A, C) # 将前 n-1 个盘子， 通过 A， 从 B 移动到 C
        
hanoi(x, 'left', 'mid' , 'right' )
print 'total steps:', count
        