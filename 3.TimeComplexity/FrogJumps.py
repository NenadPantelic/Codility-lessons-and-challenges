#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:44:24 2020

@author: nenad
"""

"""
Problem description: https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

"""
# O((y-x) // d)
def frog_jumps(x,y,d):
    start = x
    counter = 0
    while start < y:
        start += d
        counter += 1
        
    return counter

# O(1))
def frog_jumps(x,y,d):
    import math
    return math.ceil((y-x) / d)

# Test 1
x = 10
y = 85
d = 30
print(frog_jumps(x, y, d))
    