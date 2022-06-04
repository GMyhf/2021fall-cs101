# -*- coding: utf-8 -*-
# truely brute force
n = int(input())+1
maxi = 0
for x in range(n):
    for y in range(n):
        for z in range(n):
            if not any(((x+y)%2, (y+z)%3, (x+y+z)%5)):
                maxi = max(maxi, x+y+z)
print(maxi)

"""info
Created on Wed Dec 22 16:55:58 2021
@author: Asus
http://cs101.openjudge.cn/practice/04146/
04146:数字方格
总时间限制: 1000ms 内存限制: 65536kB
描述
如上图，有3个方格，每个方格里面都有一个整数a1，a2，a3。已知0 <= a1, a2, a3 <= n，而且a1 + a2是2的倍数，a2 + a3是3的倍数， a1 + a2 + a3是5的倍数。你的任务是找到一组a1，a2，a3，使得a1 + a2 + a3最大。
输入
一行，包含一个整数n (0 <= n <= 100)。
输出
一个整数，即a1 + a2 + a3的最大值。
样例输入
3
样例输出
5
"""