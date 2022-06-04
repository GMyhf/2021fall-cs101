# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 11:16:17 2021

@author: 乘一x1
"""

n = int(input())
l = [int(x) for x in input().split()]
len_max = {}
len_max[0] = 1
ma = 1

for i in range(1,n,1):
    len_max[i] = 1
    for j in range(i,-1,-1):
        if l[j]<l[i] and len_max[i]<len_max[j]+1:
            len_max[i] = len_max[j]+1
    if len_max[i] > ma:
        ma = len_max[i]
        
print(ma)