# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 19:28:01 2021

@author: 乘一x1
"""

n,m = [int(x) for x in input().split()]
l = []
left = 0
right = 0
for _ in range(n):
    temp = int(input())
    right += temp
    left = max(left,temp)
    l.append(temp)
while right>left:
    now = (left+right)//2
    cnt = 1
    temp = 0
    for i in range(n):
        if temp + l[i]>now:
            temp = l[i]
            cnt += 1
        else:
            temp += l[i]
        if cnt > m:
            left = now+1
            break
    else:
            right = now
print(right)            
            
            
    