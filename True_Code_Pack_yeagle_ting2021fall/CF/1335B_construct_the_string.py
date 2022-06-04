# -*- coding: utf-8 -*-
s='qwertyuiopasdfghjklzxcvbnm'
ans=[]
for _ in range(int(input())):
    n,a,b = map(int,input().split())
    if a==b==1: x = s[0]*n
    else:
        xi = s[:b]
        x = xi*(n//b) + xi[:n%b]
    ans.append(x)
print('\n'.join(ans))

"""info
Created on Thu Nov  4 10:03:30 2021
@author: Asus
https://codeforces.com/problemset/problem/1335/B
1335B-Construct the String
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given three positive integers n, a and b. You have to construct a string s of length n consisting of lowercase Latin letters such that each substring of length a has exactly b distinct letters. It is guaranteed that the answer exists.
You have to answer t independent test cases.
Recall that the substring s[l…r] is the string sl,sl+1,…,sr and its length is r−l+1. In this problem you are only interested in substrings of length a.

Input
The first line of the input contains one integer t (1≤t≤2000) — the number of test cases. Then t test cases follow.
The only line of a test case contains three space-separated integers n, a and b (1≤a≤n≤2000,1≤b≤min(26,a)), where n is the length of the required string, a is the length of a substring and b is the required number of distinct letters in each substring of length a.
It is guaranteed that the sum of n over all test cases does not exceed 2000 (∑n≤2000).
Output
For each test case, print the answer — such a string s of length n consisting of lowercase Latin letters that each substring of length a has exactly b distinct letters. If there are multiple valid answers, print any of them. It is guaranteed that the answer exists.
Example
input
4
7 5 3
6 1 1
6 6 1
5 2 2
output
tleelte
qwerty
vvvvvv
abcde
Note
In the first test case of the example, consider all the substrings of length 5:
"tleel": it contains 3 distinct (unique) letters,
"leelt": it contains 3 distinct (unique) letters,
"eelte": it contains 3 distinct (unique) letters.
"""