# -*- coding: utf-8 -*-
N, B = map(int, input().split())
E = [*map(int, input().split())]
M = [*map(int, input().split())]
pair = [*zip(E, M)]
dp = [0]*(B+1)
for i in range(N):
    mass = pair[i][1]
    if mass > B: continue
    earn = pair[i][0]
    for bag in range(B,0,-1):
        if bag >= mass:
            dp[bag] = max(dp[bag], dp[bag-mass] + earn)
print(dp[-1])

"""info
Created on Thu Dec  2 14:55:56 2021
@author: Asus
http://cs101.openjudge.cn/practice/23421/
23421:《算法图解》小偷背包问题
总时间限制: 1000ms 内存限制: 65536kB
描述
这是《算法图解》[1]书中的例子：一个小贼正在一家店里偷商品。
假设一种情况如下：
一个小偷背着一个可装4磅东西的背包。商场有三件物品分别为：
价值3000美元重4磅的音响，价值2000美元重3磅的笔记本，价值1500美元重1磅的吉他。
问小偷应该怎样选择商品，才能使得偷取的价值最高？
[1]Grokking Algorithms by Aditya Bhargava, published by Manning Publications.   Copyright © 2016 by Manning Publications.
Simplified Chinese-language edition copyright © 2017 by Posts & Telecom Press.
输入
第一行是两个整数N和B，空格分隔。N表示物品件数，B表示背包最大承重。
第二行是N个整数，空格分隔。表示各个物品价格。
第三行是N个整数，空格分隔。表示各个物品重量（是与第二行物品对齐的）。
输出
输出一个整数。保证在满足背包容量的情况下，偷的价值最高。
样例输入
3 4
3000 2000 1500
4 3 1
样例输出
3500
"""