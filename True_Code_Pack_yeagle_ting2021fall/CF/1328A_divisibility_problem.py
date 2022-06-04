# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a<=b: n=b-a
    elif a%b: n=b-(a%b)
    else: n=0
    ans.append(n)
for x in ans: print(x)

"""info
Created on Tue Oct 19 10:06:01 2021
@author: Asus
https://codeforces.com/problemset/problem/1328/A
1328A-Divisibility Problem
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given two positive integers a and b. In one move you can increase a by 1 (replace a with a+1). Your task is to find the minimum number of moves you need to do in order to make a divisible by b. It is possible, that you have to make 0 moves, as a is already divisible by b. You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤104) — the number of test cases. Then t test cases follow.
The only line of the test case contains two integers a and b (1≤a,b≤109).
Output
For each test case print the answer — the minimum number of moves you need to do in order to make a divisible by b.
Example
input
5
10 4
13 9
100 13
123 456
92 46
output
2
5
4
333
0
"""