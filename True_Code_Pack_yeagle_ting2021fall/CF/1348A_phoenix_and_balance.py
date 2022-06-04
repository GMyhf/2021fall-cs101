# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    n = int(input())
    coin = [2**x for x in range(1,n+1)]
    d = coin[-1] + sum(coin[:(n-1)//2]) - sum(coin[(n-1)//2:-1])
    ans += [d]
print('\n'.join(map(str, ans)))

"""info
Created on Wed Dec  1 10:05:33 2021
@author: Asus
https://codeforces.com/problemset/problem/1348/A
1348A-Phoenix and Balance
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Phoenix has n coins with weights 2**1,2**2,…,2**n. He knows that n is even.
He wants to split the coins into two piles such that each pile has exactly n2 coins and the difference of weights between the two piles is minimized. Formally, let a denote the sum of weights in the first pile, and b denote the sum of weights in the second pile. Help Phoenix minimize |a−b|, the absolute value of a−b.

Input
The input consists of multiple test cases. The first line contains an integer t (1≤t≤100) — the number of test cases.
The first line of each test case contains an integer n (2≤n≤30; n is even) — the number of coins that Phoenix has.
Output
For each test case, output one integer — the minimum possible difference of weights between the two piles.
Example
input
2
2
4
output
2
6
Note
In the first test case, Phoenix has two coins with weights 2 and 4. No matter how he divides the coins, the difference will be 4−2=2.
In the second test case, Phoenix has four coins of weight 2, 4, 8, and 16. It is optimal for Phoenix to place coins with weights 2 and 16 in one pile, and coins with weights 4 and 8 in another pile. The difference is (2+16)−(4+8)=6.
"""