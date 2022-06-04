# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- in and out + protected edge
--- some nice operations
--- dfs in matrix
"""

# !!! FIRST OF ALL, BEWARE OF ROW & COL, DON'T GET THEM WRONG !!!

""" template below for in and out + protected edge """
# there is A LOT OF special in & out, don't be just limited to these

# ways to input a matrix
row, col = map(int, input().split())
mtrx = [[*map(int, input().split())] for _ in range(row)]

# protected when input
row, col = map(int,input().split())
edge = [[0]*(col+2)]    # consider what should at edge, 0? 1? -1? inf? ...?
mtrx = edge + [[0,*map(int,input().split()),0]for _ in range(row)] + edge
# this is the best way to insert protected edge for me

''' both of above fit for input like this:
3 4
1 1 1 0
0 1 0 0
1 1 0 0
'''

# ways to output a matrix
# make it simple
for row in mtrx: print(*row)

# if the matrix is proctected, just slice off the edge
for row in mtrx[1:-1]: print(*row[1:-1])

# 02698: eight queen output, http://cs101.openjudge.cn/practice/02698/
def queen8_stack(sol):
    stack = [([0]*8, 0)]
    while stack:
        S, cx = stack.pop()
        if cx == 8:
            sol.append(S[:])
            continue
        for c in range(7, -1, -1):
            for r in range(cx):
                if S[r] == c or abs(S[r]-c) == cx - r: break
            else:
                S[cx] = c
                stack.append((S[:], cx+1))
    return sol
full_sol = queen8_stack([])
# another kind of output a huge string
output=[]
for n in range(92):
    out = [[0]*8 for _ in range(8)]
    for i in range(8): out[ full_sol[n][i] ][i] = 1
    output.append('No. ' + str(n+1))
    for row in out: output.append(' '.join(map(str, row)))
print('\n'.join(output))





""" template below for some nice operations """
# double for loop, going through the matrix
# frequently used on properly protected matrix
for r in range(row):        # range(1, row+1), avoiding protected edge
    for c in range(col):    # range(1, col+1), avoiding protected edge
        'do what you want to do here, examples:'
        mtrx[r][c] = 'something'    # change value first
        if mtrx[r][c] == 'target':    # careful when setting 'target'
            'do something'
        if mtrx[r][c]:    # is something equivalent to bool value 'True'
            'do some pther things'
        mtrx[r][c] = 'something'    # change value later

# get a copy of turned matrix
mtrx_t = [*zip(*mtrx)]
''' example:
1 2 3
4 5 6
7 8 9
if 'mtrx' looks like above, 'mtrx_t' will look like below:
1 4 7
2 5 8
3 6 9
'''

# spiral-matrix: turn in 4-direction
turn = ((0, 1), (1, 0), (0, -1), (-1, 0))    # clock-wise, start going right
turn = ((1, 0), (0, 1), (-1, 0), (0, -1))    # anti-clock, start going down
n = int(input())
r = c = 1 ; t=0
dr, dc = turn[t]
for i in range(1, n**2 +1):
    mtrx[r][c] = i
    if mtrx[r+dr][c+dc]:
        t = (t+1)%4
        dr, dc = turn[t]
    r += dr
    c += dc
# should be used on a properly protected matrix, this is just core structure

# 21462: encrypted praise, http://cs101.openjudge.cn/practice/21462/
n = int(input())
edge = [[-1]*(n+2)]
mtrx = edge+ [[-1, *map(int,input().split()), -1]for _ in range(n)] +edge
turn = ((1, 0), (0, 1), (-1, 0), (0, -1))  # anti-clock, start going down
mssg = ''
r = c = 1 ; t=0
dr, dc = turn[t]
for _ in range(n**2):
    goto = mtrx[r+dr][c+dc]
    if goto == -1: 
        t = (t+1)%4
        dr, dc = turn[t]
        goto = mtrx[r+dr][c+dc]
    mssg += chr(mtrx[r][c])
    if goto == 0: break
    mtrx[r][c] = -1
    r += dr
    c += dc
print(mssg)





""" template below for dfs in matrix """
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

# 8-queen and chinese knight 'ma' move 'ri' refer to dfs_bfs_template.py