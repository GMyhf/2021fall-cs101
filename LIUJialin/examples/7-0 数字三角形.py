# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 11:11:28 2021

@author: 乘一x1
"""
n = int(input())
l = []
ma = []
for _ in range(n):
    l.append([])
    ma.append([])
for i in range(n):
    for j in input().split():
        l[i].append(int(j))
        if i!=n-1:
            ma[i].append(0)
        else:
            ma[i].append(int(j))
        
for i in range(n-2,-1,-1):
    for j in range(0,i+1,1):
            ma[i][j] = l[i][j] + max(ma[i+1][j],ma[i+1][j+1])
print(ma[0][0])
    
    