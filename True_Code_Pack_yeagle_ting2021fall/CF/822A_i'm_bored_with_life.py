# -*- coding: utf-8 -*-
# easy import
from math import factorial
x = min(map(int, input().split()))
print(factorial(x))

# using another function
from math import prod
x = min(map(int, input().split()))
print(prod([*range(1, x+1)]))

# without import is ok
x = min(map(int, input().split()))
ans = 1
for i in range(1, x+1): ans *= i
print(ans)

"""info
Created on Sun Dec 12 09:13:37 2021
@author: Asus
https://codeforces.com/problemset/problem/822/A
822A-I'm bored with life
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Holidays have finished. Thanks to the help of the hacker Leha, Noora managed to enter the university of her dreams which is located in a town Pavlopolis. It's well known that universities provide students with dormitory for the period of university studies. Consequently Noora had to leave Vičkopolis and move to Pavlopolis. Thus Leha was left completely alone in a quiet town Vičkopolis. He almost even fell into a depression from boredom!
Leha came up with a task for himself to relax a little. He chooses two integers A and B and then calculates the greatest common divisor of integers "A factorial" and "B factorial". Formally the hacker wants to find out GCD(A!, B!). It's well known that the factorial of an integer x is a product of all positive integers less than or equal to x. Thus x! = 1·2·3·...·(x - 1)·x. For example 4! = 1·2·3·4 = 24. Recall that GCD(x, y) is the largest positive integer q that divides (without a remainder) both x and y.
Leha has learned how to solve this task very effective. You are able to cope with it not worse, aren't you?

Input
The first and single line contains two integers A and B (1 ≤ A, B ≤ 10**9, min(A, B) ≤ 12).
Output
Print a single integer denoting the greatest common divisor of integers A! and B!.
Example
input
4 3
output
6
Note
Consider the sample.
4! = 1·2·3·4 = 24. 3! = 1·2·3 = 6. The greatest common divisor of integers 24 and 6 is exactly 6.
"""