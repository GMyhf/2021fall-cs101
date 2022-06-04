# -*- coding: utf-8 -*-
n = int(input())
s = [*map(int,input().split())]
dp = [1]*n
for i in range(n):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))

"""info    # same with 02533:Longest Ordered Subsequence (English version)
Created on Sun Oct 17 13:16:56 2021
@author: Asus

http://cs101.openjudge.cn/practice/02757/
02757:最长上升子序列
总时间限制: 2000ms 内存限制: 65536kB
描述
一个数的序列bi，当b1 < b2 < ... < bS的时候，我们称这个序列是上升的。对于给定的一个序列(a1, a2, ..., aN)，我们可以得到一些上升的子序列(ai1, ai2, ..., aiK)，这里1 <= i1 < i2 < ... < iK <= N。比如，对于序列(1, 7, 3, 5, 9, 4, 8)，有它的一些上升子序列，如(1, 7), (3, 4, 8)等等。这些子序列中最长的长度是4，比如子序列(1, 3, 5, 8).
你的任务，就是对于给定的序列，求出最长上升子序列的长度。
输入
输入的第一行是序列的长度N (1 <= N <= 1000)。第二行给出序列中的N个整数，这些整数的取值范围都在0到10000。
输出
最长上升子序列的长度。
样例输入
7
1 7 3 5 9 4 8
样例输出
4

http://cs101.openjudge.cn/practice/02533/
02533:Longest Ordered Subsequence
总时间限制: 2000ms 内存限制: 65536kB
描述
A numeric sequence of ai is ordered if a1 < a2 < ... < aN. Let the subsequence of the given numeric sequence (a1, a2, ..., aN) be any sequence (ai1, ai2, ..., aiK), where 1 <= i1 < i2 < ... < iK <= N. For example, sequence (1, 7, 3, 5, 9, 4, 8) has ordered subsequences, e. g., (1, 7), (3, 4, 8) and many others. All longest ordered subsequences are of length 4, e. g., (1, 3, 5, 8).
Your program, when given the numeric sequence, must find the length of its longest ordered subsequence.
输入
The first line of input file contains the length of sequence N. The second line contains the elements of sequence - N integers in the range from 0 to 10000 each, separated by spaces. 1 <= N <= 1000
输出
Output file must contain a single integer - the length of the longest ordered subsequence of the given sequence.
样例输入
7
1 7 3 5 9 4 8
样例输出
4
"""