# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    n=int(input()) ; x=0 ;done=0
    for k in range(1,10):
        for i in range(1,10):
            if i*(int('1'*k))<=n: x+=1
            else: done=1 ; break
        if done: break
    ans.append(str(x))
print('\n'.join(ans))

'''I gave up
ans=[]
for _ in range(int(input())):
    n = int(input()) ; x=0
    if n>111111110:
        k = n//111111111 ; x+= k-k//10
    if n>11111110:
        k = n//11111111 ; x+= k-k//10
    if n>1111110:
        k = n//1111111 ; x+= k-k//10
    if n>111110:
        k = n//111111 ; x+= k-k//10
    if n>11110:
        k = n//11111 ; x+= k-k//10
    if n>1110:
        k = n//1111 ; x+= k-k//10
    if n>110:
        k = n//111 ; x+= k-k//10
    if n>10:
        k = n//11 ; x+= k-k//10
    if n<10: x = n
    else: x += 9
    ans.append(str(x))
print('\n'.join(ans))
'''
"""info
Created on Sat Nov  6 19:19:39 2021
@author: Asus
https://codeforces.com/problemset/problem/1520/B
1520B-Ordinary Numbers
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Let's call a positive integer n ordinary if in the decimal notation all its digits are the same. For example, 1, 2 and 99 are ordinary numbers, but 719 and 2021 are not ordinary numbers.
For a given number n, find the number of ordinary numbers among the numbers from 1 to n.

Input
The first line contains one integer t (1≤t≤10**4). Then t test cases follow.
Each test case is characterized by one integer n (1≤n≤10**9).
Output
For each test case output the number of ordinary numbers among numbers from 1 to n.
Example
input
6
1
2
3
4
5
100
output
1
2
3
4
5
18
"""