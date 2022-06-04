# -*- coding: utf-8 -*-
n = int(input())
m = n%4
if n == 0: print(1)
elif m == 0: print(6)
elif m == 1: print(8)
elif m == 2: print(4)
else: print(2)

# shortened with list indexing & comprehension
n = int(input())
print([6,8,4,2,1][n%4 if n!=0 else 4])

"""info
Created on Thu Dec  2 14:25:54 2021
@author: Asus
https://codeforces.com/problemset/problem/742/A
742A-Arpa’s hard exam and Mehrdad’s naive cheat
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

There exists an island called Arpa’s land, some beautiful girls live there, as ugly ones do.
Mehrdad wants to become minister of Arpa’s land. Arpa has prepared an exam. Exam has only one question, given n, print the last digit of 1378n.
Mehrdad has become quite confused and wants you to help him. Please help, although it's a naive cheat.

Input
The single line of input contains one integer n (0  ≤  n  ≤  10**9).
Output
Print single integer — the last digit of 1378n.
Examples
input
1
output
8
input
2
output
4
Note
In the first example, last digit of 1378**1 = 1378 is 8.
In the second example, last digit of 1378**2 = 1378·1378 = 1898884 is 4.
"""