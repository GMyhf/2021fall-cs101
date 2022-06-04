# -*- coding: utf-8 -*-
ans=0
n, x = map(int,input().split())
for i in range(1,n+1):
    if x%i == 0 and x/i <= n:
        ans += 1
print(ans)

"""info
Created on Sat Nov 20 09:12:40 2021
@author: Asus
https://codeforces.com/problemset/problem/577/A
577A-Multiplication Table
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Let's consider a table consisting of n rows and n columns. The cell located at the intersection of i-th row and j-th column contains number i × j. The rows and columns are numbered starting from 1.
You are given a positive integer x. Your task is to count the number of cells in a table that contain number x.

Input
The single line contains numbers n and x (1 ≤ n ≤ 10**5, 1 ≤ x ≤ 10**9) — the size of the table and the number that we are looking for in the table.
Output
Print a single number: the number of times x occurs in the table.
Examples
input
10 5
output
2
input
6 12
output
4
input
5 13
output
0
Note
A table for the second sample test is given below. The occurrences of number 12 are marked bold.
"""