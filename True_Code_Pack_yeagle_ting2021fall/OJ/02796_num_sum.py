# -*- coding: utf-8 -*-
num = list(map(int,input().split()))
ans = 0
for i in num[1:]:
    if i<num[0]: ans+=i
print(ans)

#old_code
num = str.split(input())
num = list(map(int, num))
small = []
for i in num[1:]:
    if i < num[0]:
        small.append(i)
    else: pass
print(sum(small))

"""info
Created on Sun Sep 26 14:41:34 2021
@author: Asus
http://cs101.openjudge.cn/practice/2796/
2796:数字求和
总时间限制: 3000ms 内存限制: 65536kB
描述
给定一个正整数a，以及另外的5个正整数，问题是：这5个整数中，小于a的整数的和是多少？
输入
输入一行，只包括6个小于100的正整数，其中第一个正整数就是a。
输出
输出一行，给出一个正整数，是5个数中小于a的数的和。
样例输入
10 1 2 3 4 11
样例输出
10
"""