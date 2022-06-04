# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:52:48 2021

@author: 乘一x1
"""
ans = []
def queen(A): 
    now = len(A)
    if now == 8: 
        ans.append("".join([str(i) for i in A]))
        return
    for col in range(8): 
        for row in range(now): 
            if A[row] == col or abs(col - A[row]) == now - row:
                break
        else: 
                A.append(col) 
                queen(A)
                A.pop(-1)
for i in range(8):
    queen([i])
for i in range(len(ans)):
    print("No.",i+1)
    l = [["0" for i in range(8)] for j in range(8)]
    for j in range(8):
        l[int(ans[i][j])][j] = "1"
    for j in l:
        print(" ".join(j))