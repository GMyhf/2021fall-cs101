# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 09:04:43 2021

@author: 乘一x1
"""
while True:
    try:
        n,k = [int(x) for x in input().split()]
        lis = [x for x in range(1,n+1)]
        dp = [[0 for i in range(k+1)] for j in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1,1):
            for j in range(1,k+1,1):
                if i>=j:
                   dp[i][j] = dp[i-j][j] + dp[i-1][j-1]
        print(dp[n][k])            
                
        dp = [0 for i in range(n+1)]
        dp[0] = 1        
        for i in range(1,n+1):
            for j in range(n,i-1,-1):
                dp[j] +=dp[j-i]
        print(dp[n])
        lis = [x for x in range(1,n+1,2)]
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(len(lis)):
            for j in range(lis[i],n+1):
                dp[j] = dp[j]+dp[j-lis[i]]
        print(dp[n])
    except EOFError:
        break
            
