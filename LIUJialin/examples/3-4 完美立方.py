# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:08:05 2021

@author: 乘一x1
"""

n = int(input())
result = []
for i in range(6,n+1,1):
    for x1 in range(2,i,1):
        for x2 in range(x1,i,1):
            for x3 in range(x2,i,1):
                if (x1*x1*x1 + x2*x2*x2 + x3*x3*x3) == i*i*i:
                    result.append("Cube = "+str(i) +", Triple = (" + str(x1) + "," + str(x2) +","+str(x3)+")")
                    break
for i in result:
    print(i)