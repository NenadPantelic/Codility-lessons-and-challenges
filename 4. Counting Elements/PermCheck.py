#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:38:15 2020

@author: nenad
"""
"""
Problem description: https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

"""

def solution(A):
    # sort array
    A.sort()
    for i in range(1,len(A)+1):
        if A[i-1] != i:
            return 0
    # otherwise
    return 1

# Test 1
arr = [4,1,3,2]
print(solution(arr))


# Test 2
arr = [4,1,2]
print(solution(arr))