# -*- coding: utf-8 -*-
# python3 61ms , pypy3-64 77ms
n,a,b,c = map(int,input().split())
dp = [0]+[-4000]*n
cut = {k for k in {a,b,c} if k<=n}
for i in range(min(cut),n+1):
    for x in cut:
        dp[i] = max(dp[i],dp[i-x]+1)
print(dp[n])

# python3 46ms , pypy3-64 77ms
n,a,b,c = map(int,input().split())
dp = [0]+[-4000]*n
cut = set()
for x in {a,b,c}:
    if x<=n: cut.add(x)
for i in range(min(cut),n+1):
    for x in cut:
        dp[i] = max(dp[i],dp[i-x]+1)
print(dp[n])

# make it easier but run slower
n,a,b,c = map(int,input().split())
dp = [0]+[-4000]*n
cut = set((a,b,c))
for i in range(min(cut),n+1):
    for x in cut:
        if i>=x: dp[i] = max(dp[i],dp[i-x]+1)
print(dp[n])

"""info
Created on Sun Oct 31 09:26:45 2021
@author: Asus
https://codeforces.com/problemset/problem/189/A
189A-Cut Ribbon
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:
After the cutting each ribbon piece should have length a, b or c.
After the cutting the number of ribbon pieces should be maximum.
Help Polycarpus and find the number of ribbon pieces after the required cutting.

Input
The first line contains four space-separated integers n, a, b and c (1 ≤ n, a, b, c ≤ 4000) — the length of the original ribbon and the acceptable lengths of the ribbon pieces after the cutting, correspondingly. The numbers a, b and c can coincide.
Output
Print a single number — the maximum possible number of ribbon pieces. It is guaranteed that at least one correct ribbon cutting exists.
Examples
input
5 5 3 2
output
2
input
7 5 5 2
output
2
Note
In the first example Polycarpus can cut the ribbon in such way: the first piece has length 2, the second piece has length 3.
In the second example Polycarpus can cut the ribbon in such way: the first piece has length 5, the second piece has length 2.
"""