# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 01:15:33 2021
@author: 乘一x1
"""

                
out = []
while True:
    cnt = 0
    dict = {}
    a = input()
    if a == "0 0 0 0 0 0":
        break
    else:
        temp = a.split(" ")
        for i in range(6):
            dict[i+1] = int(temp[i])           
        cnt += dict[6] + dict[5] + dict[4]
        remain2 = 5 * dict[4]
        remain1 = 11 * dict[5]
        if dict[3] %4 == 0:
            cnt += dict[3]/4
        else:
            cnt += dict[3]//4 +1
            if dict[3] % 4 == 1:
                remain1 += 7
                remain2 += 5
            elif dict[3] % 4 == 2:
                remain1 += 6
                remain2 += 3
            elif dict[3] % 4 == 3:
                remain1 += 5
                remain2 += 1   
        if remain2 < dict[2]:
             dict[2]-= remain2
             if dict[2]%9==0:
                 cnt += dict[2]/9
             else:
                 cnt += dict[2]//9+1
                 remain1 += (9-dict[2]%9) *4
        else:
            remain1 += (remain2-dict[2])*4
        if remain1 < dict[1]:
            dict[1] -= remain1
            cnt += dict[1]//36
            if dict[1] %36 !=0:
                cnt+= 1
        out.append(int(cnt))
for i in out:
    print(i)   
                 