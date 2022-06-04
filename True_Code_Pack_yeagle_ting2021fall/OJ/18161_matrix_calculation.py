# -*- coding: utf-8 -*-
rowA, colA = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(rowA)]
rowB, colB = map(int, input().split())
B = [[*map(int, input().split())] for _ in range(rowB)]
rowC, colC = map(int, input().split())
C = [[*map(int, input().split())] for _ in range(rowC)]
if colA != rowB or rowA != rowC or colB != colC:
    print('Error!')
else:
    for i in range(rowC):
        for j in range(colC):
            for k in range(colA):
                C[i][j] += A[i][k]*B[k][j]
    for row in C: print(*row)

"""info
Created on Tue Nov 30 09:47:21 2021
@author: Asus
http://cs101.openjudge.cn/practice/18161/
18161:矩阵运算(matrices)
总时间限制: 1000ms 内存限制: 65536kB
描述
现有三个矩阵A, B, C，要求矩阵运算A·B+C并输出结果
矩阵运算介绍：
矩阵乘法运算必须要前一个矩阵的列数与后一个矩阵的行数相同，
如m行n列的矩阵A与n行p列的矩阵B相乘，可以得到m行p列的矩阵C，
矩阵C的每个元素都由A的对应行中的元素与B的对应列中的元素一一相乘并求和得到，
即C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + …… +A[i][n-1]*B[n-1][j]
(C[i][j]表示C矩阵中第i行第j列元素)。
矩阵的加法必须在两个矩阵行数列数均相等的情况下进行，
如m行n列的矩阵A与m行n列的矩阵B相乘，可以得到m行n列的矩阵C，
矩阵C的每个元素都由A与B对应位置的元素相加得到，
即C[i][j] = A[i][j] + B[i][j]
输入
输入分为三部分，分别是A,B,C三个矩阵的内容。
每一部分的第一行为两个整数，代表矩阵的行数row和列数col
接下来row行，每行有col个整数，代表该矩阵这一行的每个元素
输出
如果可以完成矩阵计算，输出计算结果，与输入格式类似，不需要输出行数和列数信息。
如果不能完成矩阵计算，输出"Error!"
样例
Sample Input1:
3 1
0
1
0
1 2
1 1
3 2
3 1
3 1
3 1
Sample Output1:
3 1
4 2
3 1

Sample Input2:
1 1
0
2 1
1
3
1 1
9
Sample Output2:
Error!
提示
sample1 计算过程
| 0 |              | 0 0 |
| 1 | · |1 1| = | 1 1 |
| 0 |              | 0 0 |
| 0 0 |    | 3 1 |     | 3 1 |
| 1 1 | + | 3 1 | = | 4 2 |
| 0 0 |    | 3 1 |     | 3 1 |
"""