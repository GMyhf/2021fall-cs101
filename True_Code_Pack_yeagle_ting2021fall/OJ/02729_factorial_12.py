# -*- coding: utf-8 -*-
import math ; print(math.factorial(int(input())))

#without_math
n=int(input()) ; ans=1
if n<2: print(ans)
else:
    for i in range(1,n+1): ans*=i
    print(ans)

"""info
Created on Sun Oct 17 14:57:52 2021
@author: Asus
http://cs101.openjudge.cn/practice/02729/
02729:求12以内n的阶乘
总时间限制: 1000ms 内存限制: 65536kB
描述
求12以内n的阶乘。
输入
只有一行输入，整数n（n<=12）。
输出
只有一行输出，数值n!。
样例输入
3
样例输出
6
"""