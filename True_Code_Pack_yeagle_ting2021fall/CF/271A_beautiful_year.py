# -*- coding: utf-8 -*-
y = int(input())
while True :
    y = int(y) + 1
    y = str(y)
    if y[0]!=y[1] and y[0]!=y[2] and y[0]!=y[3] and y[1]!=y[2] and y[1]!=y[3] and y[2]!=y[3]:
        print(y)
        break
    else: pass

"""info
Created on Mon Sep 20 16:56:18 2021
@author: Asus
https://codeforces.com/problemset/problem/271/A
271A-Beautiful Year
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

It seems like the year of 2013 came only yesterday. Do you know a curious fact? The year of 2013 is the first year after the old 1987 with only distinct digits.
Now you are suggested to solve the following problem: given a year number, find the minimum year number which is strictly larger than the given one and has only distinct digits.

Input
The single line contains integer y (1000 ≤ y ≤ 9000) — the year number.
Output
Print a single integer — the minimum year number that is strictly larger than y and all it's digits are distinct. It is guaranteed that the answer exists.
Examples
    input
        1987
    output
        2013
    input
        2013
    output
        2014
"""