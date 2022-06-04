# -*- coding: utf-8 -*-
n = int(input())
if n%2==0: ans = int(n/2)
else: ans = -(n//2+1)
print(ans)

"""info
Created on Fri Oct  8 07:53:09 2021
@author: Asus
https://codeforces.com/problemset/problem/486/A
486A-Calculating Function
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

For a positive integer n let's define a function f:
f(n) =  - 1 + 2 - 3 + .. + ( - 1)nn
Your task is to calculate f(n) for a given integer n.

Input
The single line contains the positive integer n (1 ≤ n ≤ 1015).
Output
Print f(n) in a single line.
Examples
input
4
output
2
input
5
output
-3
Note
f(4) =  - 1 + 2 - 3 + 4 = 2
f(5) =  - 1 + 2 - 3 + 4 - 5 =  - 3
"""