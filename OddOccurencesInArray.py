#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:11:59 2020

@author: nenad
"""

from collections import Counter
def odd_occurence(arr):
    counter = Counter()
    # count freq of every value
    for val in arr:
        counter[val] += 1
    
    # only one element with odd freq is present - find it
    for val in counter:
        if counter[val] % 2 == 1:
            return val
        

# Test 1
arr = [9,3,9,3,9,7,9]
print(odd_occurence(arr))