# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 18:59:03 2021

@author: 乘一x1
"""
out1 = []
def f(todo,start,end,between):

    if todo == 1:
        out1.append(start+"->"+end)
    else:
        f(todo-1,start,between,end)
        out1.append(start+"->"+end)
        f(todo-1,between,end,start)
n,a,b,c = input().split(" ")
f(int(n),a,c,b)
out2 = [1]
for i in range(int(n)-1):
    ma = max(out2)
    out2 *= 2
    out2.insert(len(out2)//2,ma+1)
for i in range(len(out1)):
    print(str(out2[i]) + ":"+out1[i])

