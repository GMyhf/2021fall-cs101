# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 22:47:48 2021

@author: 乘一x1
"""

a,b,c = [int(x) for x in input().split(" ")]
cnt = 0
for i in range(c+1):
    for j in range(c+1):
        if a*i+b*j==c:
            cnt+= 1
            break
print(cnt)