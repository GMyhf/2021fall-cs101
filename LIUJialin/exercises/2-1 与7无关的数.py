# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:06:07 2021

@author: 乘一x1
"""
n = int(input())
count = 0
for i in range(n+1):
    flag = 1
    if i//10 == 7 or i%7== 0 or i%10==7:
        flag = 0
    if flag == 1:
        count += i*i
print(count)