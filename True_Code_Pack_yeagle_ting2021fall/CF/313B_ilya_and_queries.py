# -*- coding: utf-8 -*-
s = input()
same = [0] ; cnt = 0 ; ans = []
for i in range(1,len(s)):
    if s[i]==s[i-1]: cnt+=1
    same.append(cnt)
for _ in range(int(input())):
    li,ri = map(int,input().split())
    ans.append(same[ri-1]-same[li-1])
for a in ans: print(a)

# improved_code :　python3 654ms , pypy3-64 1590ms
s = input()
same = [0] ; cnt = 0 ; ans = []
for i in range(1,len(s)):
    if s[i]==s[i-1]: cnt+=1
    same += [cnt]
for _ in range(int(input())):
    li,ri = map(int,input().split())
    ans += [same[ri-1]-same[li-1]]
print('\n'.join(map(str,ans)))

# modified when making template
s = input()
same, cnt, ans = [0], 0, []
for i in range(1,len(s)):
    if s[i] == s[i-1]: cnt += 1
    same.append(cnt)
for _ in range(int(input())):
    li, ri = map(int, input().split())
    ans.append(same[ri-1]-same[li-1])
print('\n'.join(map(str, ans)))

"""info
Created on Wed Oct 27 08:06:10 2021
@author: Asus
https://codeforces.com/contest/313/problem/B
313B-Ilya and Queries
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Ilya the Lion wants to help all his friends with passing exams. They need to solve the following problem to pass the IT exam.
You've got string s = s1s2... sn (n is the length of the string), consisting only of characters "." and "#" and m queries. Each query is described by a pair of integers li, ri (1 ≤ li < ri ≤ n). The answer to the query li, ri is the number of such integers i (li ≤ i < ri), that si = si + 1.
Ilya the Lion wants to help his friends but is there anyone to help him? Help Ilya, solve the problem.

Input
The first line contains string s of length n (2 ≤ n ≤ 10**5). It is guaranteed that the given string only consists of characters "." and "#".
The next line contains integer m (1 ≤ m ≤ 10**5) — the number of queries. Each of the next m lines contains the description of the corresponding query. The i-th line contains integers li, ri (1 ≤ li < ri ≤ n).
Output
Print m integers — the answers to the queries in the order in which they are given in the input.
Examples
input
......
4
3 4
2 3
1 6
2 6
output
1
1
5
4
input
#..###
5
1 3
5 6
1 5
3 6
3 4
output
1
1
2
2
0
"""