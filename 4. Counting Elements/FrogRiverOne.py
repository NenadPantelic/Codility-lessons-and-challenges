#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:04:35 2020

@author: nenad
"""

"""
Problem description: https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

"""
def solution(X, A):
    els = set(range(1,X+1))
    for i in range(len(A)):
        el = A[i]
        # value checked
        if el in els:
            els.remove(el)
        # all positions (in range [1,X] are checked)
        if len(els) == 0:
            return i
    # otherwise       
    return -1

# Test 1
A = [1,3,1,4,2,3,5,4]
X = 5
print(solution(X, A))

# Test 1
A = [1,3,1,4,2,3,5,4]
X = 4
print(solution(X, A))
