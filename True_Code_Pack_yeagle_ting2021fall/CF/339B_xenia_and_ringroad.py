# -*- coding: utf-8 -*-
n,m = map(int,input().split())
task = [int(x) for x in input().split()]
ans = task[0]-1
for i in range(1,m):
    ti=task[i] ; tp=task[i-1]
    if ti!=tp:
        ans += ti-tp
        if ti<tp: ans += n
print(ans)

"""info
Created on Thu Oct 28 08:40:19 2021
@author: Asus
https://codeforces.com/problemset/problem/339/B
339B-Xenia and Ringroad
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Xenia lives in a city that has n houses built along the main ringroad. The ringroad houses are numbered 1 through n in the clockwise order. The ringroad traffic is one way and also is clockwise.
Xenia has recently moved into the ringroad house number 1. As a result, she's got m things to do. In order to complete the i-th task, she needs to be in the house number ai and complete all tasks with numbers less than i. Initially, Xenia is in the house number 1, find the minimum time she needs to complete all her tasks if moving from a house to a neighboring one along the ringroad takes one unit of time.

Input
The first line contains two integers n and m (2 ≤ n ≤ 10**5, 1 ≤ m ≤ 10**5). The second line contains m integers a1, a2, ..., am (1 ≤ ai ≤ n). Note that Xenia can have multiple consecutive tasks in one house.
Output
Print a single integer — the time Xenia needs to complete all tasks.
Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.
Examples
input
4 3
3 2 3
output
6
input
4 3
2 3 3
output
2
Note
In the first test example the sequence of Xenia's moves along the ringroad looks as follows: 1 → 2 → 3 → 4 → 1 → 2 → 3. This is optimal sequence. So, she needs 6 time units.
"""