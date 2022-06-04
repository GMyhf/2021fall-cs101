# -*- coding: utf-8 -*-
ans = []
down = {'U':'D', 'D':'U', 'L':'L', 'R':'R'}
for _ in range(int(input())):
    input()
    ans.append(''.join([down[i] for i in input()]))
print('\n'.join(ans))

"""info
Created on Tue Dec 21 13:54:45 2021
@author: Asus
https://codeforces.com/problemset/problem/1567/A
1567A-Domino Disaster
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Alice has a grid with 2 rows and n columns. She fully covers the grid using n dominoes of size 1×2 — Alice may place them vertically or horizontally, and each cell should be covered by exactly one domino.
Now, she decided to show one row of the grid to Bob. Help Bob and figure out what the other row of the grid looks like!

Input
The input consists of multiple test cases. The first line contains an integer t (1≤t≤5000) — the number of test cases. The description of the test cases follows.
The first line of each test case contains an integer n (1≤n≤100) — the width of the grid.
The second line of each test case contains a string s consisting of n characters, each of which is either L, R, U, or D, representing the left, right, top, or bottom half of a domino, respectively (see notes for better understanding). This string represents one of the rows of the grid.
Additional constraint on the input: each input corresponds to at least one valid tiling.
Output
For each test case, output one string — the other row of the grid, using the same format as the input string. If there are multiple answers, print any.
Example
input
4
1
U
2
LR
5
LRDLR
6
UUUUUU
output
D
LR
LRULR
DDDDDD
Note
In the first test case, Alice shows Bob the top row, the whole grid may look like:
In the second test case, Alice shows Bob the bottom row, the whole grid may look like:
In the third test case, Alice shows Bob the bottom row, the whole grid may look like:
In the fourth test case, Alice shows Bob the top row, the whole grid may look like:
"""