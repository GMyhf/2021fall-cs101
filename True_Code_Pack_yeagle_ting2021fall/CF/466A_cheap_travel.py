# -*- coding: utf-8 -*-
n,m,a,b = map(int,input().split())
if a <= b/m: print(a*n)
else:
    x=n//m
    print(min((x*b+(n-x*m)*a),-(-n//m)*b))

"""info
Created on Fri Oct 22 08:35:16 2021
@author: Asus
https://codeforces.com/problemset/problem/466/A
466A-Cheap Travel
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output
Ann has recently started commuting by subway. We know that a one ride subway ticket costs a rubles. Besides, Ann found out that she can buy a special ticket for m rides (she can buy it several times). It costs b rubles. Ann did the math; she will need to use subway n times. Help Ann, tell her what is the minimum sum of money she will have to spend to make n rides?

Input
The single line contains four space-separated integers n, m, a, b (1 ≤ n, m, a, b ≤ 1000) — the number of rides Ann has planned, the number of rides covered by the m ride ticket, the price of a one ride ticket and the price of an m ride ticket.
Output
Print a single integer — the minimum sum in rubles that Ann will need to spend.
Examples
input
6 2 1 2
outpu
6
input
5 2 2 3
output
8
Note
In the first sample one of the optimal solutions is: each time buy a one ride ticket. There are other optimal solutions. For example, buy three m ride tickets.
"""