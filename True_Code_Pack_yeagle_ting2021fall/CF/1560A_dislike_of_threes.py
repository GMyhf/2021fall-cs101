# -*- coding: utf-8 -*-
ans=[]
like=[0]
for i in range(1,1667):
    if i%3 and str(i)[-1] != '3':
        like += [i]
for _ in range(int(input())):
    ans += [like[int(input())]]
print('\n'.join(map(str, ans)))

"""info
Created on Tue Nov 23 07:57:43 2021
@author: Asus
https://codeforces.com/problemset/problem/1560/A
1560A-Dislike of Threes
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Polycarp doesn't like integers that are divisible by 3 or end with the digit 3 in their decimal representation. Integers that meet both conditions are disliked by Polycarp, too.
Polycarp starts to write out the positive (greater than 0) integers which he likes: 1,2,4,5,7,8,10,11,14,16,…. Output the k-th element of this sequence (the elements are numbered from 1).

Input
The first line contains one integer t (1≤t≤100) — the number of test cases. Then t test cases follow.
Each test case consists of one line containing one integer k (1≤k≤1000).
Output
For each test case, output in a separate line one integer x — the k-th element of the sequence that was written out by Polycarp.
Example
input
10
1
2
3
4
5
6
7
8
9
1000
output
1
2
4
5
7
8
10
11
14
1666
"""