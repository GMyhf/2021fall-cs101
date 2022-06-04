# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:13:43 2021

@author: 乘一x1
"""

import copy
s = []
for i in range(5):
    s.append([int(x) for x in input().split(" ")])
for i in range(64):
    a = []
    while len(a)<6:
        a.append(i%2)
        i //= 2
    a = [a[::-1]]
    x = copy.deepcopy(s)
    for j in range(1,5,1):
        temp = []
        for k in range(0,6,1):
            if j>=2:
                t1 = a[j-2][k] 
            else:
                t1 = 0
            if k>=1:
                t2 = a[j-1][k-1] 
            else:
                t2 = 0
            if k<=4:
                t3 = a[j-1][k+1] 
            else:
                t3 = 0
            t4 = a[j-1][k]
            if (t1+t2+t3+t4+2)%2 == 1:
                x[j-1][k] = 1 - x[j-1][k]
            temp.append(x[j-1][k]) 
        a.append(temp)
    for k in range(0,6,1):
            t1 = a[3][k] 
            if k>=1:
                t2 = a[4][k-1] 
            else:
                t2 = 0
            if k<=4:
                t3 = a[4][k+1] 
            else:
                t3 = 0
            t4 = a[4][k]
            if (t1+t2+t3+t4+2)%2 == 1:
                    x[4][k] = 1 - x[4][k]
    if x[-1] == [0,0,0,0,0,0]:
        for j in range(0,5,1):
            for k in range(0,6,1):
                if k != 5:
                    print(a[j][k],end = " ")
                else:
                    print(a[j][k],end = "\n")
        break