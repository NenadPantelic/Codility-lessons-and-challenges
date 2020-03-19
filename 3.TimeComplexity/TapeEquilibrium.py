#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 14:42:37 2020

@author: nenad
"""

"""
Problem description: https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

"""
# O(n)
def solution(A):
    cumsum = []
    sum = 0
    # determine cumsum for every element
    for val in A:
        sum += val
        cumsum.append(sum)
        
    # maximum possible value of A[i] is 1000, and the minimum one is -1000 -> difference is 2000
    min_diff = 2000
    # get two sums - before element (element included) and sum of elements after it -> use the smallest one
    for i in range(len(A)-1):
        diff = abs(sum - 2 * cumsum[i])
        if diff < min_diff:
            min_diff = diff
            
    return min_diff
    

# Test 1
A = [3,1,2,4,3]
print(solution(A))

# Test 2
A = [3,3]
print(solution(A))

# Test 3
A = [-1000,1000]
print(solution(A))
