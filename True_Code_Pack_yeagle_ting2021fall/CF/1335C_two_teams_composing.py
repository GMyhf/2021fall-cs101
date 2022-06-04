# -*- coding: utf-8 -*-
from collections import Counter
ans=[]
for _ in range(int(input())):
    n = int(input())
    stu = sorted(map(int, input().split()))
    if n < 2: ans.append(0) ; continue
    diff = len(set(stu))
    same = Counter(stu).most_common(1)[0][1]
    ans.append(max(min(diff, same-1), min(diff-1, same)))
print('\n'.join(map(str, ans)))

"""info
Created on Wed Dec  1 10:28:29 2021
@author: Asus
https://codeforces.com/problemset/problem/1335/C
1335C-Two Teams Composing
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

You have n students under your control and you have to compose exactly two teams consisting of some subset of your students. Each student had his own skill, the i-th student skill is denoted by an integer ai (different students can have the same skills).
So, about the teams. Firstly, these two teams should have the same size. Two more constraints:
The first team should consist of students with distinct skills (i.e. all skills in the first team are unique).
The second team should consist of students with the same skills (i.e. all skills in the second team are equal).
Note that it is permissible that some student of the first team has the same skill as a student of the second team.
Consider some examples (skills are given):
[1,2,3], [4,4] is not a good pair of teams because sizes should be the same;
[1,1,2], [3,3,3] is not a good pair of teams because the first team should not contain students with the same skills;
[1,2,3], [3,4,4] is not a good pair of teams because the second team should contain students with the same skills;
[1,2,3], [3,3,3] is a good pair of teams;
[5], [6] is a good pair of teams.
Your task is to find the maximum possible size x for which it is possible to compose a valid pair of teams, where each team size is x (skills in the first team needed to be unique, skills in the second team should be the same between them). A student cannot be part of more than one team.
You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤10**4) — the number of test cases. Then t test cases follow.
The first line of the test case contains one integer n (1≤n≤2⋅10**5) — the number of students. The second line of the test case contains n integers a1,a2,…,an (1≤ai≤n), where ai is the skill of the i-th student. Different students can have the same skills.
It is guaranteed that the sum of n over all test cases does not exceed 2⋅10**5 (∑n≤2⋅10**5).
Output
For each test case, print the answer — the maximum possible size x for which it is possible to compose a valid pair of teams, where each team size is x.
Example
input
4
7
4 2 4 1 4 3 4
5
2 1 5 4 3
1
1
4
1 1 1 3
output
3
1
0
2
Note
In the first test case of the example, it is possible to construct two teams of size 3: the first team is [1,2,4] and the second team is [4,4,4]. Note, that there are some other ways to construct two valid teams of size 3.
"""