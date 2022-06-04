# -*- coding: utf-8 -*-
# going up
n = int(input())
tri = [[*map(int, input().split())] for _ in range(n)]
for i in range(n-2,-1,-1):
    for j in range(i+1):
        tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
print(tri[0][0])

# going down
n = int(input())
tri = [[0, *map(int, input().split()), 0] for _ in range(n)]
for i in range(1,n):
    for j in range(1,i+2):
        tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
print(max(tri[-1]))

"""info
Created on Tue Nov 23 11:15:44 2021
@author: Asus
http://cs101.openjudge.cn/practice/02760/
02760:数字三角形
总时间限制: 1000ms 内存限制: 65536kB
描述
7
3   8
8   1   0
2   7   4   4
4   5   2   6   5
(图1)
图1给出了一个数字三角形。从三角形的顶部到底部有很多条不同的路径。对于每条路径，把路径上面的数加起来可以得到一个和，你的任务就是找到最大的和。
注意：路径上的每一步只能从一个数走到下一层上和它最近的左边的那个数或者右边的那个数。
输入
输入的是一行是一个整数N (1 < N <= 100)，给出三角形的行数。下面的N行给出数字三角形。数字三角形上的数的范围都在0和100之间。
输出
输出最大的和。
样例输入
5
7
3 8
8 1 0 
2 7 4 4
4 5 2 6 5
样例输出
30

http://cs101.openjudge.cn/practice/01163/
01163:The Triangle  # English_version
总时间限制: 1000ms 内存限制: 65536kB
描述
7
3   8
8   1   0
2   7   4   4
4   5   2   6   5
(Figure 1)
Figure 1 shows a number triangle. Write a program that calculates the highest sum of numbers passed on a route that starts at the top and ends somewhere on the base. Each step can go either diagonally down to the left or diagonally down to the right.
输入
Your program is to read from standard input. The first line contains one integer N: the number of rows in the triangle. The following N lines describe the data of the triangle. The number of rows in the triangle is > 1 but <= 100. The numbers in the triangle, all integers, are between 0 and 99.
输出
Your program is to write to standard output. The highest sum is written as an integer.
样例输入
5
7
3 8
8 1 0 
2 7 4 4
4 5 2 6 5
样例输出
30
"""