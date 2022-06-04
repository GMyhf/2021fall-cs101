# -*- coding: utf-8 -*-
a, b, c = map(int, input().split())
solve, mx, my = 0, c//a, c//b
for x in range(mx+1):
    for y in range(my+1):
        if a*x + b*y == c: solve += 1
print(solve)

"""info
Created on Wed Dec 22 20:36:22 2021
@author: Asus
http://cs101.openjudge.cn/practice/04139/
04139:不定方程求解
总时间限制: 1000ms 内存限制: 65536kB
描述
给定正整数a，b，c。求不定方程 ax+by=c 关于未知数x和y的所有非负整数解组数。
输入
一行，包含三个正整数a，b，c，两个整数之间用单个空格隔开。每个数均不大于1000。
输出
一个整数，即不定方程的非负整数解组数。
样例输入
2 3 18
样例输出
4
"""