# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:03:23 2021

@author: 乘一x1
"""
cnt = 0
def f(x_now,y_now):
    global flag,cnt
    flag0 = True
    for i in range(8):
        x = x_now + turn[i][0]
        y = y_now + turn[i][1]
        if 0<=x<n and 0<=y<m:
            if flag[x][y]:
                flag0 = False
                flag[x][y] = False
                f(x,y)
                flag[x][y] = True
    if flag0:
            flag1 = True
            for i in range(n):
                for j in range(m):
                    if flag[i][j]:
                        flag1 = False
                        break
            if flag1:
                cnt+=1
result = []
for _ in range(int(input())):
    cnt = 0
    n,m,x,y = [int(x) for x in input().split()]
    flag = [[True for i in range(m)] for j in range(n)]
    turn = ((2,1),(1,2),(2,-1),(1,-2),(-1,-2),(-2,-1),(-1,2),(-2,1))
    flag[x][y] = False
    f(x,y)
    result.append(cnt)
print(*result,sep="\n")