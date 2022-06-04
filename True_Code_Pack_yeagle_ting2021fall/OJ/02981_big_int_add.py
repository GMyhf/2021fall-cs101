# -*- coding: utf-8 -*-
num=[]
for n in range(2):
    num.append(input())
a=int(num[0]) ; b=int(num[1])
print(a+b)

#short, fastest?:
a=int(input()) ; b=int(input())
print(a+b)

#even shorter:
print(int(input())+int(input()))

"""info
Created on Sat Sep 25 10:58:21 2021
@author: Asus
http://cs101.openjudge.cn/practice/2981/
2981:大整数加法
总时间限制: 1000ms 内存限制: 65536kB
描述
求两个不超过200位的非负整数的和。
输入
有两行，每行是一个不超过200位的非负整数，可能有多余的前导0。
输出
一行，即相加后的结果。结果里不能有多余的前导0，即如果结果是342，那么就不能输出为0342。
样例输入
22222222222222222222
33333333333333333333
样例输出
55555555555555555555
"""

