# -*- coding: utf-8 -*-
n, m, L = map(int, input().split())
def dls_rec(tree:dict, node:str, seen:list, dep:int):
    if dep > L: return seen
    if node not in seen:
        seen.append(node)
        if node in tree:
            for near in tree[node]:
                dls_rec(tree, near, seen, dep+1)
    return seen
tree = {}
for _ in range(m):
    a, b = map(int, input().split())
    try:
        tree[a].append(b)
        tree[a].sort()
    except : tree[a] = [b]
    try:
        tree[b].append(a)
        tree[b].sort()
    except : tree[b] = [a]
start = int(input())
print(*dls_rec(tree, start, [], 0))

"""info
Created on Tue Dec 28 18:43:35 2021
@author: Asus
http://cs101.openjudge.cn/practice/23558/
23558:有界的深度优先搜索
总时间限制: 1000ms 内存限制: 65536kB
描述
深度优先搜索 (Depth-first Search, DFS) 是一种常用的搜索算法，可以对树或图的节点进行遍历。其过程简要来说是对每一个可能的分支路径深入到不能再深入为止，而且每个节点只能访问一次。在人工智能中，我们有时会将问题抽象为一个用图表示的状态空间，图中的每个节点表示一种状态，节点之间的边表示状态间可以发生转换（简单起见，这里我们认为边是无向的）。例如在下图中，共有0-6七个状态。从节点0开始用DFS算法遍历该图，假设一个节点连接的多个其他节点遍历的顺序为按编号从小到大，则节点的遍历序列为  0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
一些实际问题的状态空间可能很大甚至是无限的，此时DFS算法会沿某条路径无穷地搜索下去，以至于算法无法正常结束。针对这个问题，我们可以使用一种改进的有界深度优先搜索 (Depth-limited Search, DLS) 算法。DLS与DFS的唯一不同点在于其有一个最大深度 L ，在搜索过程中，如果当前路径的搜索深度超过了 L ，则认为当前分支不能继续向下并直接返回。注意，当前分支向下的各节点还可能通过其他路径到达。仍以上图为例，假设最大搜索深度 L=2 ，则其遍历序列为 0 -> 1 -> 2 ->(达到深度界限返回)-> 4 -> 5 -> 6。下图是另一个例子，红色线代表了搜索的顺序。DLS搜索可能无法完全探索状态空间，但能保证正常结束。对于一个给定的图和深度 L ，请你实现DLS算法，并输出从给定节点开始DLS搜索产生的遍历序列。在此问题背景下，遍历序列中不需要包含那些与初始节点不连通的节点。
输入
第一行是三个正整数 n, m, L，表示图的节点个数、边数和最大搜索深度。节点的编号为0到n-1。 n <= 100
接下来 m 行，每行为空格分隔的2个整数 a和 b ，代表顶点 a 和顶点 b 之间有一条无向边相连。输入边不会重复，例如输入 a, b 后，后面的行都不会出现 a, b 和 b, a 。
接下来一行是一个0到n-1的整数，代表搜索的开始节点 start 。
输出
一行由空格分隔的数字（节点编号），即使用DLS算法从 start 节点开始，遍历得到的节点访问序列。对于同一个节点连接的多个其他节点，遍历的顺序为按编号从小到大。

样例
Sample Input1:
7 7 2
0 1
1 2
2 3
2 4
0 4
0 5
5 6
0
Sample Output1:
0 1 2 4 5 6

Sample Input2:
6 8 3
1 0
0 2
1 2
0 4
2 3
4 3
4 5
3 5
1
Sample Output2:
1 0 2 3 4 5

Sample Input3:
6 5 6
0 2
0 1
1 5
0 3
2 3
4
Sample Output3:
4
说明：因为没有结点与4连通。
提示
tags: dfs
"""