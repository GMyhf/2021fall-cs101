# -*- coding: utf-8 -*-
n=int(input()) ; age=[]
for i in range(n): age.append(int(input()))
ans=sum(age)/n ; print('%.2f'%ans)

"""info
Created on Tue Oct  5 08:57:05 2021
@author: Asus
http://cs101.openjudge.cn/practice/2714/
2714:求平均年龄
总时间限制: 1000ms 内存限制: 65536kB
描述
班上有学生若干名，给出每名学生的年龄（整数），求班上所有学生的平均年龄，保留到小数点后两位。
输入
第一行有一个整数n（1<= n <= 100），表示学生的人数。其后n行每行有1个整数，表示每个学生的年龄，取值为15到25。
输出
输出一行，该行包含一个浮点数，为要求的平均年龄，保留到小数点后两位。
样例输入
2
18
17
样例输出
17.50
"""