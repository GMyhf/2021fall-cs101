# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:33:36 2021

@author: 乘一x1
"""

n,w = [int(x) for x in input().split()]
l = []
for i in range(n):
    a,b = [int(x) for x in input().split()]
    w0 = a/b
    for i in range(b):
        l.append(w0)
l = sorted(l,reverse = True)
print(sum(l[:w]))