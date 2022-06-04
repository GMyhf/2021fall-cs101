# -*- coding: utf-8 -*-
t = int(input())
ans=[]
for a in range(t):
    a = int(input())
    if 360%(180-a)==0:
        ans.append('YES')
    else: ans.append('NO')
for x in ans: print(x)

"""info
Created on Wed Sep 29 12:28:43 2021
@author: Asus
https://codeforces.com/problemset/problem/270/A
270A-Fancy Fence
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Emuskald needs a fence around his farm, but he is too lazy to build it himself. So he purchased a fence-building robot.
He wants the fence to be a regular polygon. The robot builds the fence along a single path, but it can only make fence corners at a single angle a.
Will the robot be able to build the fence Emuskald wants? In other words, is there a regular polygon which angles are equal to a?

Input
The first line of input contains an integer t (0 < t < 180) — the number of tests. Each of the following t lines contains a single integer a (0 < a < 180) — the angle the robot can make corners at measured in degrees.
Output
For each test, output on a single line "YES" (without quotes), if the robot can build a fence Emuskald wants, and "NO" (without quotes), if it is impossible.
Examples
    input
        3
        30
        60
        90
    output
        NO
        YES
        YES
Note
In the first test case, it is impossible to build the fence, since there is no regular polygon with angle 30.
In the second test case, the fence is a regular triangle, and in the last test case — a square.
"""