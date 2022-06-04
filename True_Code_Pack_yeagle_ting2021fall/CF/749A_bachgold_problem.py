# -*- coding: utf-8 -*-
n = int(input())
k = n//2
ans = ['2']*k
if n%2: ans[-1] = '3'
print(k)
print(' '.join(ans))

"""info
Created on Tue Nov 30 07:52:47 2021
@author: Asus
https://codeforces.com/problemset/problem/749/A
749A-Bachgold Problem
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Bachgold problem is very easy to formulate. Given a positive integer n represent it as a sum of maximum possible number of prime numbers. One can prove that such representation exists for any integer greater than 1.
Recall that integer k is called prime if it is greater than 1 and has exactly two positive integer divisors — 1 and k.

Input
The only line of the input contains a single integer n (2 ≤ n ≤ 100 000).
Output
The first line of the output contains a single integer k — maximum possible number of primes in representation.
The second line should contain k primes with their sum equal to n. You can print them in any order. If there are several optimal solution, print any of them.
Examples
input
5
output
2
2 3
input
6
output
3
2 2 2
"""