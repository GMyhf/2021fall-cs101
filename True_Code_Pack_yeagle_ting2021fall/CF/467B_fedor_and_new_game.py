# -*- coding: utf-8 -*-
n, m, k = map(int, input().split())
player = [int(input()) for _ in range(m+1)]
fedor = player[-1]
friend = 0
for i in range(m):
    comp = fedor ^ player[i]
    diff = 0
    while comp:
        comp &= comp -1
        diff += 1
    if diff <= k: friend += 1
print(friend)

# refer to code by XIASHA on CF
n, m, k = map(int, input().split())
a = []
for _ in range(1 + m):
	a.append(int(input()))
	a[-1] &= ~(0 << n)
val = a[-1]
res = 0
for i in range(m):
	ans = val ^ a[i]
	cnt = 0
	while ans:
		ans &= ans - 1
		cnt += 1
	res += cnt <= k
print(res)

"""info
Created on Sat Dec 11 08:48:56 2021
@author: Asus
https://codeforces.com/problemset/problem/467/B
467B-Fedor and New Game
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

After you had helped George and Alex to move in the dorm, they went to help their friend Fedor play a new computer game «Call of Soldiers 3».
The game has (m + 1) players and n types of soldiers in total. Players «Call of Soldiers 3» are numbered form 1 to (m + 1). Types of soldiers are numbered from 0 to n - 1. Each player has an army. Army of the i-th player can be described by non-negative integer xi. Consider binary representation of xi: if the j-th bit of number xi equal to one, then the army of the i-th player has soldiers of the j-th type.
Fedor is the (m + 1)-th player of the game. He assume that two players can become friends if their armies differ in at most k types of soldiers (in other words, binary representations of the corresponding numbers differ in at most k bits). Help Fedor and count how many players can become his friends.

Input
The first line contains three integers n, m, k (1 ≤ k ≤ n ≤ 20; 1 ≤ m ≤ 1000).
The i-th of the next (m + 1) lines contains a single integer xi (1 ≤ xi ≤ 2n - 1), that describes the i-th player's army. We remind you that Fedor is the (m + 1)-th player.
Output
Print a single integer — the number of Fedor's potential friends.
Examples
input
7 3 1
8
5
111
17
output
0
input
3 3 3
1
2
3
4
output
3
"""