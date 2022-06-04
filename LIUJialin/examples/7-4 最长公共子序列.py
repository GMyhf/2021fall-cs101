# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 19:26:55 2021

@author: 乘一x1
"""

while True:
    try:
        s1,s2 = input().split()
        dp = [[0] + [0 for i in range(len(s2))] for j in range(1+len(s1))]
        for i in range(1,1+len(s1)):
            for j in range(1,1+len(s2)):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        print(dp[-1][-1])
    except:
        break