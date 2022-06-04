# -*- coding: utf-8 -*-

n_half = int(input())//2 + 1
num = sorted(map(int,input().split()))
m = int(input())
for i in range(n_half):
    x = m-num[i]
    if x > num[-1]+num[-2]:
        print('No') ; break
    if x in num:
        print(num[i],x) ; break
else: print('No')

# time=1087ms? kinda tle?

"""info
Created on Thu Nov  4 14:09:37 2021
@author: Asus
http://cs101.openjudge.cn/practice/04143/
04143:和为给定数
总时间限制: 1000ms 内存限制: 65536kB
描述
给出若干个整数，询问其中是否有一对数的和等于给定的数。
输入
共三行：
第一行是整数n(0 < n <= 100,000)，表示有n个整数。
第二行是n个整数。整数的范围是在0到10^8之间。
第三行是一个整数m（0 <= m <= 2^30)，表示需要得到的和。
输出
若存在和为m的数对，输出两个整数，小的在前，大的在后，中间用单个空格隔开。若有多个数对满足条件，选择数对中较小的数更小的。若找不到符合要求的数对，输出一行No。
样例输入
4
2 5 1 4
6
样例输出
1 5
"""