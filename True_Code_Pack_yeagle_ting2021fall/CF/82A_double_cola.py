# -*- coding: utf-8 -*-
n, r = int(input()), 1
while 5*r < n:
    n -= 5*r
    r *= 2
print(['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard'][(n-1)//r])

"""info
Created on Tue Dec 21 13:23:10 2021
@author: Asus
https://codeforces.com/problemset/problem/82/A
82A-Double Cola
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on. This process continues ad infinitum.
For example, Penny drinks the third can of cola and the queue will look like this: Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny.
Write a program that will print the name of a man who will drink the n-th can.
Note that in the very beginning the queue looks like that: Sheldon, Leonard, Penny, Rajesh, Howard. The first person is Sheldon.

Input
The input data consist of a single integer n (1 ≤ n ≤ 10**9).
It is guaranteed that the pretests check the spelling of all the five names, that is, that they contain all the five possible answers.
Output
Print the single line — the name of the person who drinks the n-th can of cola. The cans are numbered starting from 1. Please note that you should spell the names like this: "Sheldon", "Leonard", "Penny", "Rajesh", "Howard" (without the quotes). In that order precisely the friends are in the queue initially.

Examples
input
1
output
Sheldon
input
6
output
Sheldon
input
1802
output
Penny
"""