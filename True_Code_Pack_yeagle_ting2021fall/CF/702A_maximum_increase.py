# -*- coding: utf-8 -*-
n = int(input())
*a, = map(int,input().split())
dp = [1]*n
for i in range(1,n):
    if a[i-1] < a[i]:
        dp[i] += dp[i-1]
print(max(dp))

# using variable and slower(maybe) code
n = int(input())
*a, = map(int,input().split())
dp = [1]*n
k = 1
for i in range(1,n):
    if a[i-1] < a[i]:
        k += 1
        dp[i] = k
    else:
        k = 1
print(max(dp))

"""info
Created on Sun Nov 21 08:40:53 2021
@author: Asus
https://codeforces.com/problemset/problem/702/A
702A-Maximum Increase
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given array consisting of n integers. Your task is to find the maximum length of an increasing subarray of the given array.
A subarray is the sequence of consecutive elements of the array. Subarray is called increasing if each element of this subarray strictly greater than previous.

Input
The first line contains single positive integer n (1 ≤ n ≤ 10**5) — the number of integers.
The second line contains n positive integers a1, a2, ..., an (1 ≤ ai ≤ 10**9).
Output
Print the maximum length of an increasing subarray of the given array.
Examples
input
5
1 7 2 11 15
output
3
input
6
100 100 100 100 100 100
output
1
input
3
1 2 3
output
3
"""