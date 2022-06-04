# -*- coding: utf-8 -*-
n = int(input())
Fx=[] ; Fy=[] ; Fz=[]
for i in range(n):
    x,y,z = map(int,input().split())
    Fx.append(x) ; Fy.append(y) ; Fz.append(z)
if sum(Fx)==0 and sum(Fy)==0 and sum(Fz)==0:
    print("YES")
else: print("NO")

#improved_code
Fx=[] ; Fy=[] ; Fz=[]
for _ in range(int(input())):
    x,y,z = map(int,input().split())
    Fx.append(x) ; Fy.append(y) ; Fz.append(z)
if any((sum(Fx),sum(Fy),sum(Fz))):
    print("NO")
else: print("YES")

"""info
Created on Thu Sep 30 08:43:25 2021
@author: Asus
https://codeforces.com/problemset/problem/69/A
69A-Young Physicist
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

A guy named Vasya attends the final grade of a high school. One day Vasya decided to watch a match of his favorite hockey team. And, as the boy loves hockey very much, even more than physics, he forgot to do the homework. Specifically, he forgot to complete his physics tasks. Next day the teacher got very angry at Vasya and decided to teach him a lesson. He gave the lazy student a seemingly easy task: You are given an idle body in space and the forces that affect it. The body can be considered as a material point with coordinates (0; 0; 0). Vasya had only to answer whether it is in equilibrium. "Piece of cake" — thought Vasya, we need only to check if the sum of all vectors is equal to 0. So, Vasya began to solve the problem. But later it turned out that there can be lots and lots of these forces, and Vasya can not cope without your help. Help him. Write a program that determines whether a body is idle or is moving by the given vectors of forces.

Input
The first line contains a positive integer n (1 ≤ n ≤ 100), then follow n lines containing three integers each: the xi coordinate, the yi coordinate and the zi coordinate of the force vector, applied to the body ( - 100 ≤ xi, yi, zi ≤ 100).
Output
Print the word "YES" if the body is in equilibrium, or the word "NO" if it is not.
Examples
    input
        3
        4 1 7
        -2 4 -1
        1 -5 -3
    output
        NO
    input
        3
        3 -1 7
        -5 2 -4
        2 -1 -3
    output
        YES
"""