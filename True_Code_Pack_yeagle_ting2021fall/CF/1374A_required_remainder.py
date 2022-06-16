# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    x,y,n = map(int,input().split())
    i = n%x
    if i==y: ans.append(n)
    elif i>y: ans.append(n-i+y)
    else: ans.append(n-i-x+y)
print('\n'.join(map(str,ans)))

"""info
Created on Fri Oct 29 09:42:16 2021
@author: Asus
https://codeforces.com/problemset/problem/1374/A
1374A-Required Remainder
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given three integers x,y and n. Your task is to find the maximum integer k such that 0≤k≤n that kmodx=y, where mod is modulo operation. Many programming languages use percent operator % to implement it.
In other words, with given x,y and n you need to find the maximum possible integer from 0 to n that has the remainder y modulo x.
You have to answer t independent test cases. It is guaranteed that such k exists for each test case.

Input
The first line of the input contains one integer t (1≤t≤5⋅10**4) — the number of test cases. The next t lines contain test cases.
The only line of the test case contains three integers x,y and n (2≤x≤10**9; 0≤y<x; y≤n≤109).
It can be shown that such k always exists under the given constraints.
Output
For each test case, print the answer — maximum non-negative integer k such that 0≤k≤n and kmodx=y. It is guaranteed that the answer always exists.
Example
input
7
7 5 12345
5 0 4
10 5 15
17 8 54321
499999993 9 1000000000
10 5 187
2 0 999999999
output
12339
0
15
54306
999999995
185
999999998
Note
In the first test case of the example, the answer is 12339=7⋅1762+5 (thus, 12339mod7=5). It is obvious that there is no greater integer not exceeding 12345 which has the remainder 5 modulo 7.
"""