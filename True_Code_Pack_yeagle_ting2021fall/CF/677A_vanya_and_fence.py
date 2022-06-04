# -*- coding: utf-8 -*-
n,h = map(int,input().split())
f = list(map(int,input().split()))
ans=0
for i in f:
    if i>h: ans+=2
    else: ans+=1
print(ans)

"""info
Created on Mon Oct 18 08:40:22 2021
@author: Asus
https://codeforces.com/problemset/problem/677/A
677A-Vanya and Fence
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Vanya and his friends are walking along the fence of height h and they do not want the guard to notice them. In order to achieve this the height of each of the friends should not exceed h. If the height of some person is greater than h he can bend down and then he surely won't be noticed by the guard. The height of the i-th person is equal to ai.
Consider the width of the person walking as usual to be equal to 1, while the width of the bent person is equal to 2. Friends want to talk to each other while walking, so they would like to walk in a single row. What is the minimum width of the road, such that friends can walk in a row and remain unattended by the guard?

Input
The first line of the input contains two integers n and h (1 ≤ n ≤ 1000, 1 ≤ h ≤ 1000) — the number of friends and the height of the fence, respectively.
The second line contains n integers ai (1 ≤ ai ≤ 2h), the i-th of them is equal to the height of the i-th person.
Output
Print a single integer — the minimum possible valid width of the road.
Examples
    input
        3 7
        4 5 14
    output
        4
    input
        6 1
        1 1 1 1 1 1
    output
        6
    input
        6 5
        7 6 8 9 10 5
    output
        11
Note
In the first sample, only person number 3 must bend down, so the required width is equal to 1 + 1 + 2 = 4.
In the second sample, all friends are short enough and no one has to bend, so the width 1 + 1 + 1 + 1 + 1 + 1 = 6 is enough.
In the third sample, all the persons have to bend, except the last one. The required minimum width of the road is equal to 2 + 2 + 2 + 2 + 2 + 1 = 11.
"""