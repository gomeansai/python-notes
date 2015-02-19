# -*- coding: utf-8 -*-
"""
Created on Sun Jan 04 21:27:40 2015

@author: tianyi
"""

def hanoi(n, A, B, C):
    if n == 1:
        print "move", n, 'from', A, 'to', C  #移动过程
        return 1
    else:
        count = hanoi(n - 1, A, C, B) #将前 n-1 个盘子， 通过 C， 从 A 移动到 B
        print 'move', n,'from', A, 'to', C  #移动过程 只剩一个盘子
        count += 1
        count += hanoi(n - 1, B, A, C) # 将前 n-1 个盘子， 通过 A， 从 B 移动到 C
        return count

if __name__ == '__main__':
    x = int(raw_input('input x:'))
    count = hanoi(x, 'left', 'mid' , 'right' )
    print 'total steps:', count
