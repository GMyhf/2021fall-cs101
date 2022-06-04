# -*- coding: utf-8 -*-
n = int(input())
ans=0 ; k=0
for i in range(1,150):
    k+=i ; n-=k
    if n<0: break
    ans+=1
print(ans)

"""info
Created on Sun Nov  7 08:40:13 2021
@author: Asus
https://codeforces.com/problemset/problem/492/A
492A-Vanya and Cubes
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Vanya got n cubes. He decided to build a pyramid from them. Vanya wants to build the pyramid as follows: the top level of the pyramid must consist of 1 cube, the second level must consist of 1 + 2 = 3 cubes, the third level must have 1 + 2 + 3 = 6 cubes, and so on. Thus, the i-th level of the pyramid must have 1 + 2 + ... + (i - 1) + i cubes.
Vanya wants to know what is the maximum height of the pyramid that he can make using the given cubes.

Input
The first line contains integer n (1 ≤ n ≤ 10**4) — the number of cubes given to Vanya.
Output
Print the maximum possible height of the pyramid in the single line.
Examples
input
1
output
1
input
25
output
4
Note
Illustration to the second sample:
"""