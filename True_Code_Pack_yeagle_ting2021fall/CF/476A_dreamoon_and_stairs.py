# -*- coding: utf-8 -*-
n, m = map(int, input().split())
if n < m:
    ans = -1
else:
    for i in range((n+1)//2, n+1):
        if i%m == 0:
            ans = i ; break
print(ans)

"""info
Created on Wed Nov 24 14:51:39 2021
@author: Asus
https://codeforces.com/problemset/problem/476/A
476A-Dreamoon and Stairs
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Dreamoon wants to climb up a stair of n steps. He can climb 1 or 2 steps at each move. Dreamoon wants the number of moves to be a multiple of an integer m.
What is the minimal number of moves making him climb to the top of the stairs that satisfies his condition?

Input
The single line contains two space separated integers n, m (0 < n ≤ 10000, 1 < m ≤ 10).
Output
Print a single integer — the minimal number of moves being a multiple of m. If there is no way he can climb satisfying condition print  - 1 instead.
Examples
input
10 2
output
6
input
3 5
output
-1
Note
For the first sample, Dreamoon could climb in 6 moves with following sequence of steps: {2, 2, 2, 2, 1, 1}.
For the second sample, there are only three valid sequence of steps {2, 1}, {1, 2}, {1, 1, 1} with 2, 2, and 3 steps respectively. All these numbers are not multiples of 5.
"""