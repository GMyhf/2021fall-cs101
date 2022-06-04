# -*- coding: utf-8 -*-
n = int(input())
ans = []
while True:
    ans.append('I hate') ; n-=1
    if n==0: ans.append('it'); break
    else: ans.append('that')
    ans.append('I love') ; n-=1
    if n==0: ans.append('it'); break
    else: ans.append('that')
print(' '.join(ans))

#looked_a_little_better_code
n = int(input())
ans = []
while True:
    ans.append('I hate') ; n-=1
    if n: ans.append('that')
    else: ans.append('it'); break
    ans.append('I love') ; n-=1
    if n: ans.append('that')
    else: ans.append('it'); break
print(' '.join(ans))

#more_simple_code
ans=[]
for i in range(int(input())):
    ans.append(['hate','love'][i%2])
print('I ' + ' that I '.join(ans) + ' it')

#one_line_code
print('I '+' that I '.join(['hate','love'][i%2]for i in range(int(input())))+' it')

"""info
Created on Sun Oct  3 10:10:05 2021
@author: Asus
https://codeforces.com/problemset/problem/705/A
705A-Hulk
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Dr. Bruce Banner hates his enemies (like others don't). As we all know, he can barely talk when he turns into the incredible Hulk. That's why he asked you to help him to express his feelings.
Hulk likes the Inception so much, and like that his feelings are complicated. They have n layers. The first layer is hate, second one is love, third one is hate and so on...
For example if n = 1, then his feeling is "I hate it" or if n = 2 it's "I hate that I love it", and if n = 3 it's "I hate that I love that I hate it" and so on.
Please help Dr. Banner.

Input
The only line of the input contains a single integer n (1 ≤ n ≤ 100) — the number of layers of love and hate.
Output
Print Dr.Banner's feeling in one line.
Examples
    input
        1
    output
        I hate it
    input
        2
    output
        I hate that I love it
    input
        3
    output
        I hate that I love that I hate it
"""