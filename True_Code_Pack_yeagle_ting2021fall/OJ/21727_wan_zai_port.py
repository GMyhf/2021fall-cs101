# -*- coding: utf-8 -*-
n,m = map(int,input().split())
brick = [int(x) for x in input().split()]
mx=0 ; ans=0
for i in range(n):
    mx+=brick[i]
    if mx>m: ans=i ; break
    else: ans+=1
print(ans)

"""info
Created on Mon Nov  1 08:09:10 2021
@author: Asus
http://cs101.openjudge.cn/practice/21727/
21727:湾仔码头 (math)
总时间限制: 1000ms 内存限制: 65536kB
描述
小马是打工人，今天他在香港湾仔码头打工，工作内容是搬砖。
他需要把 N 块高分子液体砖中的一部分放入他今天负责的集装箱中，这个集装箱体积为 M。由于薪酬是按件计费，因此小马想搬更多的砖，以得到更多的薪酬。
砖的体积各不相同，且板砖的体积总量不能超过集装箱的体积。
请帮助小马计算他今天最多可以搬多少砖？
输入
输入为第一行为两个数字 N, M (0 < N <= 100, 0 < M <= 1000 )，分别表示码头今天的砖头数量、小马负责的集装箱的体积。
第二行 n 个正整数，第 i 个整数 wi 表示第 i 个高分子液体砖的体积，保证按升序给出所有砖的体积。
输出
每行一个整数，表示小马今天最多可以搬多少砖
样例
sample1 in:
3 100
2 3 99
sample1 out:
2
解释：选择前 2 块砖
sample2 in:
4 155
40 50 60 70
sample2 out:
3
解释：选择前 3 块砖
"""