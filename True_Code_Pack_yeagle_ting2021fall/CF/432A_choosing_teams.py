# -*- coding: utf-8 -*-
n,k = map(int,input().split())
y = sorted([int(x) for x in input().split()])
member = 0
for x in y:
    if x + k <= 5 : member += 1
    else: break
print(member//3)

"""info
Created on Wed Nov  3 08:30:17 2021
@author: Asus
https://codeforces.com/problemset/problem/432/A
432A-Choosing Teams
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

The Saratov State University Olympiad Programmers Training Center (SSU OPTC) has n students. For each student you know the number of times he/she has participated in the ACM ICPC world programming championship. According to the ACM ICPC rules, each person can participate in the world championship at most 5 times.
The head of the SSU OPTC is recently gathering teams to participate in the world championship. Each team must consist of exactly three people, at that, any person cannot be a member of two or more teams. What maximum number of teams can the head make if he wants each team to participate in the world championship with the same members at least k times?

Input
The first line contains two integers, n and k (1 ≤ n ≤ 2000; 1 ≤ k ≤ 5). The next line contains n integers: y1, y2, ..., yn (0 ≤ yi ≤ 5), where yi shows the number of times the i-th person participated in the ACM ICPC world championship.
Output
Print a single number — the answer to the problem.
Examples
input
5 2
0 4 5 1 0
output
1
input
6 4
0 1 2 3 4 5
output
0
input
6 5
0 0 0 0 0 0
output
2
Note
In the first sample only one team could be made: the first, the fourth and the fifth participants.
In the second sample no teams could be created.
In the third sample two teams could be created. Any partition into two teams fits.
"""