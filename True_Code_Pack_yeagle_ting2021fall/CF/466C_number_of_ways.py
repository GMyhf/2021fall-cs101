# -*- coding: utf-8 -*-
n = int(input())
a = [*map(int,input().split())]
s = sum(a) ; ans = 0
if s%3==0:
    n1_3 = s/3
    n2_3 = 2*n1_3
    sum_i = match = 0
    for i in range(n-1):
        sum_i += a[i]
        if sum_i == n2_3:
            ans += match
        if sum_i == n1_3:
            match += 1
print(ans)

"""info
Created on Tue Nov  9 09:06:45 2021
@author: Asus
https://codeforces.com/problemset/problem/466/C
466C-Number of Ways
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

You've got array a[1], a[2], ..., a[n], consisting of n integers. Count the number of ways to split all the elements of the array into three contiguous parts so that the sum of elements in each part is the same.
More formally, you need to find the number of such pairs of indices i, j (2 ≤ i ≤ j ≤ n - 1), that .

Input
The first line contains integer n (1 ≤ n ≤ 5·10**5), showing how many numbers are in the array. The second line contains n integers a[1], a[2], ..., a[n] (|a[i]| ≤  10**9) — the elements of array a.
Output
Print a single integer — the number of ways to split the array into three parts with the same sum.
Examples
input
5
1 2 3 0 3
output
2
input
4
0 1 -1 0
output
1
input
2
4 1
output
0
"""