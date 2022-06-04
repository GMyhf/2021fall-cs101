# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:26:56 2021

@author: 乘一x1
"""

d = int(input())
n = int(input())
dic = {}
cand = set()
for i in range(n):
    a,b,j = [int(x) for x in input().split(' ')]
    dic[(a,b)] = j
    for p in range(-d,d+1,1):
        for q in range(-d,d+1,1):
            if 0<=a+p<=1024 and 0<=b+q<=1024:
                cand.add((a+p,b+q))

ma = 0
ma_number = 0
for i,j in cand:
        l = i-d
        r = i+d
        u = j-d
        b = j+d
        temp = 0
        for k in dic:
            if l<=k[0]<=r and u<=k[1]<=b:
                temp += dic[k]
        if temp>ma:
            ma = temp
            ma_number = 1
        elif temp == ma:
            ma_number+= 1
print(ma_number,ma)
