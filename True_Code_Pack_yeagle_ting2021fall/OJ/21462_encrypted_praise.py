# -*- coding: utf-8 -*-
n = int(input())
edge = [-1]*(n+2)
matx = [edge, *[[-1, *map(int, input().split()), -1] for _ in range(n)], edge]
turn = ((1, 0), (0, 1), (-1, 0), (0, -1))  #anti-clock, starting down
mssg = ''
y = x = 1 ; t=0
dy, dx = turn[t]
for _ in range(n**2):
    goto = matx[y+dy][x+dx]
    if goto == -1: 
        t = (t+1)%4
        dy, dx = turn[t]
        goto = matx[y+dy][x+dx]
    mssg += chr(matx[y][x])
    if goto == 0: break
    matx[y][x] = -1
    y += dy
    x += dx
print(mssg)

# remastered when creating template:
n = int(input())
edge = [[-1]*(n+2)]
mtrx = edge+ [[-1, *map(int,input().split()), -1]for _ in range(n)] +edge
turn = ((1, 0), (0, 1), (-1, 0), (0, -1))  #anti-clock, starting down
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

"""info
Created on Tue Dec  7 09:38:17 2021
@author: Asus
http://cs101.openjudge.cn/practice/21462/
21462:加密的称赞 v0.2 (matrices)
总时间限制: 1000ms 内存限制: 65536kB
描述
圣诞将至，小翔想写一段话给小叶，为了体现他的别出心裁，他想运用在计概中所学知识，对这段话进
行加密。具体方法如下：
1. 小翔首先想出自己想说的话：You are so beautiful!
2. 然后把每个字符按照顺序，以逆时针转圈的方式填入一个n阶方阵（即一个n*n的矩阵），如下图1所示
3. 最后把相应的字符转化为ASCII码，没有字符的地方用0表示，如下图2所示。
对应英文描述
It's almost Christmas, and Xiaoxiang wants to write a message to Xiaoye. In order to show his inventiveness, he wants to encrypt the message by applying what he has learned in the Theory of Calculations. The method is as follows.
First think of something he wants to say: You are so beautiful!
Then fill in an -order matrix (a  matrix) with each character in the order in which they are written, in a counterclockwise circle, as shown in Figure 1 below.
Finally, the corresponding characters are converted to ASCII code, with ​ where there are no characters, as shown in Figure 2.
输入
第一行为n（n≤100），表示这个方阵的阶数。接下来有行，每一行n个整数，表示字符的ASCII码
输出
一行，即小翔本来想说的话

样例
sample1 in
3
104 101 109
97 0 111
110 100 115
sample1 out
handsome

sample2 in
5
89 116 117 97 101
111 105 0 0 98
117 102 0 0 32
32 117 108 33 111
97 114 101 32 115
sample2 out
You are so beautiful!
提示
在openjudge中print(chr(0))是有输出的，是ASCII码为0对应的字符，本题中0表示没有输出。
"""