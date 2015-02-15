# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 09:22:48 2015

@author: tianyi
"""

def is_ok(string_word):
    if string_word in keyword.kwlist:
        return False
    elif string_word == '':
        return False
    elif string_word[0] not in string.ascii_letters and string_word[0] != '_':
        return False
    for i in string_word[1:]:
        if i not in string.ascii_letters and i not in string.digits and i != '_':
            return False
    return True
    
import string
import keyword
string_list = []
input_line = raw_input()
string_list.append(input_line)
while input_line != '':
    input_line = raw_input()
    string_list.append(input_line)
del string_list[-1]
for word in string_list:
    print is_ok(word)