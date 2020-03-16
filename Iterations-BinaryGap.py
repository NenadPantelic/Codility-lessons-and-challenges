#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 13:59:42 2020

@author: nenad
"""


def binary_gap(N):
    binary_rep = bin(N)[2:]
    n = len(binary_rep)
    i = 0
    # flags for start and end of the zero sequence
    start = end = False
    maxlen = 0
    count = 0
    while i < n:
        if binary_rep[i] == "1":
            if start:
                end = True
            else:
                start = True
            # sequence ended
            if end:
                end = False
                maxlen = max(maxlen, count)
                count = 0
            i += 1
        else:
            # iterate over zeros and count them
            while i < n and binary_rep[i] == "0":
                count += 1
                i += 1
    return maxlen
    
    
    
    
# Test 1
N = 9
print(binary_gap(N))

# Test 2
N = 32
print(binary_gap(N))

# Test 3
N = 20
print(binary_gap(N))

# Test 4
N = 15 
print(binary_gap(N))
# # Test 5
N = 1041
print(binary_gap(N))
