# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 19:41:52 2021

@author: 乘一x1
"""
import array
R,C = [int(x) for x in input().split()]
N = int(input())
flag = [array.array ("B", [0]*(C+1)) for j in range(R+1)]
point = [0 for i in range(N)]
for i in range(N):
    x,y = [int(x) for x in input().split()]
    point[i] = (x,y)
    flag[x][y] = 1
point = sorted(point,key = lambda x:(x[0],x[1]))
ma = 2
def check(x,y):
    if 0<x<=R and 0<y<=C:
        return True
for i in range(N):
    x1,y1 = point[i]
    for j in range(i+1,N):
        x2,y2 = point[j]
        dx = x2- x1
        dy = y2- y1
        cnt=2
        if check(x1-dx,y1-dy):
            continue
        if x1+dx*(ma-1) > R:
            break
        if y1+dy*(ma-1) > C or y1+dy*(ma-1) <= 0:
            continue

        while check(x2+dx,y2+dy):
            x2+= dx
            y2+= dy
            if not flag[x2][y2]:
                break
            cnt+= 1
        else:
            ma = max(ma,cnt)
if ma == 2:
    ma = 0
print(ma)