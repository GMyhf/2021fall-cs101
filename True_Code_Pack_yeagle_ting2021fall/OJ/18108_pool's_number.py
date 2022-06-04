# -*- coding: utf-8 -*-
ans=[]
ng_8 = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
def dfs(mtx, r, c, max_r, max_c):
    at_edge = any((r<0, c<0, r >= max_r, c >= max_c))
    if at_edge or mtx[r][c]!='W': return
    mtx[r][c] = '.'
    for k in range(8):
        dfs(mtx, r + ng_8[k][0], c + ng_8[k][1], max_r, max_c)
for _ in range(int(input())):
    a = 0
    N, M = map(int, input().split())
    farm =  [[*input()] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 'W':
                a += 1
                dfs(farm, i, j, N, M)
    ans += [a]
print('\n'.join(map(str, ans)))

"""info
Created on Tue Nov 30 13:58:06 2021
@author: Asus
http://cs101.openjudge.cn/practice/18108/
18108:池塘数目(matrix,dfs)
总时间限制: 1000ms 内存限制: 65536kB
描述
一场暴雨之后，农田里形成了大大小小的池塘。农田用N×M个格子表示，格子有两种状态，有水('W')和无水('.')。相邻两个有水的格子属于一个池塘，一个格子被视作和它周围八个格子都相邻。
现在需要数出在农田里有多少个池塘。
输入
第一行是一个整数，表示一共有 T 组数据。
每组第一行包含两个整数N和M。
接下来的N行，每行有M个字符('W'或者'.')，表示格子的当前状态。字符之间没有空格。
输出
每组数据对应一行，输出农田里的池塘数目。
样例输入
2
2 2
W.
.W
10 12
W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
.W.W......W.
..W.......W.
样例输出
1
3
"""