# -*- coding: utf-8 -*-
"""
Created on Sun Jan 04 00:39:41 2015

@author: tianyi
"""

year = int(raw_input('year:'))
month = int(raw_input('month:'))


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
        
    

def get_num_of_days_in_month(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    elif month in (4,6,9,11):
        return 30
    elif is_leap_year(year):
        return 29
    else:
        return 28
        

def get_total_num_of_days(year,month): #这个月之前的天数，已知1800年1月1日是WED
    days = 0
    for y in range(1800,year):#### year 的前一年
      if is_leap_year(y):
          days += 366
      else:
          days += 365
          
    for m in range(1,month):# 同样是前一个月
        days += get_num_of_days_in_month(year,m)
        
    return days
         
    
def get_start_day(year,month):
    
    return (3 + get_total_num_of_days(year,month)) % 7
    
    
print get_start_day(year,month)
