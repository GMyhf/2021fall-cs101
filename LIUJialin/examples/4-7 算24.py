# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 18:55:50 2021

@author: 乘一x1
"""
import math
def f(x):
    global dp
    if dp[tuple(x)]:
        return False
    n = len(x)
    if n == 1:
        if math.fabs(x[0]-24)<=0.00001:
            return True
        else:
            return False
    for i in range(n):

        for j in range(n): 
            if i == j:
                continue

            c = []
            for k in range(n):
                if k!=i and k!=j:
                    c.append(x[k])
            c.append(0)

            c[-1] = x[i]+x[j]
            if f(c):
                return True
            else:
                dp[tuple(c)] = 1

            c[-1] = x[i]*x[j]
            if f(c):
                    return True
            else:
                dp[tuple(c)] = 1

            c[-1] = x[i]-x[j]
            if f(c):
                return True
            else:
                dp[tuple(c)] = 1
            if x[j]!=0:
                c[-1] = x[i]/x[j]
                if f(c):
                    return True
                else:
                    dp[tuple(c)] = 1
    return False
result = []
from collections import defaultdict
dp = defaultdict(int)
while True:
    s = [int(x) for x in input().split()]
    if s[0] == 0:
        break
    else:
        result.append(["NO","YES"][f(s)])
print(*result,sep="\n")     
