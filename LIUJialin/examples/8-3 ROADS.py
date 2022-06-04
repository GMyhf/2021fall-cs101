# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:44:01 2021

@author: 乘一x1
"""
import sys
sys.setrecursionlimit(1000000)
money = int(input())
city = int(input())
road = int(input())
from collections import defaultdict
G = defaultdict(list)
for i in range(road):
    a1,a2,a3,a4 = [int(x) for x in input().split()]
    G[a1].append([a2,a3,a4])
minstep = float("inf")
mark = [True for i in range(city+1)]
minL = [[float("inf") for i in range(money+1)] for i in range(city+1)]

def f(x,step,cost):
    global minstep,money,mark,d
    if x == city:
        minstep = min(step,minstep)
        return
     
    for i in G[x]:
        if mark[i[0]] and step+i[1]<minstep and cost+i[2]<=money:
            if step+i[1]<minL[i[0]][cost+i[2]]:
                mark[i[0]] = False
                minL[i[0]][cost+i[2]] = step+i[1]
                f(i[0],step+i[1],cost+i[2])
                mark[i[0]] = True
mark[1] = False
f(1,0,0)
if minstep == float("inf"):
    print(-1)
else:
    print(minstep)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
minstep = float("inf")
mark = [True for i in range(city+1)]
def f(x,step,cost):
    global minstep,money,mark,d
    if step>=minstep or cost>money:
        return
    if x == city:
        minstep = min(step,minstep)
        return
    if d[x] == []:
        return
    for i in d[x]:
        if mark[i]:
            mark[i] = False
            f(i,step+l[(x,i)],cost+t[(x,i)])
            mark[i] = True
mark[1] = False
f(1,0,0)
if minstep == float("inf"):
    print(-1)
else:
    print(minstep)
    
    




