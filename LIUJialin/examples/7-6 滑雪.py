# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:59:37 2021

@author: 乘一x1
"""

ma = 0
def f(x_now,y_now):
    global dp,l,m,n,turn
    for i in range(4):
        x = x_now + turn[i][0]
        y = y_now + turn[i][1]
        if 0<=x<m and 0<=y<n:
            if l[x][y] > l[x_now][y_now]:
                if dp[x][y] == 1:
                    dp[x_now][y_now] = max(dp[x_now][y_now],f(x,y)+1) 
                else:
                    dp[x_now][y_now] = max(dp[x_now][y_now],dp[x][y]+1)
    return dp[x_now][y_now]
                 
turn = ((0,1),(1,0),(0,-1),(-1,0))
m,n = [int(x) for x in input().split()]
l = []
for i in range(m):
    temp = [int(x) for x in input().split()]
    l.append(temp)
dp = [[1 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        ma = max(ma,f(i,j))
print(ma)