# -*- coding: utf-8 -*-
# refer to code of GMyhf
import math
n_r = {}
for i in range(1001):
    n_r[i] = math.factorial(i)
def nCr(n:int, r:int):
    return n_r[n] // n_r[r] // n_r[n-r]
ans = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans.append(nCr(b, a))
print('\n'.join(map(str, ans)))

# refer to code of classmate WangZiYiDian
import sys
fac = [1]
for i in range(1, 1001):
    fac.append(fac[-1]*i)
for i in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    if 2*a < b: a = b-a
    ans = fac[b] // fac[a] // fac[b-a]
    sys.stdout.write('%d\n'%ans)

# TLE old code...
from math import comb
ans=[]
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans.append(comb(b, a))
print('\n'.join(map(str, ans)))

"""info
Created on Mon Dec 13 20:52:21 2021
@author: Asus
http://cs101.openjudge.cn/practice/19971/
19971:组合数
总时间限制: 1000ms 内存限制: 65536kB
描述
给定A,B 算C(A,B)  (0<=a<=b<=1000)
输入
第一行为一个整数t，t<=100000
接下来t行每行两个整数a,b
输出
t行共t个整数，为每一组（a,b）对应的组合数
样例输入
3
2 4
10 34
2 7
样例输出
6
131128140
21
"""