# -*- coding: utf-8 -*-
# edit: if change 'seen' to a set, will be better
# dfs - recursion method
# recursion is usually easier to be understood (for me)
def dfs_rec(tree:dict, stud:str, seen:list):
    if stud not in seen:
        seen.append(stud)
        if stud in tree:
            for know in tree[stud]:
                dfs_rec(tree, know, seen)
    return seen

tree = {}
for _ in range(int(input())):
    link = input().split()
    tree[link[0]] = link[2:]

maxi = 0
for stud in tree:
    seen = dfs_rec(tree, stud, [])
    if '-1' in seen:
        seen.remove('-1')
    maxi = max(maxi, len(seen))
print(maxi)
# another pattern with more return and less indentation
def dfs_rec(tree:dict, stud:str, seen:list):
    if stud in seen: return seen
    seen.append(stud)
    if stud not in tree: return seen
    for know in tree[stud]:
        dfs_rec(tree, know, seen)
    return seen


# dfs - using stack method (non-recursion)
# stack is nice, but its usage is harder to be understood
def dfs_stk(tree:dict, init:str):
    seen = [init]
    stack = [init]
    while stack:
        stud = stack[-1]
        if stud not in seen:
            seen.append(stud)
        if stud not in tree:
            stack.pop()
            continue
        do_pop = True
        for know in tree[stud]:
            if know not in seen:
                stack.append(know)
                do_pop = False
                break
        if do_pop: stack.pop()
    return seen

tree = {}
for _ in range(int(input())):
    link = input().split()
    tree[link[0]] = link[2:]

maxi = 0
for stud in tree:
    seen = dfs_stk(tree, stud)
    if '-1' in seen:
        seen.remove('-1')
    maxi = max(maxi, len(seen))
print(maxi)


# bfs - using queue method (extra, kinda at the top tier of syllabus)
# queue is nice too, differ from stack, but usage is similar concept
def bfs_que(tree:dict, init:str):
    seen = []
    queue = [init]
    while queue:
        stud = queue.pop(0)
        if stud not in seen:
            seen.append(stud)
            if stud in tree:
                for know in tree[stud]:
                    queue.append(know)
    return seen

tree = {}
for _ in range(int(input())):
    link = input().split()
    tree[link[0]] = link[2:]

maxi = 0
for stud in tree:
    seen = bfs_que(tree, stud)
    if '-1' in seen:
        seen.remove('-1')
    maxi = max(maxi, len(seen))
print(maxi)

"""info
Created on Tue Dec 14 10:20:29 2021
@author: Asus
http://cs101.openjudge.cn/practice/21608/
21608:你和你比较熟悉的同学 (dfs, bfs)
总时间限制: 1000ms 内存限制: 65536kB
描述
2020年秋季学期，Henry老师讲授北京大学《计算概论B》课程，其中12班127人，13班37人。临近期末，12月18日做了一个简单的问卷调查。以这种方式做为一次点名，同时也希望了解学生们的一些情况。
问卷内容是：写出自己和脑海中的班里（包括12班、和13班）的另外4名同学的名字。每位同学的名字用一个不重复的正整数表示。如果认识的同学少于4个，也可以少填写。每位同学最多提交1次问卷调查。
根据收集到的结果，形成了一张班级社会网络图 G = (V, E)，如下所示。V是顶点的集合，E是边的集合 。在这个有向图G中，每位同学是一个顶点，边是认识关系。注意认识关系是单向的，即甲认识乙，不代表乙认识甲。
Henry老师想知道在有向图G中，找最大有向子树，所包含的顶点的个数。
【说明：对于一个点，计算从这个点（包括自己）开始沿着有向边能到达的点的数量。】
输入
输入第一行为一个数字 n ( 1 < n <= 200 )，表示调查问卷反馈人数。
第 2 ~ n+1 行是同学之间的认识关系。
每一行中，冒号之前是提交问卷同学名字，之后是认识的同学名字。
-1表示没有熟悉的同学。
冒号及整数，由空格分隔。
输出
输出一个整数。表示找到的最大有向子树，所包含的顶点的个数。

样例
sample1 in:
5
53 : -1
118 : 119 136 137
92 : 107 93 102 91
102 : -1
130 : 66 132 135 103
sample1 out:
5
说明：表示从一个点出发，沿着有向边走，最多5个点连通。
130->66,130->132,130->135,130->103. 五个点包括：130、66、132、135和103.

sample2 in:
13
53 : -1
118 : 119 136 137
92 : 107 93 102 91
102 : -1
130 : 66 132 135 103
42 : 39 40 41
39 : 42 40 41 127
43 : 94
134 : 135 132 131 128
136 : 119 118 176 139
17 : 16 39 42
96 : 81 102 162 101
141 : 142
sample2 out:
7
说明：17->16,17->39,17->42; 39->40,39->41,39->127. 
七个点包括：17、16、39、42、40、41和127.
"""