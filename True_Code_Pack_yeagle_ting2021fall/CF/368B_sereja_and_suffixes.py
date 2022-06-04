# -*- coding: utf-8 -*-
n,m = map(int,input().split())
a = input().split()
a.reverse()
cnt=[] ; dp=set() ; ans=[]
for i in range(n):
    if a[i] not in dp: dp.add(a[i])
    cnt.append(len(dp))
cnt.reverse()
for _ in range(m):
    ans.append(cnt[int(input())-1])
for x in ans: print(x)              # python3 373ms , pypy3-64 810ms

# improved_code : python3 249ms , pypy3-64 733ms
n,m = map(int,input().split())
array = [*reversed(input().split())]
distinct = set()  ;  n_dstt = [0]*n
for i in range(n):
    a = array[i]
    if a not in distinct: distinct.add(a)
    n_dstt[-i-1] = len(distinct)
print('\n'.join([str(n_dstt[int(input())-1]) for _ in range(m)]))

"""info
Created on Thu Oct 28 08:08:09 2021
@author: Asus
https://codeforces.com/problemset/problem/368/B
368B-Sereja and Suffixes
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Sereja has an array a, consisting of n integers a1, a2, ..., an. The boy cannot sit and do nothing, he decided to study an array. Sereja took a piece of paper and wrote out m integers l1, l2, ..., lm (1 ≤ li ≤ n). For each number li he wants to know how many distinct numbers are staying on the positions li, li + 1, ..., n. Formally, he want to find the number of distinct numbers among ali, ali + 1, ..., an.?
Sereja wrote out the necessary array elements but the array was so large and the boy was so pressed for time. Help him, find the answer for the described question for each li.

Input
The first line contains two integers n and m (1 ≤ n, m ≤ 10**5). The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 105) — the array elements.
Next m lines contain integers l1, l2, ..., lm. The i-th line contains integer li (1 ≤ li ≤ n).
Output
Print m lines — on the i-th line print the answer to the number li.

Examples
input
10 10
1 2 3 4 1 2 3 4 100000 99999
1
2
3
4
5
6
7
8
9
10
output
6
6
6
6
6
5
4
3
2
1
"""