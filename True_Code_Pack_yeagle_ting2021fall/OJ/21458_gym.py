# -*- coding: utf-8 -*-
T, n = map(int, input().split())
plan = [[*map(int, input().split())] for _ in range(n)]
dp = [0]+[-1]*T
for i in range(n):
    time, work = plan[i]
    for t in range(T, 0, -1):
        if t >= time and dp[t-time] != -1:
            dp[t] = max(dp[t], dp[t-time]+work)
print(dp[-1])

"""info
Created on Thu Dec 16 20:04:58 2021
@author: Asus
http://cs101.openjudge.cn/practice/21458/
21458:健身房 (dp)
总时间限制: 1000ms 内存限制: 65536kB
描述
小嘤是大不列颠及北爱尔兰联合王国大力士，为了完成增肌计划，他需要选择一些训练组进行训练：有n个训练组，每天做第i个训练需要耗费ti分钟，每天坚持做第i个训练一个月后预计可增肌wi千克。因为会导致效果变差，小嘤一天不会做相同的训练组多次。由于小嘤是强迫症，他希望每天用于健身的时间恰好为T 分钟，他希望在一个月后获得最多的增肌量，请帮助小嘤计算：他训练一个月后最大增肌量是多少呢？
对应英文描述：
Boingo, a bodybuilder from the United Kingdom of Great Britain and Northern Ireland, needs to choose a number of training sets in order to complete his muscle building program: there are n training groups, and it takes ti minutes per day to do the  i-th training set, and It's expected to gain  wi kilograms of muscle after doing the first i training set every day for one month. Boingo would not do the same training set more than once a day because it's not effective. Since Boingo is obsessive-compulsive, he wants to spend exactly  t minutes per day working out, he wants to gain the maximum amount of muscle mass after one month of training, please help him.
输入
第一行两个整数 T,n。
第 2 行到第 n+1 行，每行两个整数 ti,wi。
保证 0 < ti ≤ T ≤ 10**3, 0 < n ≤ 10**3, 0 < wi < 20。
输出
如果不存在满足条件的训练计划，输出-1。
如果存在满足条件的训练计划，输出一个整数，表示训练一个月后的最大增肌量。

样例
sample1 in
6 4
2 1
4 7
3 5
3 5
sample1 out
10

sample2 in
700 4
450 5
340 1
690 10
9 2
sample2 out
-1
样例2解释：无法找出一种方案满足训练时间恰好等于T.
"""