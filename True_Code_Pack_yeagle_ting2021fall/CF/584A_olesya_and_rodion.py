# -*- coding: utf-8 -*-
n, t = map(int, input().split())
for i in range(10**(n-1), 10**n):
    if i%t == 0:
        print(i)
        break
else: print(-1)

# another way which is shown by test data
n, t = map(int, input().split())
if t == 10:
    if n < 2:
        print(-1)
    else:
        print('1'*(n-1)+'0')
else:
    print(str(t)*n)

"""info
Created on Sun Nov 28 15:27:20 2021
@author: Asus
https://codeforces.com/problemset/problem/584/A
584A-Olesya and Rodion
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Olesya loves numbers consisting of n digits, and Rodion only likes numbers that are divisible by t. Find some number that satisfies both of them.
Your task is: given the n and t print an integer strictly larger than zero consisting of n digits that is divisible by t. If such number doesn't exist, print  - 1.

Input
The single line contains two numbers, n and t (1 ≤ n ≤ 100, 2 ≤ t ≤ 10) — the length of the number and the number it should be divisible by.
Output
Print one such positive number without leading zeroes, — the answer to the problem, or  - 1, if such number doesn't exist. If there are multiple possible answers, you are allowed to print any of them.

Examples
input
3 2
output
712
"""