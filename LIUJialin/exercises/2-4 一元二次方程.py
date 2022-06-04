# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:39:47 2021

@author: 乘一x1
"""
from math import sqrt
from math import fabs
out=[]
n= int(input())
for i in range(n):
    putin = input().split(" ")
    a = float(putin[0])
    b = float(putin[1])
    c = float(putin[2])
    delta = b*b-4*a*c
    if delta ==0:
        x = round(-b/a/2,5)
        if x==0:
            x = fabs(x)
        out.append((1,x))
    elif delta >0:
        x1 = round((-b+sqrt(delta))/a/2,5)
        x2 = round((-b-sqrt(delta))/a/2,5)
        if x1== 0:
            x1 = fabs(x1)
        if x2 == 0:
            x2 = fabs(x2)
        if x2>x1:
            x3 = x1
            x1 = x2
            x2 = x3
        out.append((2,x1,x2))
    else:
        shibu = round(-b/a/2,5)
        xubu = round(sqrt(-delta)/a/2,5)
        if shibu == 0:
            shibu = fabs(shibu)
        out.append((3,shibu,xubu))
for i in out:
    if i[0] == 1:
        print("x1=x2="+str("%.5f"%i[1]))
    if i[0] == 2:
        print("x1="+"%.5f"%i[1]+";x2="+"%.5f"%i[2])
    if i[0] == 3:
        print("x1=" + str("%.5f"%i[1])+"+"+str("%.5f"%i[2]) +"i;x2=" +str("%.5f"%i[1])+"-"+str("%.5f"%i[2]) +"i")
        
        