#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:17:20 2020

@author: nenad
"""

"""
Problem description: https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

"""
def cyclic_rotation(arr, k):
    copy_arr = arr[:]
    n = len(arr)
    for i in range(n):
        # cyclic rotation
        arr[(i+k)%n] = copy_arr[i]
        

    return arr


# Test 1
A = [3, 8, 9, 7, 6]
K = 3
print(cyclic_rotation(A,K))


# Test 2
A = [0,0,0]
K = 1
print(cyclic_rotation(A,K))



# Test 3
A = [1,2,3,4]
K = 4
print(cyclic_rotation(A,K))
    
