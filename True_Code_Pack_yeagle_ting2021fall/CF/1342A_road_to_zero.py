# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if x == y == 0:
        ans += [0]
    elif 2*a < b:
        ans += [(x+y)*a]
    else:
        ans += [abs(x-y)*a + min(x, y)*b]
print('\n'.join(map(str, ans)))

"""info
Created on Fri Nov 26 08:27:33 2021
@author: Asus
https://codeforces.com/problemset/problem/1342/A
1342A-Road To Zero
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given two integers x and y. You can perform two types of operations:
Pay a dollars and increase or decrease any of these integers by 1. For example, if x=0 and y=7 there are four possible outcomes after this operation:
x=0, y=6;
x=0, y=8;
x=−1, y=7;
x=1, y=7.
Pay b dollars and increase or decrease both integers by 1. For example, if x=0 and y=7 there are two possible outcomes after this operation:
x=−1, y=6;
x=1, y=8.
Your goal is to make both given integers equal zero simultaneously, i.e. x=y=0. There are no other requirements. In particular, it is possible to move from x=1, y=0 to x=y=0.
Calculate the minimum amount of dollars you have to spend on it.

Input
The first line contains one integer t (1≤t≤100) — the number of testcases.
The first line of each test case contains two integers x and y (0≤x,y≤10**9).
The second line of each test case contains two integers a and b (1≤a,b≤10**9).
Output
For each test case print one integer — the minimum amount of dollars you have to spend.

Example
input
2
1 3
391 555
0 0
9 4
output
1337
0
Note
In the first test case you can perform the following sequence of operations: first, second, first. This way you spend 391+555+391=1337 dollars.
In the second test case both integers are equal to zero initially, so you dont' have to spend money.
"""