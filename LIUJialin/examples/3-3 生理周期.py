# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 11:05:54 2021

@author: 乘一x1
"""
k = 1
while True:
        p,e,j,d = [int(x) for x in input().split()]
        if p == -1:
            break
        d0 = d+1
        p %= 23
        e %= 28
        j %= 33
        while True:
            if d0%23 == p and d0%28 == e and d0%33 == j:
                print("Case "+str(k) +": the next triple peak occurs in " + str(d0-d) + " days.")
                break
            else:
                d0 += 1
        k+= 1
