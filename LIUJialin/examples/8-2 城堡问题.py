# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:23:20 2021

@author: 乘一x1
"""
n = int(input())
m = int(input())
l = []
mark = [[True for i in range(m)] for j in range(n)]
for i in range(n):
    l.append([int(x) for x in input().split()])
s = 0
def dfs(x,y):
    global s
    if l[x][y]&1 == 0:
        if y>=1:
            if mark[x][y-1]:
                mark[x][y-1] = False
                s+=1
                dfs(x,y-1)
    if l[x][y]&2 == 0:
        if x>=1:
            if mark[x-1][y]:
                mark[x-1][y] = False
                s+=1
                dfs(x-1,y)
    if l[x][y]&4 == 0:
        if y+1<m:
            if mark[x][y+1]:
                mark[x][y+1] = False
                s+=1
                dfs(x,y+1)
    if l[x][y]&8 == 0:
        if x+1<n:
            if mark[x+1][y]:
                mark[x+1][y] = False
                s+=1
                dfs(x+1,y)        
ans = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if mark[i][j]:
            s = 1
            cnt +=1
            mark[i][j] = False
            dfs(i,j)
            ans = max(ans,s)     
print(cnt)
print(ans)        