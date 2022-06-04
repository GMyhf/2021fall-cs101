# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:53:00 2021

@author: 乘一x1
"""
result = []
while True:
    try:
        s = input()
        result.append(s)
        l = [0 for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == "(":
                l[i] = 1
            elif s[i] == ")":
                l[i] = 2
                if i>0:
                    for j in range(i-1,-1,-1):
                        if l[j] == 1:
                            l[j] = 0
                            l[i] = 0
                            break
        out = ""
        for i in l:
            if i == 1:
                out += "$"
            elif i == 2:
                out += "?"
            else:
                out+=" "
        result.append(out)
        
    except EOFError:
        print(*result,sep="\n")
        break