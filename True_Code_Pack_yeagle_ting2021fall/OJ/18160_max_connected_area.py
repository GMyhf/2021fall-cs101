# -*- coding: utf-8 -*-
ans=[]
ng_8 = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
area = 0
def dfs(mtrx, r, c, max_r, max_c):
    at_edge = any((r<0, c<0, r >= max_r, c >= max_c))
    if at_edge or mtrx[r][c]!='W': return
    global area
    area += 1
    mtrx[r][c] = '.'
    for k in range(8):
        dfs(mtrx, r + ng_8[k][0], c + ng_8[k][1], max_r, max_c)
for _ in range(int(input())):
    N, M = map(int, input().split())
    board =  [[*input()] for _ in range(N)]
    maxi = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'W':
                area = 0
                dfs(board, i, j, N, M)
                maxi = max(maxi, area)
    ans.append(maxi)
print('\n'.join(map(str, ans)))

"""info
Created on Mon Dec 13 22:49:56 2021
@author: Asus
http://cs101.openjudge.cn/practice/18160/
18160:最大连通域面积(matrix,dfs)
总时间限制: 1000ms 内存限制: 65536kB
描述
一个棋盘上有棋子的地方用（'W'）表示，没有的地方用点来表示，现在要找出其中的最大连通区域，一个格子被视作和它周围八个格子都相邻。
现在需要 找出最大的连通区域的面积是多少，一个格子代表面积为1。
输入
输入的第一行是一个整数，表示一共有 T 组数据。
每组第一行包含两个整数N和M。
接下来的N行，每行有M个字符('W'或者'.')，表示格子的当前状态。字符之间没有空格。
输出
每组数据对应一行，输出最大的连通域的面积，不包含任何空格。
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
2
16
"""