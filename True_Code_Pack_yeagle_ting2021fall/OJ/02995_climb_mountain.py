# -*- coding: utf-8 -*-
n = int(input())
view = [*map(int,input().split())]
dp_up = [1]*n
for i in range(n):
    for j in range(i):
        if view[j] < view[i]:
            dp_up[i] = max(dp_up[i], dp_up[j]+1)
view.reverse()
dp_down = [1]*n
for i in range(n):
    for j in range(i):
        if view[j] < view[i]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)
dp_down.reverse()
dp = [dp_up[x] + dp_down[x]-1 for x in range(n)]
print(max(dp))

# there should be a better way, but this is ok
# application of 02757:longest_ordered_subsequence

"""info
Created on Thu Nov 25 15:13:25 2021
@author: Asus
http://cs101.openjudge.cn/practice/02995/
02995:登山
总时间限制: 5000ms 内存限制: 131072kB
描述
五一到了，PKU-ACM队组织大家去登山观光，队员们发现山上一个有N个景点，并且决定按照顺序来浏览这些景点，即每次所浏览景点的编号都要大于前一个浏览景点的编号。同时队员们还有另一个登山习惯，就是不连续浏览海拔相同的两个景点，并且一旦开始下山，就不再向上走了。队员们希望在满足上面条件的同时，尽可能多的浏览景点，你能帮他们找出最多可能浏览的景点数么？
输入
Line 1： N (2 <= N <= 1000) 景点数
Line 2： N个整数，每个景点的海拔
输出
最多能浏览的景点数
样例输入
8
186 186 150 200 160 130 197 220
样例输出
4
"""