# -*- coding: utf-8 -*-
n = int(input())
kids = set(map(int, input().split()))
mine = {i for i in range(1, n+1)}
lost = sorted(k for k in mine - kids if k <= n)
more = sorted(a for a in kids - mine)
print(' '.join(map(str, lost)))
print(' '.join(map(str, more)))

n = int(input())
kids = [*map(int, input().split())]
lost, more = [], []
for i in range(1, n+1):
    if i not in kids: lost.append(i)
kids.reverse()
for k in kids:
    if k > n: more.append(k)
more.reverse()
print(' '.join(map(str, lost)))
print(' '.join(map(str, more)))

"""info    # WA, didn't AC in exam
FINAL EXAM on 2021.12.23 (Thu)

Sample Input1:
10
2 6 1 8 4 10 33 1000

Sample Output1:
3 5 7 9
33 1000

Sample Input2:
13
7 8 2 3 1 5 6 13 400 2000

Sample Output2:
4 9 10 11 12
400 2000
"""
