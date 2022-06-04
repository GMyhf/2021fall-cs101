# -*- coding: utf-8 -*-
R, C = map(int, input().split())
path = [[0]*(C+2) for _ in range(R+2)]  #dp
edge = [[10001]*(C+2)]
hill = edge+ [[10001,*map(int, input().split()),10001]for _ in range(R)] +edge
ng_4 = ((-1,0), (1,0), (0,-1), (0,1))
def ski(hill, i, j):
    if path[i][j] > 0: return path[i][j]
    for d in ng_4:
        dr = d[0] ; dc = d[1]
        if hill[i+dr][j+dc] < hill[i][j]:
            path[i][j] = max(path[i][j], ski(hill, i+dr, j+dc)+1)  #dp
    return path[i][j]
ans = 0
for r in range(1, R+1):
    for c in range(1, C+1):
        ans = max(ans, ski(hill, r, c))
print(ans+1)

"""info
Created on Wed Dec  1 12:44:32 2021
@author: Asus
http://cs101.openjudge.cn/practice/01088/
01088:滑雪
总时间限制: 1000ms 内存限制: 65536kB
描述
Michael喜欢滑雪百这并不奇怪， 因为滑雪的确很刺激。可是为了获得速度，滑的区域必须向下倾斜，而且当你滑到坡底，你不得不再次走上坡或者等待升降机来载你。Michael想知道载一个区域中最长的滑坡。区域由一个二维数组给出。数组的每个数字代表点的高度。下面是一个例子
 1  2  3  4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
一个人可以从某个点滑向上下左右相邻四个点之一，当且仅当高度减小。在上面的例子中，一条可滑行的滑坡为24-17-16-1。当然25-24-23-...-3-2-1更长。事实上，这是最长的一条。
输入
输入的第一行表示区域的行数R和列数C(1 <= R,C <= 100)。下面是R行，每行有C个整数，代表高度h，0<=h<=10000。
输出
输出最长区域的长度。
样例输入
5 5
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
样例输出
25
"""