# -*- coding: utf-8 -*-
# code modified from 2020fall_cs101.openjudge.cn_problems.pdf
# WARNING: This is a VERY HARD problem, please be awared.

def dfs(i:int, a:int, x:int):
    if dp[i][a] != -1:
        return dp[i][a]
    high = plat[i][2]
    left = right = 40000001
    safe = True
    for j in range(i+1, N+1):
        fall = high - plat[j][2]
        if fall > MAX:
            safe = False ; break
        le_j = plat[j][0]
        ri_j = plat[j][1]
        if le_j <= x <= ri_j:
            left = dfs(j, 0, le_j) + fall + x - le_j
            right = dfs(j, 1, ri_j) + fall + ri_j - x
            safe = False ; break
    dp[i][a] = min(left, right)
    if safe and high <= MAX: dp[i][a] = high
    return dp[i][a]

ans=[]
for _ in range(int(input())):
    N, X, Y, MAX = map(int, input().split())
    dp = [[-1, -1] for _ in range(1010)]
    plat = [[X, X, Y]]
    for _ in range(N):
        plat.append([*map(int, input().split())])
    plat.sort(key = lambda x:x[2], reverse=True)
    ans.append(dfs(0, 1, X))
print('\n'.join(map(str, ans)))

"""info
Created on Thu Dec  2 16:05:32 2021
@author: Asus
http://cs101.openjudge.cn/practice/01661/
01661:帮助 Jimmy
总时间限制: 1000ms 内存限制: 65536kB
描述
"Help Jimmy" 是在下图所示的场景上完成的游戏。
场景中包括多个长度和高度各不相同的平台。地面是最低的平台，高度为零，长度无限。
Jimmy老鼠在时刻0从高于所有平台的某处开始下落，它的下落速度始终为1米/秒。当Jimmy落到某个平台上时，游戏者选择让它向左还是向右跑，它跑动的速度也是1米/秒。当Jimmy跑到平台的边缘时，开始继续下落。Jimmy每次下落的高度不能超过MAX米，不然就会摔死，游戏也会结束。
设计一个程序，计算Jimmy到底地面时可能的最早时间。
输入
第一行是测试数据的组数t（0 <= t <= 20）。每组测试数据的第一行是四个整数N，X，Y，MAX，用空格分隔。N是平台的数目（不包括地面），X和Y是Jimmy开始下落的位置的横竖坐标，MAX是一次下落的最大高度。接下来的N行每行描述一个平台，包括三个整数，X1[i]，X2[i]和H[i]。H[i]表示平台的高度，X1[i]和X2[i]表示平台左右端点的横坐标。1 <= N <= 1000，-20000 <= X, X1[i], X2[i] <= 20000，0 < H[i] < Y <= 20000（i = 1..N）。所有坐标的单位都是米。
Jimmy的大小和平台的厚度均忽略不计。如果Jimmy恰好落在某个平台的边缘，被视为落在平台上。所有的平台均不重叠或相连。测试数据保证问题一定有解。
输出
对输入的每组测试数据，输出一个整数，Jimmy到底地面时可能的最早时间。
样例输入
1
3 8 17 20
0 10 8
0 10 13
4 14 3
样例输出
23
"""