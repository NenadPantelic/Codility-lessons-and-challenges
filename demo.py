#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 15:12:46 2020

@author: nenad
"""


def solution(A):
    A.sort()
    counter = 1
    for i in range(len(A)):
        if A[i] <= 0 or A[i] < counter:
            continue
        if A[i] != counter:
            return counter
        counter += 1
    return counter
# Test 1
A = [1, 3, 6, 4, 1, 2]
print(solution(A))
    
# Test 2
A = [1, 2,3,]
print(solution(A))        

#Test 3
A = [-1,-3]
print(solution(A))        