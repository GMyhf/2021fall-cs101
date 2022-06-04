# -*- coding: utf-8 -*-
# refer to https://blog.csdn.net/qq_26919935/article/details/77773688

import sys
sys.setrecursionlimit(100000)
ans = []
def factor(x, y):
    if x == 1: return 1
    if y == 1: return 0
    if x%y: return factor(x, y-1)
    return factor(x//y, y) + factor(x, y-1)
for _ in range(int(input())):
    i = int(input())
    ans.append(factor(i, i))
print('\n'.join(map(str, ans)))

"""info
Created on Mon Dec 20 22:58:45 2021
@author: Asus
http://cs101.openjudge.cn/practice/02749/
02749:分解因数
总时间限制: 1000ms 内存限制: 65536kB
描述
给出一个正整数a，要求分解成若干个正整数的乘积，即a = a1 * a2 * a3 * ... * an，并且1 < a1 <= a2 <= a3 <= ... <= an，问这样的分解的种数有多少。注意到a = a也是一种分解。
输入
第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数a (1 < a < 32768)
输出
n行，每行输出对应一个输入。输出应是一个正整数，指明满足要求的分解的种数
样例输入
2
2
20
样例输出
1
4
"""