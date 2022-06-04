# -*- coding: utf-8 -*-
n, m, L = map(int, input().split())
def dfs_rec(tree:dict, stud:str, seen, dep:int):
    if dep > L: return seen
    if stud not in seen:
        seen.append(stud)
        if stud in tree:
            for know in tree[stud]:
                dfs_rec(tree, know, seen, dep+1)
    return seen
tree = {}
for _ in range(m):
    x, y = map(int, input().split())
    try:
        tree[x].append(y)
        tree[x].sort()
    except : tree[x] = [y]
    try:
        tree[y].append(x)
        tree[y].sort()
    except : tree[y] = [x]
start = int(input())
print(*dfs_rec(tree, start, [], 0))

"""info    # AC
FINAL EXAM on 2021.12.23 (Thu)

7 7 2
0 1
1 2
2 3
2 4
0 4
0 5
5 6
0

"""