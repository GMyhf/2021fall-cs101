# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 16:35:19 2021

@author: 乘一x1
"""
file = []
out = []
result = []
file0 = []
level = 1
cnt = 1
flag = True
while True:
    s = input()
    if s == "#":
        break
    if flag:
        print("DATA SET "+str(cnt)+":")
        cnt += 1
        print("ROOT")
        flag = False
    if s == "*":
        flag = True
        for i in out:
            s = ""
            s+="|     "*(i[1]-1)
            s+=i[0]
            print(s)
        print(*sorted(file),sep="\n")
        out = []
        file = []
        level = 1
        print("")
        continue
    if s[0] == "f":
        if level == 1:
            file.append(s)
        else:
            file0.append((s,level))
    elif s[0] == "]":
        for i in sorted(file0):
            if i[1] == level:
                out.append(i)
        file0 = [i for i in file0 if i[1]!=level]
        level -= 1
    elif s[0] == "d":
        level += 1
        out.append((s,level))

            