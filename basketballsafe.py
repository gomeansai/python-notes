# -*- coding: utf-8 -*-
"""
Created on Tue Dec 30 20:50:53 2014

@author: tianyi
"""

points = int(raw_input('Leading points:'))
has_ball = raw_input('The leading team has ball(yes/no)')
secends = int(raw_input('the left secends:'))

points -= 3

if has_ball == 'yes':
    points += 0.5
else:
    points -= 0.5
    
if points <0:
    points = 0

points = points ** 2

if points > secends:
    print 'not safe'
else:
    print 'safe'
    
    
    