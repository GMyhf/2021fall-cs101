# -*- coding: utf-8 -*-
n = int(input())
tumor = [[*map(int,input().split())] for _ in range(n)]
outside = 255*n
inside = 255*(n-2)
border = 1
row = 0
for i in tumor:
    si = sum(i)
    if si == border:
        break
    if si == inside:
        row += 1
    elif si != outside:
        len_t = (outside - si)//255 -2
        border = si 
print(row*len_t)

"""info
Created on Mon Nov 22 21:40:29 2021
@author: Asus
http://cs101.openjudge.cn/practice/02713/
02713:肿瘤面积
总时间限制: 1000ms 内存限制: 65536kB
描述
在一个正方形的灰度图片上，肿瘤是一块矩形的区域，肿瘤的边缘所在的像素点在图片中用0表示。其它肿瘤内和肿瘤外的点都用255表示。现在要求你编写一个程序，计算肿瘤内部的像素点的个数（不包括肿瘤边缘上的点）。已知肿瘤的边缘平行于图像的边缘。
输入
只有一个测试样例。第一行有一个整数n，表示正方形图像的边长。其后n行每行有n个整数，取值为0或255。整数之间用一个空格隔开。已知n不大于1000。
输出
输出一行，该行包含一个整数，为要求的肿瘤内的像素点的个数。
样例输入
5
255 255 255 255 255
255 0 0 0 255
255 0 255 0 255
255 0 0 0 255
255 255 255 255 255
样例输出
1
提示
如果使用静态数组来表示图片数据，需要将该数组定义成全局变量。
"""