# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 17:55:52 2021

@author: 乘一x1
"""
ma = 0
n = int(input())
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            if ((i+j)%2 == 0) and ((j+k)%3==0) and ((i+j+k)%5==0):
                if i+j+k>ma:
                    ma = i+j+k
print(ma)