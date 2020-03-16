#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:47:30 2020

@author: nenad
"""


def solution(H):
    # write your code in Python 3.6
    n = len(H)
    l = 0
    r = n-1
    left_max = right_max = 0
    lmax_index = 0
    rmax_index = n-1
    while l < r:
        if H[l] <= H[r]:
            if H[l] >= left_max:
                left_max = H[l]
                lmax_index = l
            l += 1
        else:
            if H[r] >= right_max:
                right_max = H[r]
                rmax_index = r
            r -= 1
    #print(l,r)
    #global_maxx = maxx(H[l], H[lmax_index], H[rmax_index])
            
    maxxes = {l:H[l],lmax_index:H[lmax_index], rmax_index:H[rmax_index]}
    max_indices = [l, lmax_index, rmax_index]
    #max_indices.sort()
    #maxx_values = [maxxes[val] for val in max_indices]
    #if maxxes[0] == maxxes[1] == maxxes[2]:
    #
    print(max_indices)
    print(H[l], H[rmax_index])
    if H[l] == H[lmax_index]:
        #maxx_pos = l
        total = abs(l - lmax_index+1) * H[l] + (n-l-1) * H[rmax_index]
    elif H[l] == H[rmax_index]:
        "HEREE"
        total = rmax_index* H[lmax_index] + (n-rmax_index) * H[rmax_index]
        print(rmax_index* H[lmax_index])
        print((n-rmax_index) * H[rmax_index])
    else:
        lval = H[l] - H[lmax_index]
        rval = H[l] - H[rmax_index]
        if lval > rval:
            total = l * H[lmax_index] + (n-l) * H[l]
        else:
            total = (l+1) * H[l] + (n-l-1) * H[rmax_index]
    return total
        
    #print(max_indices)
    
    #return (H[l],H[lmax_index], H[rmax_index])      

# # Test 1
# H = [5,3,2,4]
# #print(solution(H))
# # Test 2
# H = [5,3,5,2,1]
# #print(solution(H))

# # Test 2
# H = [1,1,7,6,6,6]
# print(solution(H))

# # Test 4
# H = [3,1,4]
# print(solution(H))

# Test 4
H = [5,5,6,4,3,2,1]
#print(solution(H))
        

# Test 4
H = [7,7,3,7,7]
print(solution(H))