# -*- coding: utf-8 -*-
mx = [[*map(int, input().split())] for _ in range(5)]
for i in range(5):
    r_max = max(mx[i])
    for j in range(5):
        c_min = min((mx[0][j], mx[1][j], mx[2][j], mx[3][j], mx[4][j]))
        if mx[i][j] == r_max == c_min:
            print(i+1, j+1, mx[i][j]) ; break
    if mx[i][j] == r_max == c_min: break
else: print('not found')

# turn the matrix with *zip(*mx)
mx = [[*map(int, input().split())] for _ in range(5)]
mx_t = [*zip(*mx)]
for i in range(5):
    r_max = max(mx[i])
    for j in range(5):
        c_min = min(mx_t[j])
        saddle = mx[i][j] == r_max == c_min
        if saddle:
            print(i+1, j+1, mx[i][j]) ; break
    if saddle: break
else: print('not found')

#row_max = [r.index(max(r)) for r in mx]
#mx_t = [*zip(*mx)]
#col_min = [c.index(min(c)) for c in mx_t]

"""info
Created on Thu Nov 25 15:29:59 2021
@author: Asus
http://cs101.openjudge.cn/practice/03670/
03670:计算鞍点
总时间限制: 1000ms 内存限制: 65536kB
描述
给定一个5*5的矩阵，每行只有一个最大值，每列只有一个最小值，寻找这个矩阵的鞍点。
鞍点指的是矩阵中的一个元素，它是所在行的最大值，并且是所在列的最小值。
例如：在下面的例子中（第4行第1列的元素就是鞍点，值为8 ）。
11 3 5 6 9
12 4 7 8 10
10 5 6 9 11
8 6 4 7 2
15 10 11 20 25

输入
输入包含一个5行5列的矩阵
输出
如果存在鞍点，输出鞍点所在的行、列及其值，如果不存在，输出"not found"
样例输入
11 3 5 6 9
12 4 7 8 10
10 5 6 9 11
8  6 4 7 2
15 10 11 20 25
样例输出
4 1 8
"""