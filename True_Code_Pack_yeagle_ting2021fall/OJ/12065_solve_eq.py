# -*- coding: utf-8 -*-
def f(x): return x**3 - 5*x**2 + 10*x - 80
def f1(x): return 3*x**2 - 10*x + 10
x = 0 ; xn = 1
while abs(x-xn) > 1e-10:
    xn = x
    x = x - f(x)/f1(x)
print('%.9f'%x)

"""info
Created on Sat Oct  2 13:42:37 2021
@author: Asus
http://cs101.openjudge.cn/practice/12065/
12065:方程求解
总时间限制: 1000ms 内存限制: 65536kB
描述
求下面方程的根：f(x) = x3- 5x2+ 10x - 80 = 0。
输入
-
输出
精确到小数点后9位。
样例输入
-
样例输出
-
"""