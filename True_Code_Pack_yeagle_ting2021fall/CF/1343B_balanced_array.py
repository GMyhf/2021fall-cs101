# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    n = int(input())
    if n%4: ans.append(['NO'])
    else:
        even = [*range(2,n+1,2)]
        odd = [*range(1,n,2)]
        odd[-1] += n//2
        x = even + odd
        ans.extend([['YES'],x])
for a in ans: print(*a)

"""info
Created on Wed Nov  3 07:56:43 2021
@author: Asus
https://codeforces.com/problemset/problem/1343/B
1343B-Balanced Array
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given a positive integer n, it is guaranteed that n is even (i.e. divisible by 2).
You want to construct the array a of length n such that:
The first n2 elements of a are even (divisible by 2);
the second n2 elements of a are odd (not divisible by 2);
all elements of a are distinct and positive;
the sum of the first half equals to the sum of the second half (∑i=1n2ai=∑i=n2+1nai).
If there are multiple answers, you can print any. It is not guaranteed that the answer exists.
You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤10**4) — the number of test cases. Then t test cases follow.
The only line of the test case contains one integer n (2≤n≤2⋅105) — the length of the array. It is guaranteed that that n is even (i.e. divisible by 2).
It is guaranteed that the sum of n over all test cases does not exceed 2⋅10**5 (∑n≤2⋅105).
Output
For each test case, print the answer — "NO" (without quotes), if there is no suitable answer for the given test case or "YES" in the first line and any suitable array a1,a2,…,an (1≤ai≤10**9) satisfying conditions from the problem statement on the second line.
Example
input
5
2
4
6
8
10
output
NO
YES
2 4 1 5
NO
YES
2 4 6 8 1 3 5 11
NO
"""