# -*- coding: utf-8 -*-
n,M = map(int,input().split())
p = [0]+[int(x) for x in input().split()]+[M]
lit=[] ; off=[] ; n+=2
for i in range(1,n):
    if i%2: lit.append(p[i]-p[i-1])
    else: off.append(p[i]-p[i-1])
mx = sum(lit) ; sumlit=0 ; sumoff = sum(off)
for k in range(n-1):
    ki = k//2
    if k%2:
        if off[ki]<2: continue
    else:
        sumlit += lit[ki]
        if k>1: sumoff -= off[ki-1]
        if lit[ki]<2: continue
    tp = sumlit + sumoff -1
    if tp>mx: mx = tp
print(mx)

"""info
Created on Tue Oct 26 07:53:53 2021
@author: Asus
https://codeforces.com/problemset/problem/1000/B
1000B-Light It Up
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Recently, you bought a brand new smart lamp with programming features. At first, you set up a schedule to the lamp. Every day it will turn power on at moment 0 and turn power off at moment M. Moreover, the lamp allows you to set a program of switching its state (states are "lights on" and "lights off"). Unfortunately, some program is already installed into the lamp.
The lamp allows only good programs. Good program can be represented as a non-empty array a, where 0<a1<a2<⋯<a|a|<M. All ai must be integers. Of course, preinstalled program is a good program.
The lamp follows program a in next manner: at moment 0 turns power and light on. Then at moment ai the lamp flips its state to opposite (if it was lit, it turns off, and vice versa). The state of the lamp flips instantly: for example, if you turn the light off at moment 1 and then do nothing, the total time when the lamp is lit will be 1. Finally, at moment M the lamp is turning its power off regardless of its state.
Since you are not among those people who read instructions, and you don't understand the language it's written in, you realize (after some testing) the only possible way to alter the preinstalled program. You can insert at most one element into the program a, so it still should be a good program after alteration. Insertion can be done between any pair of consecutive elements of a, or even at the begining or at the end of a.
Find such a way to alter the program that the total time when the lamp is lit is maximum possible. Maybe you should leave program untouched. If the lamp is lit from x till moment y, then its lit for y−x units of time. Segments of time when the lamp is lit are summed up.

Input
First line contains two space separated integers n and M (1≤n≤10**5, 2≤M≤10**9) — the length of program a and the moment when power turns off.
Second line contains n space separated integers a1,a2,…,an (0<a1<a2<⋯<an<M) — initially installed program a.
Output
Print the only integer — maximum possible total time when the lamp is lit.
Examples
input
3 10
4 6 7
output
8
input
2 12
1 10
output
9
input
2 7
3 4
output
6
Note
In the first example, one of possible optimal solutions is to insert value x=3 before a1, so program will be [3,4,6,7] and time of lamp being lit equals (3−0)+(6−4)+(10−7)=8. Other possible solution is to insert x=5 in appropriate place.
In the second example, there is only one optimal solution: to insert x=2 between a1 and a2. Program will become [1,2,10], and answer will be (1−0)+(10−2)=9.
In the third example, optimal answer is to leave program untouched, so answer will be (3−0)+(7−4)=6.
"""