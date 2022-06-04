# -*- coding: utf-8 -*-
n,m = map(int,input().split())
tv = sorted(t for t in map(int,input().split()) if t<0)
print(-sum(tv[:m]))

"""info
Created on Wed Nov 17 08:03:54 2021
@author: Asus
https://codeforces.com/problemset/problem/34/B
34B-Sale
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Once Bob got to a sale of old TV sets. There were n TV sets at that sale. TV set with index i costs ai bellars. Some TV sets have a negative price — their owners are ready to pay Bob if he buys their useless apparatus. Bob can «buy» any TV sets he wants. Though he's very strong, Bob can carry at most m TV sets, and he has no desire to go to the sale for the second time. Please, help Bob find out the maximum sum of money that he can earn.

Input
The first line contains two space-separated integers n and m (1 ≤ m ≤ n ≤ 100) — amount of TV sets at the sale, and amount of TV sets that Bob can carry. The following line contains n space-separated integers ai ( - 1000 ≤ ai ≤ 1000) — prices of the TV sets.
Output
Output the only number — the maximum sum of money that Bob can earn, given that he can carry at most m TV sets.
Examples
input
5 3
-6 0 35 -2 4
output
8
input
4 2
7 0 0 -7
output
7
"""