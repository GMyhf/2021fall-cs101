# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 10:31:22 2021

@author: 乘一x1
"""

while True:
    try:
        n = int(input())
        lis = [x for x in range(1,n+1)]
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(n):
            for j in range(lis[i],n+1):
                dp[j] = dp[j]+dp[j-lis[i]]
        print(dp[n])
    except:
        break