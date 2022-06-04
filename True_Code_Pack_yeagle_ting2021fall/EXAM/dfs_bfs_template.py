# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- matrix
--- 8 queen and chinese knight special
--- graph or tree
"""

""" template below for matrix """
ng_4 = ((-1,0),(0,-1),(0,1),(1,0))
ng_8 = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))

def dfs_ng4(mtrx, r, c, max_r, max_c, aim):    # without protected edge
    at_edge = any((r<0, c<0, r >= max_r, c >= max_c))
    if at_edge or mtrx[r][c] != aim: return
    mtrx[r][c] = '#'    # wipe off the target
    for k in range(4):
        dfs_ng4(mtrx, r + ng_4[k][0], c + ng_4[k][1], max_r, max_c, aim)


def dfs_ng8(mtrx, r, c, max_r, max_c):    # without protected edge
    at_edge = any((r<0, c<0, r >= max_r, c >= max_c))
    if at_edge or mtrx[r][c] != 'W': return
    mtrx[r][c] = '.'    # wipe off the target
    for k in range(8):
        dfs_ng8(mtrx, r + ng_8[k][0], c + ng_8[k][1], max_r, max_c)


area = 0
def dfs_ng8_acc(mtrx, r, c, max_r, max_c):    # without protected edge
    at_edge = any((r<0, c<0, r >= max_r, c >= max_c))
    if at_edge or mtrx[r][c] != 'W': return
    global area
    area += 1    # accumulating wanted data
    mtrx[r][c] = '.'    # wipe off the target
    for k in range(8):
        dfs_ng8_acc(mtrx, r + ng_8[k][0], c + ng_8[k][1], max_r, max_c)



""" template below for 8 queen and chinese knight special """
# 8 queen is classic and harder dfs, learn those easy problems before this
sol=[]
def queen8_rec(S, cx=0):
    if len(sol) > 45: return
    if cx == 8:
        sol.append(''.join([str(i+1) for i in S]))
        return
    for c in range(8):
        for r in range(cx):
            if S[r] == c or abs(S[r]-c) == cx - r: break
        else:
            S[cx] = c
            queen8_rec(S, cx+1)
queen8_rec([0]*8)

full_sol = sol[:] + [*reversed([str(99999999-int(s)) for s in sol])]
# if did not return at len(sol) > 45 , operation above is not needed
# and list 'sol' will contain all answers

# non-recursive (using stack)
def queen8_stack(sol):
    stack = [([0]*8, 0)]
    while stack:
        S, cx = stack.pop()
        if cx == 8:
            sol.append(''.join([str(i+1) for i in S]))
            continue
        for c in range(7, -1, -1):
            for r in range(cx):
                if S[r] == c or abs(S[r]-c) == cx - r: break
            else:
                S[cx] = c
                stack.append((S[:], cx+1))
    return sol
full_sol = queen8_stack([])


# chinese knight 'ma', move in 'ri'
ans = [] ; a = 0
ri_8 = ((2,-1),(2,1),(-2,-1),(-2,1),(-1,-2),(1,-2),(1,2),(-1,2))
def dfs_ri(mtrx, r, c, max_r, max_c, stp):
    if stp == max_r*max_c:
        global a
        a += 1
        return
    for i in range(8):
        dr = r + ri_8[i][0]
        dc = c + ri_8[i][1]
        if not mtrx[dr][dc] and 0 <= dr < max_r and 0 <= dc < max_c:
            mtrx[dr][dc] = 1
            dfs_ri(mtrx, dr, dc, max_r, max_c, stp+1)
            mtrx[dr][dc] = 0
for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    board = [[0]*(10) for _ in range(10)]
    a = 0 ; board[x][y] = 1
    dfs_ri(board, x, y, n, m, 1)
    ans.append(a)
print('\n'.join(map(str, ans)))



""" template below for graph or tree """
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


# 580C-Kefa and Park on codeforces and this is bfs with queue
# graph with double direction
n, maxi = map(int, input().split())
c_01 = [*map(int, input().split())]
cats = { 1 : c_01[0] }
tree = {}
for _ in range(n-1):
    x, y = map(int, input().split())
    try: tree[x].append(y)
    except : tree[x] = [y]
    try: tree[y].append(x)
    except : tree[y] = [x]
path = 0
went = set()
queue = [1]
while queue:
    vrtx = queue.pop(0)
    went.add(vrtx)
    if cats[vrtx] > maxi: continue
    more = False
    for k in tree[vrtx]:
        if k not in went:
            if c_01[k-1]:
                cats[k] = cats[vrtx] +1
            else:
                cats[k] = 0
            queue.append(k)
            more = True
    if not more: path += 1
print(path)