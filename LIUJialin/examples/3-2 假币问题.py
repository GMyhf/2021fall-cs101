# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:35:07 2021

@author: 乘一x1
"""

n = int(input())
for i in range(n):
    true = set()
    result = set()
    for j in range(3):
        s = input()
        result.add(s)
    for x in "ABCDEFGHIJKL":
        flag = 1
        for j in result:
            j = j.split()
            if x in j[0]:
                if j[2] != "up":
                    flag = 0
                    break
            elif x in j[1]:
                if j[2] != "down":
                    flag = 0
                    break
        if flag ==1:
            print(x+" is the counterfeit coin and it is heavy.")
            break
        flag = 1
        for j in result:
            j = j.split()
            if x in j[0]:
                if j[2] != "down":
                    flag = 0
                    break
            elif x in j[1]:
                if j[2] != "up":
                    flag = 0
                    break
        if flag ==1:
            print(x+" is the counterfeit coin and it is light.")
            break
                
            