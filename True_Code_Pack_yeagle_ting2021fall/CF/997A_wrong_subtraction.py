# -*- coding: utf-8 -*-
lst = [int(i) for i in input().split()]
n = lst[0] ; k = lst[1]
while k!=0:
    if str(n)[-1]!="0":
        n = int(n-1)
    else: n = int(n/10)
    k -= 1
print(n)

"""info
Created on Tue Sep 28 12:36:36 2021
@author: Asus
https://codeforces.com/problemset/problem/977/A
977A-Wrong Subtraction
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Little girl Tanya is learning how to decrease a number by one, but she does it wrong with a number consisting of two or more digits. Tanya subtracts one from a number by the following algorithm:
1. if the last digit of the number is non-zero, she decreases the number by one;
2. if the last digit of the number is zero, she divides the number by 10 (i.e. removes the last digit).
You are given an integer number n. Tanya will subtract one from it k times. Your task is to print the result after all k subtractions.
It is guaranteed that the result will be positive integer number.

Input
The first line of the input contains two integer numbers n and k (2≤n≤109, 1≤k≤50) — the number from which Tanya will subtract and the number of subtractions correspondingly.
Output
Print one integer number — the result of the decreasing n by one k times.
It is guaranteed that the result will be positive integer number.
Examples
    input
        512 4
    output
        50
    input
        1000000000 9
    output
        1
Note
The first example corresponds to the following sequence: 512→511→510→51→50.
"""