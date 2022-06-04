# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 19:10:28 2021

@author: 乘一x1
"""

ans = 0
def dfs(i,k):
    global ans
    for j in range(n):
        if l[i][j] == "#" and visit[j]:
            if k == 1:
                ans+=1
            else:
                visit[j] = False
                for m in range(i+1,n-k+2):
                    dfs(m,k-1)
                visit[j] = True
while True:
    n,k = [int(x) for x in input().split()]
    if n == -1:
        break
    l = []
    for i in range(n):
        l.append([i for i in input()])
    visit = [True for i in range(n)]
    ans = 0
    for i in range(n-k+1):
        dfs(i,k)
    print(ans)
