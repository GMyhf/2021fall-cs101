# -*- coding: utf-8 -*-
m,n,p,q = map(int,input().split())
mat = [[*map(int,input().split())]for _ in range(m)]
con = [[*map(int,input().split())]for _ in range(p)]
ans = [[0]*(n+1-q) for _ in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        for x in range(p):
            for y in range(q):
                ans[i][j] += mat[i+x][j+y]*con[x][y]
for row in ans: print(*row)

"""info
Created on Tue Nov 16 08:36:21 2021
@author: Asus
http://cs101.openjudge.cn/practice/19942/
19942:二维矩阵上的卷积运算v0.2 (matrix) # 2-D matrix convolution calculation
总时间限制: 1000ms 内存限制: 65536kB
描述
二维矩阵上的卷积，是卷积神经网络中经常需要进行的一种运算。该运算在输入的二维矩阵上滑动不同的卷积核，并在每一个滑动的位置上将卷积核与输入图像对应位置的元素进行相乘并逐个求和的运算。下图很好地说明了运算的结果矩阵的每一个位置是如何计算得来的。本题中在行列方向的滑动均以1为步长进行，且输入输出均为整数。
如对第1行第1列，12 = 3*0+3*1+2*2+0*2+0*2+1*0+3*0+1*1+2*2。
输入
第一行4个整数，分别代表二维矩阵的行数和列数m和n以及卷积核的行数和列数p和q
（1 <= p <= m; 1 <= q <= n）
接下来m行，每行为空格分隔的n个整数，代表二维数组中每行的数据。
接下来p行，每行为空格分隔的q个整数，代表卷积核中每行的数据。
输出
易知，p*q的卷积核在m*n的矩阵上以1为步长滑动，横向一共有m+1-p个位置，纵向一共有n+1-q个位置。
因此输出共m+1-p行，每行为以空格分隔的n+1-q个整数，代表卷积运算后的结果。

样例
Sample1 Input:
5 5 3 3
3 3 2 1 0
0 0 1 3 1
3 1 2 2 3
2 0 0 2 2
2 0 0 0 1
0 1 2
2 2 0
0 1 2
Sample1 Output:
12 12 17
10 17 19
9 6 14

Sample2 Input:
5 4 4 4
10 -8 6 9
7 -9 1 0
1 -9 2 -5
-3 6 -1 2
-10 -2 -1 -2
-9 -1 -6 10
3 -2 -5 9
-10 -3 -10 7
3 -2 -7 0 
Sample2 Output:
-46
-77
"""