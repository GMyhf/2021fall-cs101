# -*- coding: utf-8 -*-
L, M = map(int,input().split())
tree = set() ; cut = set()
for i in range(L+1): tree.add(i)
for i in range(M):
    start, end = map(int,input().split())
    for i in range(start,end+1): cut.add(i)
tree.difference_update(cut)    # tree-=cut (better)
print(len(tree))

"""info
Created on Thu Sep 30 08:54:25 2021
@author: Asus
http://cs101.openjudge.cn/practice/1810/
1810:校门外的树
总时间限制: 1000ms 内存限制: 65536kB
描述
某校大门外长度为L的马路上有一排树，每两棵相邻的树之间的间隔都是1米。我们可以把马路看成一个数轴，马路的一端在数轴0的位置，另一端在L的位置；数轴上的每个整数点，即0，1，2，……，L，都种有一棵树。
马路上有一些区域要用来建地铁，这些区域用它们在数轴上的起始点和终止点表示。已知任一区域的起始点和终止点的坐标都是整数，区域之间可能有重合的部分。现在要把这些区域中的树（包括区域端点处的两棵树）移走。你的任务是计算将这些树都移走后，马路上还有多少棵树。
输入
输入的第一行有两个整数L（1 <= L <= 10000）和 M（1 <= M <= 100），L代表马路的长度，M代表区域的数目，L和M之间用一个空格隔开。接下来的M行每行包含两个不同的整数，用一个空格隔开，表示一个区域的起始点和终止点的坐标。
输出
输出包括一行，这一行只包含一个整数，表示马路上剩余的树的数目。
样例输入
500 3
150 300
100 200
470 471
样例输出
298
"""