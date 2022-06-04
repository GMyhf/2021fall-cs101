# -*- coding: utf-8 -*-
from math import gcd
a, b, n = map(int, input().split())
while True:
    A = gcd(a, n)
    if n >= A:
        n -= A
    else:
        print(1)
        break
    B = gcd(b, n)
    if n >= B:
        n -= B
    else:
        print(0)
        break

"""info
Created on Sat Dec  4 23:09:57 2021
@author: Asus
https://codeforces.com/problemset/problem/119/A
119A-Epic Game
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Simon and Antisimon play a game. Initially each player receives one fixed positive integer that doesn't change throughout the game. Simon receives number a and Antisimon receives number b. They also have a heap of n stones. The players take turns to make a move and Simon starts. During a move a player should take from the heap the number of stones equal to the greatest common divisor of the fixed number he has received and the number of stones left in the heap. A player loses when he cannot take the required number of stones (i. e. the heap has strictly less stones left than one needs to take).
Your task is to determine by the given a, b and n who wins the game.

Input
The only string contains space-separated integers a, b and n (1 ≤ a, b, n ≤ 100) — the fixed numbers Simon and Antisimon have received correspondingly and the initial number of stones in the pile.
Output
If Simon wins, print "0" (without the quotes), otherwise print "1" (without the quotes).
Examples
input
3 5 9
output
0
input
1 1 100
output
1
Note
The greatest common divisor of two non-negative integers a and b is such maximum positive integer k, that a is divisible by k without remainder and similarly, b is divisible by k without remainder. Let gcd(a, b) represent the operation of calculating the greatest common divisor of numbers a and b. Specifically, gcd(x, 0) = gcd(0, x) = x.
In the first sample the game will go like that:
Simon should take gcd(3, 9) = 3 stones from the heap. After his move the heap has 6 stones left.
Antisimon should take gcd(5, 6) = 1 stone from the heap. After his move the heap has 5 stones left.
Simon should take gcd(3, 5) = 1 stone from the heap. After his move the heap has 4 stones left.
Antisimon should take gcd(5, 4) = 1 stone from the heap. After his move the heap has 3 stones left.
Simon should take gcd(3, 3) = 3 stones from the heap. After his move the heap has 0 stones left.
Antisimon should take gcd(5, 0) = 5 stones from the heap. As 0 < 5, it is impossible and Antisimon loses.
In the second sample each player during each move takes one stone from the heap. As n is even, Antisimon takes the last stone and Simon can't make a move after that.
"""