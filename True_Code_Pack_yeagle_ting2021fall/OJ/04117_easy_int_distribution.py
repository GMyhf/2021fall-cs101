# -*- coding: utf-8 -*-
ans = []
while True:
    try: n = int(input())
    except EOFError: break
    dp = [[0]*(n+1) for _ in range(n+1)]
    for k in range(n+1):
        dp[k][1] = 1
        dp[0][k] = 1
    for i in range(1, n+1):
        for j in range(2, n+1):
            dp[i][j] = dp[i][j-1]
            if i >= j: dp[i][j] += dp[i-j][j]
    ans.append(dp[n][n])
print('\n'.join(map(str, ans)))

# refer to code of BoHai-Li in 2020fall-cs101.openjudge.cn_problems.pdf

"""info
Created on Fri Dec 17 23:26:58 2021
@author: Asus
http://cs101.openjudge.cn/practice/04117/
04117:简单的整数划分问题
总时间限制: 100ms 内存限制: 65536kB
描述
将正整数n 表示成一系列正整数之和，n=n1+n2+…+nk, 其中n1>=n2>=…>=nk>=1 ，k>=1 。
正整数n 的这种表示称为正整数n 的划分。正整数n 的不同的划分个数称为正整数n 的划分数。
输入
标准的输入包含若干组测试数据。每组测试数据是一个整数N(0 < N <= 50)。
输出
对于每组测试数据，输出N的划分数。
样例输入
5
样例输出
7
提示
5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1
"""