# -*- coding: utf-8 -*-
ans = []
for _ in range(int(input())):
    ans += [[1]*(int(input()))]
for a in ans: print(*a)

# oneline_code
for a in [[1]*(int(input())) for _ in range(int(input()))]: print(*a)

"""info
Created on Thu Nov 25 12:57:03 2021
@author: Asus
https://codeforces.com/problemset/problem/1372/A
1372A-Omkar and Completion
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You have been blessed as a child of Omkar. To express your gratitude, please solve this problem for Omkar!
An array a of length n is called complete if all elements are positive and don't exceed 1000, and for all indices x,y,z (1≤x,y,z≤n), ax+ay≠az (not necessarily distinct).
You are given one integer n. Please find any complete array of length n. It is guaranteed that under given constraints such array exists.

Input
Each test contains multiple test cases. The first line contains t (1≤t≤1000)  — the number of test cases. Description of the test cases follows.
The only line of each test case contains one integer n (1≤n≤1000).
It is guaranteed that the sum of n over all test cases does not exceed 1000.
Output
For each test case, print a complete array on a single line. All elements have to be integers between 1 and 1000 and for all indices x,y,z (1≤x,y,z≤n) (not necessarily distinct), ax+ay≠az must hold.
If multiple solutions exist, you may print any.
Example
input
2
5
4
output
1 5 3 77 12
384 384 44 44
Note
It can be shown that the outputs above are valid for each test case. For example, 44+44≠384.
Below are some examples of arrays that are NOT complete for the 1st test case:
[1,2,3,4,5]
Notice that a1+a2=a3.
[1,3000,1,300,1]
Notice that a2=3000>1000.
"""