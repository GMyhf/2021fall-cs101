# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:48:22 2021

@author: 乘一x1
"""
import sys
sys.setrecursionlimit(1000000)
direction = [[1,0],[0,1],[-1,0],[0,-1]]
minstep = 1
def f(x_start,y_start,x_end,y_end,step,d):
    global minstep,w,h,l,lmin
    if step >= minstep:
        return
    if (x_start == x_end) and (y_start == y_end):
        minstep = min(minstep,step)
        return
    for i in range(4):
        x_next = x_start + direction[i][0]
        y_next = y_start + direction[i][1]
        if (0<= x_next<=w+1) and (0<= y_next <=h+1):
            if ((l[y_next][x_next] == " ") or (x_next == x_end and y_next==y_end)) and l0[y_next][x_next]:
                l0[y_next][x_next] = False
                if d == i:
                    if step<lmin[y_next][x_next][i]:
                        lmin[y_next][x_next][i] = step
                        f(x_next,y_next,x_end,y_end,step,i)
                else:
                    if step+1<lmin[y_next][x_next][i]:
                        lmin[y_next][x_next][i] = step+1
                        f(x_next,y_next,x_end,y_end,step+1,i)
                l0[y_next][x_next] = True
                
    
cnt1 = 1
while True:
    
    w,h = [int(x) for x in input().split(" ")]
    if w == 0 and h == 0:
         break
    print("Board #"+str(cnt1)+":")
    cnt1+=1
    l = [[" " for i in range(w+2)] for j in range(h+2)]
    for i in range(h):
        s = input()
        for j in range(len(s)):
            l[i+1][j+1] = s[j]
    cnt2 = 1
    while True:
        l0 = [[True for i in range(w+2)] for j in range(h+2)]
        lmin  = [[[float("inf") for k in range(4)]for i in range(w+2)] for j in range(h+2)]
        s = input()
        if s == "0 0 0 0":
            break
        x,y,x_end,y_end = [int(x) for x in s.split()]
        minstep = 1000000
        l0[y][x] = False
        f(x,y,x_end,y_end,0,-1)
        if minstep < 1000000:
                print("Pair " + str(cnt2) +": " +str(minstep) +" segments.")
        else:
                print("Pair " + str(cnt2) +": impossible.")
        cnt2+=1
    print("")