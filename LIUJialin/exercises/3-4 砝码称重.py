# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 23:03:39 2021

@author: 乘一x1
"""

a1,a2,a3,a4,a5,a6 = [int(x) for x in input().split(" ")]
result = set()
for b1 in range(a1+1):
    for b2 in range(a2+1):
        for b3 in range(a3+1):
            for b4 in range(a4+1):
                for b5 in range(a5+1):
                    for b6 in range(a6+1):
                        result.add(b1+2*b2+3*b3+5*b4+10*b5+20*b6)
print("Total="+str(len(result)-1))