# -*- coding: utf-8 -*-
input()
t = [int(x) for x in input().split()]
w = min(t.count(1),t.count(2),t.count(3))
print(w)
for _ in range(w):
    a=t.index(1) ; t[a]=0
    b=t.index(2) ; t[b]=0
    c=t.index(3) ; t[c]=0
    print(a+1,b+1,c+1)

"""info
Created on Sat Oct 30 08:10:32 2021
@author: Asus
https://codeforces.com/problemset/problem/490/A
490A-Team Olympiad
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

The School №0 of the capital of Berland has n children studying in it. All the children in this school are gifted: some of them are good at programming, some are good at maths, others are good at PE (Physical Education). Hence, for each child we know value ti:
ti = 1, if the i-th child is good at programming,
ti = 2, if the i-th child is good at maths,
ti = 3, if the i-th child is good at PE
Each child happens to be good at exactly one of these three subjects.
The Team Scientific Decathlon Olympias requires teams of three students. The school teachers decided that the teams will be composed of three children that are good at different subjects. That is, each team must have one mathematician, one programmer and one sportsman. Of course, each child can be a member of no more than one team.
What is the maximum number of teams that the school will be able to present at the Olympiad? How should the teams be formed for that?

Input
The first line contains integer n (1 ≤ n ≤ 5000) — the number of children in the school. The second line contains n integers t1, t2, ..., tn (1 ≤ ti ≤ 3), where ti describes the skill of the i-th child.
Output
In the first line output integer w — the largest possible number of teams.
Then print w lines, containing three numbers in each line. Each triple represents the indexes of the children forming the team. You can print both the teams, and the numbers in the triplets in any order. The children are numbered from 1 to n in the order of their appearance in the input. Each child must participate in no more than one team. If there are several solutions, print any of them.
If no teams can be compiled, print the only line with value w equal to 0.
Examples
input
7
1 3 1 3 2 1 2
output
2
3 5 2
6 7 4
input
4
2 1 1 2
output
0
"""