# -*- coding: utf-8 -*-
# refer to sample code
import math
def quantile(data, n, q):
    mid = (n-1)*q
    le = math.floor(mid)
    ri = math.ceil(mid)
    if le == ri:
        return data[int(mid)]
    d_le = data[le] * (ri-mid)
    d_ri = data[ri] * (mid-le)
    return d_le + d_ri
n = int(input())
data = sorted(map(float, input().split()))
for q in (0.25, 0.5, 0.75):
    print('%.2f'%quantile(data, n, q))

# something wrong with this code and I don't know why...
def quantile(data, n, q):
    target = (n-1)*q
    i = int(target)
    if target%1:
        ans = (data[i] + data[i+1])/2
    else:
        ans = data[i]
    return ans
n = int(input())
data = sorted(map(float, input().split()))
for q in (0.25, 0.5, 0.75):
    print('%.2f'%quantile(data, n, q))

"""info
Created on Mon Nov 22 15:57:12 2021
@author: Asus
http://cs101.openjudge.cn/practice/12555/
12555:寻找四分位数v0.2(math)
总时间限制: 1000ms 内存限制: 65536kB
描述
四分位数，即统计学中，把所有数值由小到大排列并分成四等份，处于三个分割点位置的数值就是四分位数（定义见下图中R7）。
现给定样本有n个数（当作浮点数处理），输出其四分位数，要求保留两位小数。
输入
输入的第一行是一个整数n (1<= n <= 300000)。
第二行包含n个浮点数，中间用空格隔开。
输出
输出为三行，每行包含一个数。分别为较小四分位数（Q1），中位数（Q2），较大四分位数（Q3）。
样例输入
15
7 20 16 6 58 9 20 50 23 33 8 10 15 16 104
样例输出
9.50
16.00
28.00
提示
本题是针对样本计算四分位数。计算方法是 https://en.wikipedia.org/wiki/Quantile
中的R7.
"""