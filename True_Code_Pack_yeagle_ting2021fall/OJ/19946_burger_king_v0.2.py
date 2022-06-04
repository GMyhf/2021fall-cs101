# -*- coding: utf-8 -*-
m,n = map(int,input().split())
worker = sorted(map(int,input().split()))
burger = sorted(map(int,input().split()))
w = b = ans = 0
while True:
    if worker[w]>=burger[b]:
        ans+=1 ; b+=1
    w+=1
    if w==m or b==n: break
print(ans)

"""
Created on Mon Nov 15 22:35:06 2021
@author: Asus
http://cs101.openjudge.cn/practice/19946/
19946:汉堡王v0.2
总时间限制: 1000ms 内存限制: 65536kB
描述
汉堡王最近新出了一款产品“重装芝牛国王堡”，该汉堡由3层牛排和3层芝士组成。同时它原有的产品也都在生产。
每天店长都会遇到一个问题，如何安排工人来生产汉堡？
因为每个厨师每天只能记住一个食品的配方，而且由于汉堡具有一定的制作难度，每个工人的熟练度不同，只能生产难度低于或等于自己熟练度的汉堡。
现在想请你帮助店长求一下每天最多能生产多少种类的汉堡。
输入
第一行输入两个整数m和n，代表m个工人和n个产品
第二行输入m个整数，代表每个工人的熟练度
第三行输入n个整数，代表每个汉堡的制作难度
输出
每天最多能生产的种类
样例
Sample1 Input:
2 2
1 2
2 1
Sample1 Output:
2

Sample2 Input:
8 5
1 2 3 4 5 6 7 8
5 6 7 8 9
Sample2 Output:
4

Sample3 Input:
4 3
11 12 13 14
21 22 23
Sample3 Output:
0
"""