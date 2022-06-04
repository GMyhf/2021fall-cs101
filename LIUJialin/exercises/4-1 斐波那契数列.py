# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 13:06:17 2021

@author: 乘一x1
"""

n = int(input())
def feibo(x):
    if x==1:
        return 1
    elif x == 2:
        return 1
    else:
        return feibo(x-1) + feibo(x-2)
for i in range(n):
    a = int(input())
    print(feibo(a))    
    