# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:53:46 2021

@author: 乘一x1
"""

L,M = input().split(" ")
L = int(L)
M = int(M)
subway = set()
tree = [i for i in range(L+1)]
for i in range(M):
    l,r = input().split(" ")
    l = int(l)
    r = int(r)
    subway0 = set(range(l,r+1,1))
    subway =subway | subway0
for j in subway:
    tree.remove(j)
print(len(tree))
    