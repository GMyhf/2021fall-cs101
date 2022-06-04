# -*- coding: utf-8 -*-
ans = [] ; a = 0
ri_8 = ((2,-1),(2,1),(-2,-1),(-2,1),(-1,-2),(1,-2),(1,2),(-1,2))
def dfs(mtx, r, c, max_r, max_c, stp):
    if stp == max_r*max_c:
        global a
        a += 1
        return
    for i in range(8):
        dr = r + ri_8[i][0]
        dc = c + ri_8[i][1]
        if not mtx[dr][dc] and 0 <= dr < max_r and 0 <= dc < max_c:
            mtx[dr][dc] = 1
            dfs(mtx, dr, dc, max_r, max_c, stp+1)
            mtx[dr][dc] = 0
for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    board = [[0]*(10) for _ in range(10)]
    a = 0 ; board[x][y] = 1
    dfs(board, x, y, n, m, 1)
    ans.append(a)
print('\n'.join(map(str, ans)))

"""info
Created on Thu Dec  2 15:21:20 2021
@author: Asus
http://cs101.openjudge.cn/practice/04123/
04123:马走日
总时间限制: 1000ms 内存限制: 65536kB
描述
马在中国象棋以日字形规则移动。
请编写一段程序，给定n*m大小的棋盘，以及马的初始位置(x，y)，要求不能重复经过棋盘上的同一个点，计算马可以有多少途径遍历棋盘上的所有点。
输入
第一行为整数T(T < 10)，表示测试数据组数。
每一组测试数据包含一行，为四个整数，分别为棋盘的大小以及初始位置坐标n,m,x,y。(0<=x<=n-1,0<=y<=m-1, m < 10, n < 10)
输出
每组测试数据包含一行，为一个整数，表示马能遍历棋盘的途径总数，0为无法遍历一次。
样例输入
1
5 4 0 0
样例输出
32
"""