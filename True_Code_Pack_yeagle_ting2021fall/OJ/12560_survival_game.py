# -*- coding: utf-8 -*-
def game(old,y,x):
    left = x-1 ; right = x+2 ; center = old[y][x]
    n = sum(old[y-1][left:right] + old[y][left:right:2] + old[y+1][left:right])
    if center: c = [0,1][1<n<4]
    else: c = [0,1][n==3]
    return c
n,m = map(int,input().split())
old = [[0]*(m+2),*[[0,*map(int,input().split()),0] for _ in range(n)],[0]*(m+2)]
new = [[0]*(m) for _ in range(n)]
for y in range(1,n+1):
    for x in range(1,m+1):
        new[y-1][x-1] = game(old,y,x)
for row in new: print(*row)
        
"""info
Created on Tue Nov  9 07:45:03 2021
@author: Asus
http://cs101.openjudge.cn/practice/12560/
12560:生存游戏(matrix)
总时间限制: 1000ms 内存限制: 65536kB
描述
有如下生存游戏的规则：
给定一个n*m(1<=n,m<=100)的数组，每个元素代表一个细胞，其初始状态为活着(1)或死去(0)。< p="">
每个细胞会与其相邻的8个邻居（除数组边缘的细胞）进行交互，并遵守如下规则：
任何一个活着的细胞如果只有小于2个活着的邻居，那它就会由于人口稀少死去。
任何一个活着的细胞如果有2个或者3个活着的邻居，就可以继续活下去。
任何一个活着的细胞如果有超过3个活着的邻居，那它就会由于人口拥挤而死去。
任何一个死去的细胞如果有恰好3个活着的邻居，那它就会由于繁殖而重新变成活着的状态。
请写一个函数用来计算所给定初始状态的细胞经过一次更新后的状态是什么。
注意：所有细胞的状态必须同时更新，不能使用更新后的状态作为其他细胞的邻居状态来进行计算。
输入
第一行为n和m，而后n行，每行m个元素，用空格隔开。
输出
n行，每行m个元素，用空格隔开。
样例输入
3 4
0 0 1 1
1 1 0 0
1 1 0 1
样例输出
0 1 1 0
1 0 0 1
1 1 1 0
"""