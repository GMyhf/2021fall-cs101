# -*- coding: utf-8 -*-
input()
num = [int(x)**(0.5) for x in input().split()]
mx = int(max(num))
prime = set() ; isprime = [1]*(mx-1)
for i in range(2,mx+1):
    if isprime[i-2]:
        prime.add(i)
        for j in range(i**2,mx+1,i): isprime[j-2]=0
for x in num: print(['NO','YES'][x in prime])
# python3 1622ms , pypy3-64 716ms

#modifying_last_step...
input()
num = [int(x)**(0.5) for x in input().split()]
mx = int(max(num))
prime = set() ; isprime = [1]*(mx-1)
for i in range(2,mx+1):
    if isprime[i-2]:
        prime.update(i)
        for j in range(i**2,mx+1,i): isprime[j-2]=0
for x in num:
    if x in prime: print('YES')
    else: print('NO')

'''sieve of eratosthenes
def eratosthenes(n):
    isprime = [1]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i,n+1,i): isprime[j]=0
    return [x for x in range(2,n+1) if isprime[x]]
print(eratosthenes(12))
'''

"""info
Created on Tue Oct 19 11:59:09 2021
@author: Asus
https://codeforces.com/problemset/problem/230/B
230B-T-primes
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

We know that prime numbers are positive integers that have exactly two distinct positive divisors. Similarly, we'll call a positive integer t Т-prime, if t has exactly three distinct positive divisors.
You are given an array of n positive integers. For each of them determine whether it is Т-prime or not.

Input
The first line contains a single positive integer, n (1 ≤ n ≤ 10**5), showing how many numbers are in the array. The next line contains n space-separated integers xi (1 ≤ xi ≤ 10**12).
Please, do not use the %lld specifier to read or write 64-bit integers in С++. It is advised to use the cin, cout streams or the %I64d specifier.
Output
Print n lines: the i-th line should contain "YES" (without the quotes), if number xi is Т-prime, and "NO" (without the quotes), if it isn't.
Examples
input
3
4 5 6
output
YES
NO
NO
Note
The given test has three numbers. The first number 4 has exactly three divisors — 1, 2 and 4, thus the answer for this number is "YES". The second number 5 has two divisors (1 and 5), and the third number 6 has four divisors (1, 2, 3, 6), hence the answer for them is "NO".
"""