# -*- coding: utf-8 -*-
N, M = map(int, input().split())
charm = [[*map(int, input().split())]for _ in range(N)]
dp = [0]*(M+1)
for i in range(N):
    wi, di = charm[i]
    if wi > M: continue
    for bag in range(M, 0, -1):
        if bag >= wi:
            dp[bag] = max(dp[bag], dp[bag-wi] + di)
print(dp[-1])

"""info
Created on Thu Dec 23 10:20:47 2021
@author: Asus
http://cs101.openjudge.cn/practice/04131/
04131:Charm Bracelet
http://cs101.openjudge.cn/practice/07113/
07113:Charm Bracelet
(both totally the same)
总时间限制: 1000ms 内存限制: 65536kB
描述
Bessie has gone to the mall's jewelry store and spies a charm bracelet. Of course, she'd like to fill it with the best charms possible from the N(1 ≤ N≤ 3,402) available charms. Each charm iin the supplied list has a weight Wi(1 ≤ Wi≤ 400), a 'desirability' factor Di(1 ≤ Di≤ 100), and can be used at most once. Bessie can only support a charm bracelet whose weight is no more than M(1 ≤ M≤ 12,880).
Given that weight limit as a constraint and a list of the charms with their weights and desirability rating, deduce the maximum possible sum of ratings.
输入
Line 1: Two space-separated integers: N and M
Lines 2..N+1: Line i+1 describes charm i with two space-separated integers: Wi and Di
输出
Line 1: A single integer that is the greatest sum of charm desirabilities that can be achieved given the weight constraints
样例输入
4 6
1 4
2 6
3 12
2 7
样例输出
23
"""