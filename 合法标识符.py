# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 13:18:21 2015

@author: ty
"""

def is_legalname(name):
    if name in keyword.kwlist:
        return False
    elif name == "":
        return False
    elif name[0] not in string.letters + '_':
         return False
    for i in name:
        if i not in string.letters + '_' + string.digits :
            return False
    return True

stopword = ''
str = ''
for line in iter(raw_input, stopword):
  str += line + '\n'

import string
import keyword
for words in str.split():

    if is_legalname(words):
        print True
    else:
        print False
