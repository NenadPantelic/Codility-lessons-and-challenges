#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:26:51 2020

@author: nenad

"""

"""
Problem description: https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

"""
def solution(A):
    A.sort()
    next_to_check = 1
    for i in range(1, len(A)+1):
        if A[i-1] < next_to_check:
            continue
        if A[i-1] > next_to_check:
            return next_to_check
        next_to_check += 1
    return next_to_check


# Test 1
A = [1, 3, 6, 4, 1, 2]
print(solution(A))
    
# Test 2
A = [1, 2,3]
print(solution(A))        

#Test 3
A = [-1,-3]
print(solution(A)) 