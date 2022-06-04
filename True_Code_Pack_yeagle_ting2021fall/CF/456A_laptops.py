# -*- coding: utf-8 -*-
n=int(input())
l=[[int(x) for x in input().split()]for _ in range(n)]
l.sort()
for i in range(len(l)-1):
    if l[i][1] > l[i+1][1]: print('Happy Alex') ; break
else: print('Poor Alex')

"""info
Created on Fri Oct 15 10:36:59 2021
@author: Asus
https://codeforces.com/problemset/problem/456/A
456A-Laptops
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

One day Dima and Alex had an argument about the price and quality of laptops. Dima thinks that the more expensive a laptop is, the better it is. Alex disagrees. Alex thinks that there are two laptops, such that the price of the first laptop is less (strictly smaller) than the price of the second laptop but the quality of the first laptop is higher (strictly greater) than the quality of the second laptop.
Please, check the guess of Alex. You are given descriptions of n laptops. Determine whether two described above laptops exist.

Input
The first line contains an integer n (1 ≤ n ≤ 10**5) — the number of laptops.
Next n lines contain two integers each, ai and bi (1 ≤ ai, bi ≤ n), where ai is the price of the i-th laptop, and bi is the number that represents the quality of the i-th laptop (the larger the number is, the higher is the quality).
All ai are distinct. All bi are distinct.
Output
If Alex is correct, print "Happy Alex", otherwise print "Poor Alex" (without the quotes).
Examples
input
2
1 2
2 1
output
Happy Alex
"""