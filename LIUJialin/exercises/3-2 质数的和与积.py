# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 22:24:00 2021

@author: 乘一x1
"""
S = int(input())
zhishu = []
for i in range(S):
    flag = 1
    for j in range(2,i//2,1):
        if i%j== 0:
            flag = 0
            break
    if flag == 1:
        zhishu.append(i)
a = S//2
b = S-a
while (a!=1) and (b!=S):
    if (a in zhishu) and (b in zhishu):
        print(a*b)
        break
    else:
        a-=1
        b+=1