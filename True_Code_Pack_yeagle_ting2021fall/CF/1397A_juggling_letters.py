# -*- coding: utf-8 -*-
ans = []
for _ in range(int(input())):
    memo = {}
    n = int(input())
    for _ in range(n):
        for char in input():
            if char in memo:
                memo[char] += 1
            else:
                memo[char] = 1
    for char in memo:
        if memo[char]%n:
            ans.append('NO')
            break
    else: ans.append('YES')
print('\n'.join(ans))

"""info
Created on Wed Dec  8 19:08:19 2021
@author: Asus
https://codeforces.com/problemset/problem/1397/A
1397A-Juggling Letters
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given n strings s1,s2,…,sn consisting of lowercase Latin letters.
In one operation you can remove a character from a string si and insert it to an arbitrary position in a string sj (j may be equal to i). You may perform this operation any number of times. Is it possible to make all n strings equal?

Input
The first line contains t (1≤t≤10): the number of test cases.
The first line of each test case contains a single integer n (1≤n≤1000): the number of strings.
n lines follow, the i-th line contains si (1≤|si|≤1000).
The sum of lengths of all strings in all test cases does not exceed 1000.
Output
If it is possible to make the strings equal, print "YES" (without quotes).
Otherwise, print "NO" (without quotes).
You can output each character in either lowercase or uppercase.
Example
input
4
2
caa
cbb
3
cba
cba
cbb
4
ccab
cbac
bca
acbcc
4
acb
caf
c
cbafc
output
YES
NO
YES
NO
Note
In the first test case, you can do the following:
Remove the third character of the first string and insert it after the second character of the second string, making the two strings "ca" and "cbab" respectively.
Remove the second character of the second string and insert it after the second character of the first string, making both strings equal to "cab".
In the second test case, it is impossible to make all n strings equal.
"""