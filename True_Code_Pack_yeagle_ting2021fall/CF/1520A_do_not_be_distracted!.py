# -*- coding: utf-8 -*-
t = int(input())
Ans=[]
for n in range(t):
    n = int(input())
    for task in range(1):
        task = input()
        if n<3: Ans.append("YES")
        else:
            sus=[]
            for i in task:
                i1 = task.find(i)
                i2 = task.rfind(i) + 1
                if task[i1:i2].__contains__(i*(i2-i1)):
                    sus.append(False)
                else: sus.append(True)
            if sum(sus): Ans.append("NO")
            else: Ans.append("YES")
for a in Ans: print(a)
    
"""info
Created on Mon Sep 27 08:25:25 2021
@author: Asus
https://codeforces.com/problemset/problem/1520/A
1520_A-Do Not Be Distracted!
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Polycarp has 26 tasks. Each task is designated by a capital letter of the Latin alphabet.
The teacher asked Polycarp to solve tasks in the following way: if Polycarp began to solve some task, then he must solve it to the end, without being distracted by another task. After switching to another task, Polycarp cannot return to the previous task.
Polycarp can only solve one task during the day. Every day he wrote down what task he solved. Now the teacher wants to know if Polycarp followed his advice.
For example, if Polycarp solved tasks in the following order: "DDBBCCCBBEZ", then the teacher will see that on the third day Polycarp began to solve the task 'B', then on the fifth day he got distracted and began to solve the task 'C', on the eighth day Polycarp returned to the task 'B'. Other examples of when the teacher is suspicious: "BAB", "AABBCCDDEEBZZ" and "AAAAZAAAAA".
If Polycarp solved the tasks as follows: "FFGZZZY", then the teacher cannot have any suspicions. Please note that Polycarp is not obligated to solve all tasks. Other examples of when the teacher doesn't have any suspicious: "BA", "AFFFCC" and "YYYYY".
Help Polycarp find out if his teacher might be suspicious.

Input
The first line contains an integer t (1≤t≤1000). Then t test cases follow.
The first line of each test case contains one integer n (1≤n≤50) — the number of days during which Polycarp solved tasks.
The second line contains a string of length n, consisting of uppercase Latin letters, which is the order in which Polycarp solved the tasks.
Output
For each test case output:
"YES", if the teacher cannot be suspicious;
"NO", otherwise.
You may print every letter in any case you want (so, for example, the strings yEs, yes, Yes and YES are all recognized as positive answer).
Example
input
    5
    3
    ABA
    11
    DDBBCCCBBEZ
    7
    FFGZZZY
    1
    Z
    2
    AB
output
    NO
    NO
    YES
    YES
    YES
"""