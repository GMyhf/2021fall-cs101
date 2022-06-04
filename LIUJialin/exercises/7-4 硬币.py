# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 09:35:27 2021

@author: 乘一x1
"""

n,x = [int(x) for x in input().split()]
lis = [int(x) for x in input().split()]
dp = [0 for i in range(x+1)]
ans = [0 for i in range(x+1)]
dp[0] = 1
for i in range(n):
    for j in range(x,lis[i]-1,-1):
        dp[j]+=dp[j-lis[i]]
l = []
for i in range(n):
    for j in range(x+1):
        if j <lis[i]:
            ans[j] = dp[j]
        else:
            ans[j] = dp[j] - ans[j - lis[i]]
    if ans[x]==0:
        l.append(lis[i])
print(len(l))
print(*l,sep=" ")