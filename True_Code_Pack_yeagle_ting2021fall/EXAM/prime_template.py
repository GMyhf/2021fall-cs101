# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- prime numbers
"""

# sieve of eratosthenes, apply it whenever prime numbers needed
def eratosthenes(n):
    isprime = [1]*(n+1)
    for i in range(2, int(n**0.5)+1):
        if isprime[i]:
            for j in range(i*i, n+1, i): isprime[j]=0
    return [x for x in range(2, n+1) if isprime[x]]
# return a list, can be set or something else, depend on what is needed
print(eratosthenes(12))



# refer to 230B-T-primes, https://codeforces.com/problemset/problem/230/B
input()
num = [int(x)**(0.5) for x in input().split()]
mx = int(max(num))
prime = set()
isprime = [1]*(mx-1)
for i in range(2, mx+1):
    if isprime[i-2]:
        prime.update(i)
        for j in range(i*i, mx+1, i): isprime[j-2]=0
for x in num:
    if x in prime: print('YES')
    else: print('NO')



# 18176: 2050 result calculate, http://cs101.openjudge.cn/practice/18176/
n = 10000
isprime = [1]*(n+1)
for i in range(2, int(n**0.5)+1):
    if isprime[i]:
        for j in range(i*i, n+1, i): isprime[j]=0
t_prime = set(x**2 for x in range(2, n+1) if isprime[x])
ans = []
m, n = map(int, input().split())
for _ in range(m):
    sum_mark = 0
    lesson = [*map(int, input().split())]
    for mark in lesson:
        if mark in t_prime:
            sum_mark += mark
    if sum_mark:
        ans.append('%.2f'%(sum_mark/len(lesson)))
    else:
        ans.append('0')
print('\n'.join(ans))



# 03134: goethebach canjecture, http://cs101.openjudge.cn/practice/03143/
ans = []
x = int(input())
if x%2 or x<5:
    print('Error!')
else:
    def eratosthenes(n):
        isprime = [1]*(n+1)
        for i in range(2, int(n**0.5)+1):
            if isprime[i]:
                for j in range(i*i, n+1, i): isprime[j]=0
        return set(x for x in range(2, n+1) if isprime[x])
    x_prime = eratosthenes(x)
    for i in range(2, x//2 +1):
        j = x-i
        if i in x_prime and j in x_prime:
            ans += ['%d=%d+%d'%(x, i, j)]
print('\n'.join(ans))



# 18107: num of prime, http://cs101.openjudge.cn/practice/18107/
def sieve(s, e):
    p_id = [1]*(e+1)
    for i in range(2, int(e**0.5)+1):
        if p_id[i]:
            for j in range(i*i, e+1, i): p_id[j]=0
    if s<2: s = 2
    prime = [x for x in range(s, e+1) if p_id[x]]
    if len(prime): return prime
    else: return [-1]
ans = []
for _ in range(int(input())):
    s, e = map(int, input().split())
    ans.append(sieve(s, e))
for a in ans: print(*a)



# 18159: ones is 1 prime, http://cs101.openjudge.cn/practice/18159/
ns, ans, k = [], [], 0
for _ in range(int(input())): ns.append(int(input()))
def sieve_1(e):
    p_id = [1]*(e+1)
    for i in range(2, int(e**0.5)+1):
        if p_id[i]:
            for j in range(i*i, e+1, i): p_id[j]=0
    return [x for x in range(2, e+1) if p_id[x]]
p_list = sieve_1(max(ns))
for n in ns:
    if n<12: ans.append(['NULL'])
    else:
        tmp = []
        for p in p_list:
            if p<n and p%10==1: tmp.append(p)
            elif p>=n: break
        ans.append(tmp)
for a in ans:
    k += 1
    print('Case%d:'%k)
    print(*a)