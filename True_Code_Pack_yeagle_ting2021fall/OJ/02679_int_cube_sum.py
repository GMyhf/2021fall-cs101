# -*- coding: utf-8 -*-
k = int(input())
m = []
for i in range(k+1):
    m.append(i**3)
print(sum(m))

#packed_code
print(sum([i**3 for i in range(int(input())+1)]))

"""info
Created on Fri Oct  1 09:10:26 2021
@author: Asus
http://cs101.openjudge.cn/practice/2679/
2679:整数的立方和
总时间限制: 1000ms 内存限制: 65536kB
描述
给定一个正整数k（1<k<10），求1到k的立方和m。即m=1+2*2*2+…+k*k*k。
输入
输入只有一行，该行包含一个正整数k。
输出
输出只有一行，该行包含1到k的立方和。
样例输入
5 
样例输出
225
"""