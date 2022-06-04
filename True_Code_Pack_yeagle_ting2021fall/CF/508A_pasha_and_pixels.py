# -*- coding: utf-8 -*-
n,m,k = map(int,input().split())
f = [[0]*(m+2) for _ in range(n+2)]    #m=x-axis---c, n=y-axis---r
def check(x,y):
    if all((f[x][y+1],f[x+1][y],f[x+1][y+1])): #left-up
        return 1
    if all((f[x][y+1],f[x-1][y],f[x-1][y+1])): #left-bottom
        return 1
    if all((f[x][y-1],f[x+1][y],f[x+1][y-1])): #right-up
        return 1
    if all((f[x][y-1],f[x-1][y],f[x-1][y-1])): #right-bottom
        return 1
    return 0
ans=0
for i in range(k):
    x,y = map(int,input().split())
    f[x][y] = 1
    if check(x,y): ans=i+1 ; break
for j in range(k-i-1): input()
if ans: print(ans)
else: print(0)

"""info
Created on Sun Oct 24 09:03:47 2021
@author: Asus
https://codeforces.com/problemset/problem/508/A
508A-Pasha and Pixels
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output
Pasha loves his phone and also putting his hair up... But the hair is now irrelevant.
Pasha has installed a new game to his phone. The goal of the game is following. There is a rectangular field consisting of n row with m pixels in each row. Initially, all the pixels are colored white. In one move, Pasha can choose any pixel and color it black. In particular, he can choose the pixel that is already black, then after the boy's move the pixel does not change, that is, it remains black. Pasha loses the game when a 2 × 2 square consisting of black pixels is formed.
Pasha has made a plan of k moves, according to which he will paint pixels. Each turn in his plan is represented as a pair of numbers i and j, denoting respectively the row and the column of the pixel to be colored on the current move.
Determine whether Pasha loses if he acts in accordance with his plan, and if he does, on what move the 2 × 2 square consisting of black pixels is formed.

Input
The first line of the input contains three integers n, m, k (1 ≤ n, m ≤ 1000, 1 ≤ k ≤ 10**5) — the number of rows, the number of columns and the number of moves that Pasha is going to perform.
The next k lines contain Pasha's moves in the order he makes them. Each line contains two integers i and j (1 ≤ i ≤ n, 1 ≤ j ≤ m), representing the row number and column number of the pixel that was painted during a move.
Output
If Pasha loses, print the number of the move when the 2 × 2 square consisting of black pixels is formed.
If Pasha doesn't lose, that is, no 2 × 2 square consisting of black pixels is formed during the given k moves, print 0.
Examples
    input
        2 2 4
        1 1
        1 2
        2 1
        2 2
    output
        4
    input
        2 3 6
        2 3
        2 2
        1 3
        2 2
        1 2
        1 1
    output
        5
    input
        5 3 7
        2 3
        1 2
        1 1
        4 1
        3 1
        5 3
        3 2
    output
        0
"""