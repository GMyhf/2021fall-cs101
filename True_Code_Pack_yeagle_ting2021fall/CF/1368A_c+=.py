# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    a, b, n = map(int, input().split())
    k=1
    while a + b <= n:
        if a <= b:
            a += b
        elif b < a:
            b += a
        k += 1
    else: ans += [k]
print('\n'.join(map(str, ans)))

"""info
Created on Thu Nov 25 12:42:11 2021
@author: Asus
https://codeforces.com/problemset/problem/1368/A
1368A-C+=
time limit per test: 2 seconds
memory limit per test: 512 megabytes
input: standard input
output: standard output

Leo has developed a new programming language C+=. In C+=, integer variables can only be changed with a "+=" operation that adds the right-hand side value to the left-hand side variable. For example, performing "a += b" when a = 2, b = 3 changes the value of a to 5 (the value of b does not change).
In a prototype program Leo has two integer variables a and b, initialized with some positive values. He can perform any number of operations "a += b" or "b += a". Leo wants to test handling large integers, so he wants to make the value of either a or b strictly greater than a given value n. What is the smallest number of operations he has to perform?

Input
The first line contains a single integer T (1≤T≤100) — the number of test cases.
Each of the following T lines describes a single test case, and contains three integers a,b,n (1≤a,b≤n≤109) — initial values of a and b, and the value one of the variables has to exceed, respectively.
Output
For each test case print a single integer — the smallest number of operations needed. Separate answers with line breaks.
Example
input
2
1 2 3
5 4 100
output
2
7
Note
In the first case we cannot make a variable exceed 3 in one operation. One way of achieving this in two operations is to perform "b += a" twice.
"""