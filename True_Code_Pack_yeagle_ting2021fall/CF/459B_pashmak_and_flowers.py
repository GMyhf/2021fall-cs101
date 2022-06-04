# -*- coding: utf-8 -*-
n = int(input())
b = sorted(map(int, input().split()))
if len(set(b)) == 1:
    print(0, n*(n-1)//2)
else:
    min_b = b[0]
    max_b = b[-1]
    for i in range(1, n):
        if b[i] != min_b:
            n_min = i
            break
    b.reverse()
    for j in range(1, n):
        if b[j] != max_b:
            n_max = j
            break
    print(max_b-min_b, n_max*n_min)

"""info
Created on Fri Dec  3 16:31:16 2021
@author: Asus
https://codeforces.com/problemset/problem/459/B
459B-Pashmak and Flowers
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Pashmak decided to give Parmida a pair of flowers from the garden. There are n flowers in the garden and the i-th of them has a beauty number bi. Parmida is a very strange girl so she doesn't want to have the two most beautiful flowers necessarily. She wants to have those pairs of flowers that their beauty difference is maximal possible!
Your task is to write a program which calculates two things:
The maximum beauty difference of flowers that Pashmak can give to Parmida.
The number of ways that Pashmak can pick the flowers. Two ways are considered different if and only if there is at least one flower that is chosen in the first way and not chosen in the second way.Input
The first line of the input contains n (2 ≤ n ≤ 2·10**5). In the next line there are n space-separated integers b1, b2, ..., bn (1 ≤ bi ≤ 10**9).
Output
The only line of output should contain two integers. The maximum beauty difference and the number of ways this may happen, respectively.
Examples
input
2
1 2
output
1 1
input
3
1 4 5
output
4 1
input
5
3 1 2 3 1
output
2 4
Note
In the third sample the maximum beauty difference is 2 and there are 4 ways to do this:
choosing the first and the second flowers;
choosing the first and the fifth flowers;
choosing the fourth and the second flowers;
choosing the fourth and the fifth flowers.
"""