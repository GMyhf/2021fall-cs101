# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 16:00:49 2021

@author: 乘一x1
"""

import copy
out = []
while True:
    flag = 1
    q = 0
    a = input()
    if a == "0 0":
        break
    else:
        n,m = a.split(" ")
        n = int(n)
        flag == 1
        m = int(m)
        remain = [i for i in range(1,n+1,1)] 
        while len(remain) >1:
            a = copy.deepcopy(remain[0])
            del remain[0]
            if flag%m !=0:
                remain.append(a)
            flag += 1
        for i in remain:
            out.append(i)
for i in out:
    print(i)