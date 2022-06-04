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
            ans[i][j] += mtrx_1[i][k] * mtrx_2[k][j]
for r in range(n):
    for c in range(n):
        if ans[r][c]: print(r, c, ans[r][c])

"""info
Created on Tue Dec 28 17:02:10 2021
@author: Asus
http://cs101.openjudge.cn/practice/23555/
23555:节省存储的矩阵乘法
总时间限制: 1000ms 内存限制: 65536kB
描述
由于矩阵存储非常耗费空间，一个长度n宽度m的矩阵需要花费n*m的存储，因此我们选择用另一种节省空间的方法表示矩阵。一个矩阵X可以表示为三元组的序列，每个三元组代表（行号，列号，元素值），如果元素值是0则我们不存储这个三元组，这样对于0很多的大型矩阵，我们节省了很多存储空间。现在我们有两个用这种方式表示的矩阵X和Y，我们想要计算这两个矩阵的乘积，并且也用三元组形式表达，该如何完成呢。
如果不知道矩阵如何相乘，可以参考：http://cs101.openjudge.cn/practice/18161
输入
输入第一行是三个整数n，m1, m2，两个矩阵X，Y的维度都是n*n，m1是矩阵X中的非0元素数，m2是矩阵Y中的非0元素数。
之后是m1行，每行是一个三元组（行号，列号，元素值），代表X矩阵的元素值，注意行列编号都从0开始。
之后是m2行，每行是一个三元组（行号，列号，元素值），代表Y矩阵的元素值，注意行列编号都从0开始。
输出
输出是m3行，代表X和Y两个矩阵乘积中的非0元素的数目，按照先行号后列号的方式递增排序。
每行仍然是前述的三元组形式。

样例
Sample Input1:
3 3 2
0 0 1
1 0 -1
1 2 3
0 0 7
2 2 1
Sample Output1:
0 0 7
1 0 -7
1 2 3
解释：
A = [
  [ 1, 0, 0],
  [-1, 0, 3],
  [0, 0, 0]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

A*B = [
[7,0,0],
[-7,0,3],
[0,0,0]]

Sample Input2:
2 2 4
0 0 1
1 1 1
0 0 2
0 1 3
1 0 4
1 1 5
Sample Output2:
0 0 2
0 1 3
1 0 4
1 1 5
解释：
A = [
[1,0],
[0,1]
]

B = [
[2,3],
[4,5]
]

A*B = [
[2,3],
[4,5]
]

提示
tags: implementation,matrices
"""