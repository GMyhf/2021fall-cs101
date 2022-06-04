# -*- coding: utf-8 -*-
k,n,w = map(int,input().split())
times = 0
for i in range(w):
    times += i+1
cost = k*times
if cost > n: print(cost-n)
else: print(0)

"""info
Created on Sat Oct  2 12:08:01 2021
@author: Asus
https://codeforces.com/problemset/problem/546/A
A-Soldier and Bananas
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

A soldier wants to buy w bananas in the shop. He has to pay k dollars for the first banana, 2k dollars for the second one and so on (in other words, he has to pay i·k dollars for the i-th banana).
He has n dollars. How many dollars does he have to borrow from his friend soldier to buy w bananas?

Input
The first line contains three positive integers k, n, w (1  ≤  k, w  ≤  1000, 0 ≤ n ≤ 109), the cost of the first banana, initial number of dollars the soldier has and number of bananas he wants.
Output
Output one integer — the amount of dollars that the soldier must borrow from his friend. If he doesn't have to borrow money, output 0.
Examples
input
3 17 4
output
13
"""