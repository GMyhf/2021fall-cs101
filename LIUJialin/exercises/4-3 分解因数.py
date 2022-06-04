# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 20:50:34 2021

@author: 乘一x1
"""

cnt = 0
def f(mi,number):
    print(mi,number)
    global cnt
    for i in range(mi,number):
        if number%i == 0 and i <= number/i:
                cnt += 1
                f(i,number//i)
for _ in range(int(input())):
    n = int(input())
    l = [0 for i in range(n+1)]
    cnt = 1
    f(2,n)
    print(cnt)        