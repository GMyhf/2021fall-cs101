# -*- coding: utf-8 -*-
from math import ceil
n,k = map(int,input().split())
a = k%2==0 and k>n/2
b = k%2!=0 and k>=(n/2)+1
if a or b: print(2*(k-ceil(n/2)))
else: print(2*k-1)

"""info
time limit exceeded: 1000000000000 500000000001 (solved.modify code)
round(19075990.5) = 19075990 ?!?!? (solved-math.ceil)
Created on Fri Oct  8 08:03:27 2021
@author: Asus
https://codeforces.com/problemset/problem/318/A
318A-Even Odds
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Being a nonconformist, Volodya is displeased with the current state of things, particularly with the order of natural numbers (natural number is positive integer number). He is determined to rearrange them. But there are too many natural numbers, so Volodya decided to start with the first n. He writes down the following sequence of numbers: firstly all odd integers from 1 to n (in ascending order), then all even integers from 1 to n (also in ascending order). Help our hero to find out which number will stand at the position number k.

Input
The only line of input contains integers n and k (1 ≤ k ≤ n ≤ 1012).
Please, do not use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specifier.
Output
Print the number that will stand at the position number k after Volodya's manipulations.
Examples
    input
        10 3
    output
        5
    input
        7 7
    output
        6
Note
In the first sample Volodya's sequence will look like this: {1, 3, 5, 7, 9, 2, 4, 6, 8, 10}. The third place in the sequence is therefore occupied by the number 5.
"""