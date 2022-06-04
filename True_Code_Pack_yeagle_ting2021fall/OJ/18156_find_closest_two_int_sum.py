# -*- coding: utf-8 -*-
T = int(input())
S = sorted(map(int, input().split()))
temp = best = li = 0
ri = len(S)-1
while li < ri:
    temp = S[li] + S[ri]
    t_df = abs(T-temp)
    b_df = abs(T-best)
    if t_df < b_df:
        best = temp
    if t_df == b_df:
        best = min(best, temp)
    if best == T:
        break
    if temp > T:
        ri -= 1
    elif temp < T:
        li += 1
print(best)

"""info
Created on Sun Dec 12 09:41:27 2021
@author: Asus
http://cs101.openjudge.cn/practice/18156/
18156:寻找离目标数最近的两数之和 (two pointers)
总时间限制: 1000ms 内存限制: 65536kB
描述
给定一组数S（可能包含相同的数），从中选取两个数，使两数之和离目标数T最近。
输入
输入包含两行。
第一行为目标数T。
第二行为S中的N个数字，每个数之间以空格隔开。
注意： 2 <= N <= 100000
输出
输出离T最近的两数之和。
如果存在多个解，则输出数值较小的那个。
样例输入
14
3 7 8 3 9
样例输出
15
"""