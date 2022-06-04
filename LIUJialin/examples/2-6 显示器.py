# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 10:24:11 2021

@author: 乘一x1
"""
out = []
while True:
    s,n = input().split()
    s = int(s)
    if s==0:
        break
    l = [[" " for i in range((s + 2)*len(n)+len(n)-1)] for j in range(2*s+4)]
    row = 0
    for num in n:
        if num == "1":
            for i in range(2*s+3):
                if i!=0 and i != s+1 and i != 2*s+2:
                    l[i][row+s+1] = "|"
        if num == "2":
            for i in range(2*s+3):
                if i == 0 or i == s+1 or i == 2*s+2:
                    for j in range(1,s+1):
                        l[i][row+j] = "-"
                elif 0<i<=s:
                    l[i][row+s+1] = "|"
                else:
                    l[i][row] = "|"
        if num == "3":
            for i in range(2*s+3):
                if i == 0 or i == s+1 or i == 2*s+2:
                    for j in range(1,s+1):
                        l[i][row+j] = "-"
                else:
                    l[i][row+s+1] = "|"
        if num == "4":
            for i in range(2*s+3):
                if i == s+1:
                    for j in range(1,s+1):
                        l[i][row+j] = "-"
                elif 0<i<=s:
                    l[i][row+s+1] = "|"
                    l[i][row] = "|"
                elif s+1<i<2*s+2:
                    l[i][row+s+1] = "|"
        if num == "5":
            for i in range(2*s+3):
                if i == 0 or i == s+1 or i == 2*s+2:
                    for j in range(1,s+1):
                        l[i][row+j] = "-"
                elif i>s+1:
                    l[i][row+s+1] = "|"
                else:
                    l[i][row] = "|"
        if num == "6":
            for i in range(2*s+3):
                if i == 0 or i == s+1 or i == 2*s+2:
                    for j in range(1,s+1):
                        l[i][row+j] = "-"
                elif i>s+1:
                    l[i][row+s+1] = "|"
                    l[i][row] = "|"
                else:
                    l[i][row] = "|"
        if num == "7":
            for i in range(2*s+3):
                if i == 0:
                    for j in range(1,s+1):
                        l[i][row+j] = "-"
                elif i!=s+1 and i != 2*s+2:
                    l[i][row+s+1] = "|"
        if num == "8":
            for i in range(2*s+3):
                if i == 0 or i == s+1 or i == 2*s+2:
                    for j in range(1,s+1):
                        l[i][row+j] = "-"
                elif i>s+1:
                    l[i][row+s+1] = "|"
                    l[i][row] = "|"
                else:
                    l[i][row+s+1] = "|"
                    l[i][row] = "|"
        if num == "9":
            for i in range(2*s+3):
                if i == 0 or i == s+1 or i == 2*s+2:
                    for j in range(1,s+1):
                        l[i][row+j] = "-"
                elif i>s+1:
                    l[i][row+s+1] = "|"
                else:
                    l[i][row+s+1] = "|"
                    l[i][row] = "|"
        if num == "0":
            for i in range(2*s+3):
                if i == 0 or i == 2*s+2:
                    for j in range(1,s+1):
                        l[i][row+j] = "-"
                elif i>s+1:
                    l[i][row+s+1] = "|"
                    l[i][row] = "|"
                elif i<s+1:
                    l[i][row+s+1] = "|"
                    l[i][row] = "|"
        row+=s+3
    
    for i in range(2*s+4):
        out.append(l[i])
for i in out:
    print(*i,sep="")
        