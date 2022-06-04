# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    input()
    array=[int(x) for x in input().split()]
    s = set(array)
    for x in s:
        if array.count(x)==1:
            ans.append(array.index(x)+1)
for a in ans: print(a)

"""info
Created on Tue Nov  2 20:21:00 2021
@author: Asus
https://codeforces.com/problemset/problem/1512/A
1512A-Spy Detected!
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given an array a consisting of n (n≥3) positive integers. It is known that in this array, all the numbers except one are the same (for example, in the array [4,11,4,4] all numbers except one are equal to 4).
Print the index of the element that does not equal others. The numbers in the array are numbered from one.

Input
The first line contains a single integer t (1≤t≤100). Then t test cases follow.
The first line of each test case contains a single integer n (3≤n≤100) — the length of the array a.
The second line of each test case contains n integers a1,a2,…,an (1≤ai≤100).
It is guaranteed that all the numbers except one in the a array are the same.
Output
For each test case, output a single integer — the index of the element that is not equal to others.
Example
input
4
4
11 13 11 11
5
1 4 4 4 4
10
3 3 3 3 10 3 3 3 3 3
3
20 20 10
output
2
1
5
3
"""