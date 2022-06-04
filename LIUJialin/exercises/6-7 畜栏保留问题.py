# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 20:38:04 2021

@author: 乘一x1
"""
import heapq
l = []
n = int(input())
d = {}
cow = [0 for i in range(n)]
for i in range(n):
    a,b = [int(x) for x in input().split()]
    l.append((a,b,i))
    d[(a,b)] = i
cnt = 0
l = sorted(l,key = lambda x:x[0])


q = []
for i in range(n):
    if q == []:
        cnt+=1
        cow[l[i][2]] = cnt
    else:
        k=heapq.heappop(q)
        if l[i][0]> k[0]:
            cow[l[i][2]] = cow[k[1]]
        else:
            heapq.heappush(q,k)  
            cnt+=1
            cow[l[i][2]] = cnt
    heapq.heappush(q,(l[i][1],l[i][2]))  
    
    
print(cnt)
print(*cow,sep="\n")