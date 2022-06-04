# -*- coding: utf-8 -*-
g = sorted([int(x) for x in input().split()])
s = sorted([int(c) for c in input().split()])
ans=0 ; i=0
for c in s:
    for x in g[i:]:
        if c>=x: i+=1 ; ans+=1 ; break
print(ans)

"""info
Created on Sun Oct 10 09:10:35 2021
@author: Asus
http://cs101.openjudge.cn/practice/18104/
18104:饼干分配(sorting)
总时间限制: 1000ms 内存限制: 65536kB
描述
在幼儿园里分饼干，每份饼干有不同的重量s(0<=s<=100)。假设每个小孩有一个阈值g(0<=g<=100)，只有得到重量大于等于g的饼干才能满足。饼干与小孩的个数不一定相等(均小于等于100)，最多只能给一个小孩一份饼干，请你计算根据给定的饼干重量和小孩的阈值，来计算最多能有几个小孩得到满足。g和s均为正整数。
输入
两行，第一行为小孩的阈值，不同阈值之间用空格隔开；第二行为饼干的重量，用空格隔开。
输出
一行，即最多能得到满足的小孩个数。
样例输入
1 2 3
1 1
样例输出
1
"""