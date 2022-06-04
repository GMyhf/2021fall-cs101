# -*- coding: utf-8 -*-
n, m1, m2 = map(int, input().split())
mtrx_1 = [[0]*n for _ in range(n)]
mtrx_2 = [[0]*n for _ in range(n)]
for _ in range(m1):
    r, c, v = map(int, input().split())
    mtrx_1[r][c] = v
for _ in range(m2):
    r, c, v = map(int, input().split())
    mtrx_2[r][c] = v
ans = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            ans[i][j] += mtrx_1[i][k]*mtrx_2[k][j]

for r in range(n):
    for c in range(n):
        if ans[r][c]:
            print(r, c, ans[r][c])


"""info    # AC
FINAL EXAM on 2021.12.23 (Thu)

3 3 2
0 0 1
1 0 -1
1 2 3
0 0 7
2 2 1

"""