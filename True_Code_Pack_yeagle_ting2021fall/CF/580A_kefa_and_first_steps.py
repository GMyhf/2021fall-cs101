# -*- coding: utf-8 -*-
n=int(input())
seq=[int(x) for x in input().split()]
length=[] ; l=1
if n==1: print(1)
else:
    for i in range(1,n):
        if seq[i]<seq[i-1]: length.append(l) ; l=1
        else: l+=1
        if l!=1: length.append(l)
    print(max(length))

"""info #dp?
Created on Sun Oct 17 10:39:36 2021
@author: Asus
https://codeforces.com/problemset/problem/580/A
580A-Kefa and First Steps
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Kefa decided to make some money doing business on the Internet for exactly n days. He knows that on the i-th day (1 ≤ i ≤ n) he makes ai money. Kefa loves progress, that's why he wants to know the length of the maximum non-decreasing subsegment in sequence ai. Let us remind you that the subsegment of the sequence is its continuous fragment. A subsegment of numbers is called non-decreasing if all numbers in it follow in the non-decreasing order.
Help Kefa cope with this task!

Input
The first line contains integer n (1 ≤ n ≤ 10**5).
The second line contains n integers a1,  a2,  ...,  an (1 ≤ ai ≤ 10**9).
Output
Print a single integer — the length of the maximum non-decreasing subsegment of sequence a.
Examples
input
6
2 2 1 3 4 1
output
3
input
3
2 2 9
output
3
Note
In the first test the maximum non-decreasing subsegment is the numbers from the third to the fifth one.
In the second test the maximum non-decreasing subsegment is the numbers from the first to the third one.
"""