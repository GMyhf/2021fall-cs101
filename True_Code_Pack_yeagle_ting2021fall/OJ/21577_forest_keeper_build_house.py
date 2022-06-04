# -*- coding: utf-8 -*-
# refer to https://blog.csdn.net/xuyang0905/article/details/109459022
# core function tranlated from C++
m, n = map(int, input().split())
land = [[0]*(n+2), *[[0, *map(int, input().split())] for _ in range(m)]]
for r in range(1, m+1):
    for c in range(1, n+1):
        if land[r][c]:
            land[r][c] = 0
        else:
            land[r][c] = land[r][c-1] +1
area = 0
for r in range(1, m+1):
    for c in range(1, n+1):
        if land[r][c]:
            wdth = land[r][c]
            area = max(area, wdth)
            for up_r in range(r-1, -1, -1):
                if land[up_r][c]:
                    wdth = min(wdth, land[up_r][c])
                    area = max(area, wdth*(r - up_r +1))
                else: break
print(area)

# brute force with for loop, refer to code of classmate Huang-ZhangYi
m, n = map(int, input().split())
edge = [[1]*(n+2)]
land = edge + [[1,*map(int,input().split()),1]for _ in range(m)] + edge
area = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        for p in range(i, m+2):
            for q in range(j, n+2):
                for k in range(i, p+1):
                    if sum(land[k][j:q+1]): break
                else: area = max(area, (p-i+1)*(q-j+1))
print(area)

"""info
Created on Tue Dec 14 13:18:18 2021
@author: Asus
http://cs101.openjudge.cn/practice/21577/
21577:（201911）护林员盖房子
总时间限制: 1000ms 内存限制: 128000kB
描述
在一片保护林中，护林员想要盖一座房子来居住，但他不能砍伐任何树木。
现在请你帮他计算：保护林中所能用来盖房子的矩形空地的最大面积。
输入
输入：
保护林用一个二维矩阵来表示，长宽都不超过20（即<=20）。
第一行是两个正整数m,n，表示矩阵有m行n列。
然后是m行，每行n个整数，用1代表树木，用0表示空地。
输出
输出：
一个正整数，表示保护林中能用来盖房子的最大矩形空地面积。
样例输入
4 5
0 1 0 1 1
0 1 0 0 1
0 0 0 0 0
0 1 1 0 1
样例输出
5
提示
子矩阵边长可以为1，也就是说：
0 0 0 0 0
依然是一个可以盖房子的子矩阵。
来源
http://www.pkupc.cn/programming/problem/e75ff4fc2e054a39b1c657016433a081/show.do?problemsId=9c77dde2
"""