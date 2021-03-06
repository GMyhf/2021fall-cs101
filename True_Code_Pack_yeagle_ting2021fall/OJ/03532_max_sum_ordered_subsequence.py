# -*- coding: utf-8 -*-
n = int(input())
*s, = map(int, input().split())
dp = [0]*n
for i in range(n):
    dp[i] = s[i]
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[i], dp[j]+s[i])
print(max(dp))

# make it a liitle better
n = int(input())
*s, = map(int, input().split())
dp = list(s)
for i in range(n):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[i], dp[j]+s[i])
print(max(dp))

"""info
Created on Mon Nov 22 14:14:05 2021
@author: Asus
http://cs101.openjudge.cn/practice/03532/
03532:最大上升子序列和
总时间限制: 1000ms 内存限制: 65536kB
描述
一个数的序列bi，当b1 < b2 < ... < bS的时候，我们称这个序列是上升的。对于给定的一个序列(a1, a2, ...,aN)，我们可以得到一些上升的子序列(ai1, ai2, ..., aiK)，这里1 <= i1 < i2 < ... < iK <= N。比如，对于序列(1, 7, 3, 5, 9, 4, 8)，有它的一些上升子序列，如(1, 7), (3, 4, 8)等等。这些子序列中序列和最大为18，为子序列(1, 3, 5, 9)的和.
你的任务，就是对于给定的序列，求出最大上升子序列和。注意，最长的上升子序列的和不一定是最大的，比如序列(100, 1, 2, 3)的最大上升子序列和为100，而最长上升子序列为(1, 2, 3)
输入
输入的第一行是序列的长度N (1 <= N <= 1000)。第二行给出序列中的N个整数，这些整数的取值范围都在0到10000（可能重复）。
输出
最大上升子序列和
样例输入
7
1 7 3 5 9 4 8
样例输出
18
"""