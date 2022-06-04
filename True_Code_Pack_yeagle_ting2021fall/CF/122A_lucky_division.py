# -*- coding: utf-8 -*-
#fast_code
n = int(input())
for i in{4,7,47,74,447,474,477,747,774}:
    if n%i==0: print('YES') ; break
else: print('NO')

#short_code
n = int(input())
print(['YES','NO'][all(n%i for i in{4,7,47,74,447,474,477,747,774})])

"""info
Created on Sun Oct 10 10:31:59 2021
@author: Asus
https://codeforces.com/problemset/problem/122/A
122A-Lucky Division
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.
Petya calls a number almost lucky if it could be evenly divided by some lucky number. Help him find out if the given number n is almost lucky.

Input
The single line contains an integer n (1 ≤ n ≤ 1000) — the number that needs to be checked.
Output
In the only line print "YES" (without the quotes), if number n is almost lucky. Otherwise, print "NO" (without the quotes).
Examples
    input
        47
    output
        YES
    input
        16
    output
        YES
    input
        78
    output
        NO
Note
Note that all lucky numbers are almost lucky as any number is evenly divisible by itself.
In the first sample 47 is a lucky number. In the second sample 16 is divisible by 4.
"""