#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:02:57 2020

@author: nenad
"""

"""
Problem description: https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
"""
# O(nlog(n))
def solution(A):
    A.sort()
    for i in range(1, len(A)+1):
        if A[i-1] != i:
            return i
    return len(A)+1


def solution(A):
    els = set(A)
    for i in range(1, len(A)+1):
        if i not in els:
            return i
    return len(A)+1
# Test 1
arr = [5,2,1,3]
print(solution(arr))

    