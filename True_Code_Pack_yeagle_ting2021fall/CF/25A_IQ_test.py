# -*- coding: utf-8 -*-
input()
mod=[int(x)%2 for x in input().split()]
if sum(mod)==1: print(mod.index(1)+1)
else: print(mod.index(0)+1)

#old_code
n=input() ; odd=0 ; even=0
num = [int(x) for x in input().split()]
for x in num:
    if odd==2 or even==2: break
    elif x%2!=0: odd+=1
    else: even+=1
if odd==2:
    for x in num:
        if x%2==0: print(num.index(x)+1)
else:
    for x in num:
        if x%2!=0: print(num.index(x)+1)

"""info #if use sum, can't deal with oddsum
Created on Sat Oct  9 11:49:05 2021
@author: Asus
https://codeforces.com/problemset/problem/25/A
25A-IQ test
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given n numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given n numbers finds one that is different in evenness.

Input
The first line contains integer n (3 ≤ n ≤ 100) — amount of numbers in the task. The second line contains n space-separated natural numbers, not exceeding 100. It is guaranteed, that exactly one of these numbers differs from the others in evenness.
Output
Output index of number that differs from the others in evenness. Numbers are numbered from 1 in the input order.
Examples
    input
        5
        2 4 7 8 10
    output
        3
    input
        4
        1 2 1 1
    output
        2
"""