# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- create graph or tree from input
--- related dfs and bfs function
"""

""" template below for create graph or tree from input """
tree = {}
for _ in range(int(input())):
    link = input().split()
    tree[link[0]] = link[2:]
    # fit for input like this: 118 : 119 136 137
    # tree[xxx] = yyy, need to be matched with input format


# from 580C-Kefa and Park on codeforces
n = int(input())
tree = {}
for _ in range(n-1):
    x, y = map(int, input().split())
    try: tree[x].append(y)
    except : tree[x] = [y]
    try: tree[y].append(x)
    except : tree[y] = [x]
    # fit for input like this: 1 2
    # graph with double direction

""" template below for related dfs and bfs function """
# 'stud' and 'init' do not limit in str,can be int or something else

def dfs_rec(tree:dict, stud:str, seen:dict):
    if stud not in seen:
        seen.add(stud)
        if stud in tree:
            for know in tree[stud]:
                dfs_rec(tree, know, seen)
    return seen

# another pattern with more return and less indentation
def dfs_rec_2(tree:dict, stud:str, seen:dict):
    if stud in seen: return seen
    seen.add(stud)
    if stud not in tree: return seen
    for know in tree[stud]:
        dfs_rec_2(tree, know, seen)
    return seen


# dfs - using stack method (non-recursion)
# stack is nice, but its usage is harder to be understood
def dfs_stk(tree:dict, init:str):
    seen = {init}
    stack = [init]
    while stack:
        stud = stack[-1]
        if stud not in seen:
            seen.add(stud)
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


# bfs - using queue method (extra, kinda at the top tier of syllabus)
# queue is nice too, differ from stack, but usage is similar concept
def bfs_que(tree:dict, init:str):
    seen = set()
    queue = [init]
    while queue:
        stud = queue.pop(0)
        if stud not in seen:
            seen.add(stud)
            if stud in tree:
                for know in tree[stud]:
                    queue.append(know)
    return seen