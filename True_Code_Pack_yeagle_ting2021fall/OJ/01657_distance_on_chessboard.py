# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    i,j = input().split()
    if i==j: ans.append('0 0 0 0'); continue
    dx = abs(ord(i[0])-ord(j[0]))
    dy = abs(int(i[1])-int(j[1]))
    k = max(dx,dy)
    if dx==0 or dy==0: r=1
    else: r=2
    if (dx+dy)%2: b='Inf'
    elif dx==dy: b=1
    else: b=2
    if b!='Inf': q = min(r,b)
    else: q = r
    tmp=[str(x) for x in [k,q,r,b]]
    ans.append(' '.join(tmp))
for a in ans: print(a)

"""info #there will be i==j ... bruh...
Created on Sat Oct 16 14:34:25 2021
@author: Asus
http://cs101.openjudge.cn/practice/01657/
01657:Distance on Chessboard
总时间限制: 1000ms 内存限制: 65536kB
描述
国际象棋的棋盘是黑白相间的 8*8 的方格，棋子放在格子中间。如下图所示：
王、后、车、象的走子规则如下：
王：横、直、斜都可以走，但每步限走一格。
后：横、直、斜都可以走，每步格数不受限制。
车：横、竖均可以走，不能斜走，格数不限。
象：只能斜走，格数不限。
写一个程序，给定起始位置和目标位置，计算王、后、车、象从起始位置走到目标位置所需的最少步数。
输入
第一行是测试数据的组数t（0 <= t <= 20）。以下每行是一组测试数据，每组包括棋盘上的两个位置，第一个是起始位置，第二个是目标位置。位置用"字母-数字"的形式表示，字母从"a"到"h"，数字从"1"到"8"。
输出
对输入的每组测试数据，输出王、后、车、象所需的最少步数。如果无法到达,就输出"Inf".
样例输入
2
a1 c3
f5 f8
样例输出
2 1 2 1
3 1 1 Inf
"""