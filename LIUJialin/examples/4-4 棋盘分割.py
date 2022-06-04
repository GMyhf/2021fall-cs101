# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 14:22:40 2021

@author: 乘一x1
"""
def f(n,x1,y1,x2,y2):
    if dp[(n,x1,y1,x2,y2)]>0:
            return dp[(n,x1,y1,x2,y2)]
    if n == 1:
        su = 0
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                    su += l[i][j]
        dp[(n,x1,y1,x2,y2)] = su*su
        return su*su
    mi = 10000000
    for i in range(x1,x2):                
                mi = min(mi,f(n-1,x1,y1,i,y2)+f(1,i+1,y1,x2,y2)) 
                mi = min(mi,f(1,x1,y1,i,y2)+f(n-1,i+1,y1,x2,y2)) 
    for i in range(y1,y2):                
                mi = min(mi,f(n-1,x1,y1,x2,i)+f(1,x1,i+1,x2,y2))
                mi = min(mi,f(1,x1,y1,x2,i)+f(n-1,x1,i+1,x2,y2))
    dp[(n,x1,y1,x2,y2)] = mi
    return mi
n = int(input())
l = []
for i in range(8):
    l.append([int(x) for x in input().split()])
s = 0
for i in l:
    for j in i:
        s +=j
from collections import defaultdict
dp = defaultdict(int)

print("%.3lf"%(f(n,0,0,7,7)/n-s*s/n/n)**0.5)
