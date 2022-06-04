# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:20:29 2021

@author: 乘一x1
"""

n,m,k=[int(x) for x in input().split()]
a=[[m]*(k+1) for i in range(n+1)]
for i in range(n+1):
    a[i][0]=0
for i in range(1,k+1):
    u,v=[int(x) for x in input().split()]
    for j in range(n,u-1,-1):
        for r in range(i,0,-1):
            a[j][r]=min(a[j][r],a[j-u][r-1]+v)
for i in range(k,-1,-1):
    if m>a[n][i]:
        print(i,m-a[n][i])
        break
