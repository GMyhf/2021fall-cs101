# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:20:45 2021

@author: 乘一x1
"""

n=int(input())
out = []
m = {0:0,1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
for i in range(n):
    putin = input().split(' ')
    start_month = int(putin[0])
    start_day = int(putin[1])
    start = int(putin[2])
    end_month = int(putin[3])
    end_day = int(putin[4])
    a = 0
    b = 0
    for j in range(start_month):
        a += m[j]
    a+= start_day
    for j in range(end_month):
        b+= m[j]
    b+= end_day
    out.append(start*(2**(b-a)))
for i in out:
    print(i)    
    