# -*- coding: utf-8 -*-
n = int(input())
edge = [[1]*(n+2)]
mx = edge + [[1, *[0]*n, 1] for _ in range(n)] + edge
turn = [(0, 1), (1, 0), (0, -1), (-1, 0)]
y = x = 1 ; t=0
dy, dx = turn[t]
for num in range(1, n**2 +1):
    mx[y][x] = num
    if mx[y+dy][x+dx]:
        t = (t+1)%4
        dy, dx = turn[t]
    y += dy
    x += dx
for row in mx[1:-1]: print(*row[1:-1])

"""info
Created on Tue Nov 23 13:09:31 2021
@author: Asus
http://cs101.openjudge.cn/practice/18106/
18106:螺旋矩阵(matrix)
总时间限制: 1000ms 内存限制: 65536kB
描述
给定一个n(1<=n<=20)，生成一个n*n的二维数组，并用1到n^2对该数组用螺旋顺序进行填充。
如给定n=3时，生成的数组如下：
[
[ 1, 2, 3 ],
[ 8, 9, 4 ],
[ 7, 6, 5 ]
]
输入
一行n
输出
n行，每行n个元素，并用空格将数组元素隔开。
样例输入
3
样例输出
1 2 3
8 9 4
7 6 5
"""