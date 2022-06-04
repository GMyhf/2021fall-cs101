# -*- coding: utf-8 -*-
# refer to https://blog.csdn.net/Li_O_Liu/article/details/105491646
n = int(input())
leri, updo = [0]*(n+1), [1]+[0]*n
for i in range(n):
    leri[i+1] = leri[i] + 2*updo[i]
    updo[i+1] = leri[i] + updo[i]
print(leri[n]+updo[n])

"""info
Created on Wed Dec 22 16:21:57 2021
@author: Asus
http://cs101.openjudge.cn/practice/04103/
04103:踩方格
总时间限制: 1000ms 内存限制: 65536kB
描述
有一个方格矩阵，矩阵边界在无穷远处。我们做如下假设：
a.    每走一步时，只能从当前方格移动一格，走到某个相邻的方格上；
b.    走过的格子立即塌陷无法再走第二次；
c.    只能向北、东、西三个方向走；
请问：如果允许在方格矩阵上走n步，共有多少种不同的方案。2种走法只要有一步不一样，即被认为是不同的方案。
输入
允许在方格上行走的步数n(n <= 20)
输出
计算出的方案数量
样例输入
2
样例输出
7
"""