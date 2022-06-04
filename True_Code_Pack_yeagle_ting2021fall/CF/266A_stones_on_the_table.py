# -*- coding: utf-8 -*-
n = int(input())
s = [x for x in input()]
i=0 ; j=1 ; ans=0
while j<len(s):
    if s[i]==s[j]:
        s.remove(s[j])
        ans+=1
    else: i+=1 ; j+=1
print(ans)

#improved_code
input() ; s=input() ; ans=0 ; a=s[0]
for i in range(1,len(s)):
    if s[i]==a: ans+=1
    else: a=s[i]
print(ans)
    
"""info
Created on Mon Oct  4 19:32:30 2021
@author: Asus
https://codeforces.com/problemset/problem/266/A
266A-Stones on the Table
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

There are n stones on the table in a row, each of them can be red, green or blue. Count the minimum number of stones to take from the table so that any two neighboring stones had different colors. Stones in a row are considered neighboring if there are no other stones between them.

Input
The first line contains integer n (1 ≤ n ≤ 50) — the number of stones on the table.
The next line contains string s, which represents the colors of the stones. We'll consider the stones in the row numbered from 1 to n from left to right. Then the i-th character s equals "R", if the i-th stone is red, "G", if it's green and "B", if it's blue.
Output
Print a single integer — the answer to the problem.
Examples
    input
        3
        RRG
    output
        1
    input
        5
        RRRRR
    output
        4
    input
        4
        BRBG
    output
        0
"""