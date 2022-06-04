# -*- coding: utf-8 -*-
string = input()
s1 = string.split('AB',1)
ans = 0
if len(s1) > 1:
    for sub in s1:
        if 'BA' in sub:
            ans = 1
            break
s2 = string.split('BA',1)
if len(s2) > 1 and not ans:
    for sub in s2:
        if 'AB' in sub:
            ans = 1
            break
print(['NO','YES'][ans])

"""info
Created on Mon Dec 13 19:58:18 2021
@author: Asus
https://codeforces.com/problemset/problem/550/A
550A-Two Substrings
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given string s. Your task is to determine if the given string s contains two non-overlapping substrings "AB" and "BA" (the substrings can go in any order).

Input
The only line of input contains a string s of length between 1 and 10**5 consisting of uppercase Latin letters.
Output
Print "YES" (without the quotes), if string s contains two non-overlapping substrings "AB" and "BA", and "NO" otherwise.
Examples
input
ABA
output
NO
input
BACFAB
output
YES
input
AXBYBXA
output
NO
Note
In the first sample test, despite the fact that there are substrings "AB" and "BA", their occurrences overlap, so the answer is "NO".
In the second sample test there are the following occurrences of the substrings: BACFAB.
In the third sample test there is no substring "AB" nor substring "BA".
"""