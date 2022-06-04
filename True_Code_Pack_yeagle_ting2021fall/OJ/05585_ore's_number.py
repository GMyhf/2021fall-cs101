# -*- coding: utf-8 -*-
ng_4 = ((-1,0),(0,-1),(0,1),(1,0))
def dfs(mtrx, r, c, max_r, max_c, aim):
    at_edge = any((r<0, c<0, r >= max_r, c >= max_c))
    if at_edge or mtrx[r][c] != aim: return
    mtrx[r][c] = '#'
    for k in range(4):
        dfs(mtrx, r + ng_4[k][0], c + ng_4[k][1], max_r, max_c, aim)
ans=[]
for _ in range(int(input())):
    n = int(input())
    red = black = 0
    area = [[*input()] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if area[i][j] == 'r':
                red += 1
                dfs(area, i, j, n, n, 'r')
            elif area[i][j] == 'b':
                black += 1
                dfs(area, i, j, n, n, 'b')
    ans.append('%d %d'%(red, black))
print('\n'.join(map(str, ans)))

"""info
Created on Mon Dec 13 22:23:58 2021
@author: Asus
http://cs101.openjudge.cn/practice/05585/
05585:晶矿的个数
总时间限制: 1000ms 内存限制: 65536kB
描述
在某个区域发现了一些晶矿，已经探明这些晶矿总共有分为两类，为红晶矿和黑晶矿。现在要统计该区域内红晶矿和黑晶矿的个数。假设可以用二维地图m[][]来描述该区域，若m[i][j]为#表示该地点是非晶矿地点，若m[i][j]为r表示该地点是红晶矿地点，若m[i][j]为b表示该地点是黑晶矿地点。一个晶矿是由相同类型的并且上下左右相通的晶矿点组成。现在给你该区域的地图，求红晶矿和黑晶矿的个数。
输入
第一行为k，表示有k组测试输入。
每组第一行为n，表示该区域由n*n个地点组成，3 <= n<= 30
接下来n行，每行n个字符，表示该地点的类型。
输出
对每组测试数据输出一行，每行两个数字分别是红晶矿和黑晶矿的个数，一个空格隔开。
样例输入
2
6
r##bb#
###b##
#r##b#
#r##b#
#r####
######
4
####
#rrb
#rr#
##bb
样例输出
2 2
1 2
"""