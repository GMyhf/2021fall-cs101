# -*- coding: utf-8 -*-
n, m = map(int, input().split())
kmax = (n-m+1)*(n-m)//2
team = n//m
left = n%m
kmin = (m-left)*team*(team-1)//2 + (team+1)*team*left//2
print(kmin, kmax)

#idea form: https://codeleading.com/article/26353391241/

"""info
Created on Tue Dec  7 08:26:02 2021
@author: Asus
https://codeforces.com/problemset/problem/478/B
478B-Random Teams
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

n participants of the competition were split into m teams in some manner so that each team has at least one participant. After the competition each pair of participants from the same team became friends.
Your task is to write a program that will find the minimum and the maximum number of pairs of friends that could have formed by the end of the competition.

Input
The only line of input contains two integers n and m, separated by a single space (1 ≤ m ≤ n ≤ 10**9) — the number of participants and the number of teams respectively.
Output
The only line of the output should contain two integers kmin and kmax — the minimum possible number of pairs of friends and the maximum possible number of pairs of friends respectively.
Examples
input
5 1
output
10 10
input
3 2
output
1 1
input
6 3
output
3 6
Note
In the first sample all the participants get into one team, so there will be exactly ten pairs of friends.
In the second sample at any possible arrangement one team will always have two participants and the other team will always have one participant. Thus, the number of pairs of friends will always be equal to one.
In the third sample minimum number of newly formed friendships can be achieved if participants were split on teams consisting of 2 people, maximum number can be achieved if participants were split on teams of 1, 1 and 4 people.
"""