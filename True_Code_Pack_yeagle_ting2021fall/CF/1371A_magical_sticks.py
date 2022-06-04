# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    ans.append((int(input())+1)//2)
print('\n'.join(map(str, ans)))

# onelined? FAST!
print('\n'.join([str((int(input())+1)//2)for _ in range(int(input()))]))

"""info
Created on Thu Dec  2 14:16:49 2021
@author: Asus
https://codeforces.com/problemset/problem/1371/A
1371A-Magical Sticks
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

A penguin Rocher has n sticks. He has exactly one stick with length i for all 1≤i≤n.
He can connect some sticks. If he connects two sticks that have lengths a and b, he gets one stick with length a+b. Two sticks, that were used in the operation disappear from his set and the new connected stick appears in his set and can be used for the next connections.
He wants to create the maximum number of sticks that have the same length. It is not necessary to make all sticks have the same length, some sticks can have the other length. How many sticks with the equal length he can create?

Input
The input consists of multiple test cases. The first line contains a single integer t (1≤t≤1000) — the number of test cases. Next t lines contain descriptions of test cases.
For each test case, the only line contains a single integer n (1≤n≤109).
Output
For each test case, print a single integer  — the answer to the problem.
Example
input
4
1
2
3
4
output
1
1
2
2
Note
In the third case, he can connect two sticks with lengths 1 and 2 and he will get one stick with length 3. So, he will have two sticks with lengths 3.
In the fourth case, he can connect two sticks with lengths 1 and 3 and he will get one stick with length 4. After that, he will have three sticks with lengths {2,4,4}, so two sticks have the same length, and one stick has the other length.
"""