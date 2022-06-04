# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 08:13:02 2021

@author: 乘一x1
"""

def f(x):
    for j in range(len(x)-1,0,-1):
        if int(x[j]) > int(x[j-1]):
            for i in range(len(x)-1,0,-1):
                if int(x[i]) > int(x[j-1]):
                            ma = x[i]
                            key = i
                            break
            l1 = []
            l2 = []
            for k in range(0,j,1):
                if k == j-1:
                    l1.append(ma)
                else:
                    l1.append(x[k])
            for k in range(j,len(x),1):
                if k== key:
                    l2.append(x[j-1])
                else:
                    l2.append(x[k])
            l2 = sorted([int(x) for x in l2])
            l2 = [str(x) for x in l2]
            return l1+l2
        elif j ==1:
            return x[::-1]
m = int(input())
out = []
for i in range(m):
    n,k = [int(x) for x in input().split(" ")]
    l = [x for x in input().split(" ")]
    if n == 1:
        out.append(1)
        continue
    for j in range(k):
        l = f(l)
    out.append(" ".join(l))
for i in out:
    print(i)
        
                                   
                  
                
            
        