# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 10:36:26 2021

@author: 乘一x1
"""
result = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        out = 0
        ji = sorted([int(x) for x in input().split()],reverse = True)
        wang = sorted([int(x) for x in input().split()],reverse = True)
        while len(ji)>0:
            if ji[0] < wang[0]:
                out -= 200
                wang.pop(0)
                ji.pop(-1)
            elif ji[0] == wang[0]:
                if ji[-1] > wang[-1]:
                        ji.pop(-1)
                        wang.pop(-1)
                        out += 200
                else:
                        if ji[-1]<wang[0]:
                            out -= 200
                        ji.pop(-1)
                        wang.pop(0)
            else:
                ji.pop(0)
                wang.pop(0)
                out += 200
        result.append(out)
print(*result,sep="\n")
        
        