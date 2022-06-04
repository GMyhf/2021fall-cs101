# -*- coding: utf-8 -*-
m, s = map(int, input().split())
if s == 0:
    if m > 1:
        print('-1 -1')
    else:
        print('0 0')
else:
    big = [0]*m
    s_saved = s
    for i in range(m):
        if s > 9:
            s -= 9
            big[i] = 9
        else:
            big[i] = s
            ib = i
            break
    if s > 9: print('-1 -1')
    else:
        small = [*reversed(big)]
        if not small[0]:
            small[0] = 1
            small[~ib] -= 1
        if sum(big) == s_saved:
            print(''.join(map(str, small)), ''.join(map(str, big)))
        else:
            print('-1 -1')

"""info
Created on Sat Dec  4 20:17:36 2021
@author: Asus
https://codeforces.com/problemset/problem/489/C
489C-Given Length and Sum of Digits...
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You have a positive integer m and a non-negative integer s. Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s. The required numbers should be non-negative integers written in the decimal base without leading zeroes.

Input
The single line of the input contains a pair of integers m, s (1 ≤ m ≤ 100, 0 ≤ s ≤ 900) — the length and the sum of the digits of the required numbers.
Output
In the output print the pair of the required non-negative integer numbers — first the minimum possible number, then — the maximum possible number. If no numbers satisfying conditions required exist, print the pair of numbers "-1 -1" (without the quotes).
Examples
input
2 15
output
69 96
input
3 0
output
-1 -1
"""