# -*- coding: utf-8 -*-
def pFactors(n):
    """Finds the prime factors of 'n'"""
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n
    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num /= check
    if num > 1:
        pFact.append(num)
    return pFact
n = int(input())
if n == 1: print(1)
else:
    memo = pFactors(n)
    x = len(memo)
    if len(memo) != len(set(memo)): print(0)
    else:
        print([1,-1][x%2])


"""info    # AC
FINAL EXAM on 2021.12.23 (Thu)



"""