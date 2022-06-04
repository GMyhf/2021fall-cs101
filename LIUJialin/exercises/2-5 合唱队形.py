# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 09:26:41 2021

@author: 乘一x1
"""

def dizeng(n,l):
    if n == 0:
        return 0
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
    return ma
def dijian(n,l):
    if n == 0:
        return 0
    len_max = {}
    len_max[0] = 1
    ma = 1
    
    for i in range(1,n,1):
        len_max[i] = 1
        for j in range(i,-1,-1):
                if l[j]>l[i] and len_max[i]<len_max[j]+1:
                    len_max[i] = len_max[j]+1
        if len_max[i] > ma:
            ma = len_max[i]
    return ma
n = int(input())
l = [x for x in input().split()]
m = 0
for i in range(n):
    
    temp = dizeng(i+1,l[:i+1]) +dijian(n-i,l[i:])-1
    if temp>m:
        m = temp
print(len(l)-m)
    