# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    input()
    a = [*map(int,input().split())]
    b = [*map(int,input().split())]
    ab = sorted([*zip(a,b)], reverse=True)
    time = 0
    for z in ab:
        deli = z[0] ; pick = z[1]
        time += pick
        if time >= deli:
            time = max(deli,time-pick)
            break
    ans.append(str(time))
print('\n'.join(ans))

#faster_code_with_sys     #work_for_onlinejudge
import sys
ans=[]
for _ in range(int(sys.stdin.readline())):
    sys.stdin.readline()
    a = [*map(int,sys.stdin.readline().split())]
    b = [*map(int,sys.stdin.readline().split())]
    ab = sorted([*zip(a,b)], reverse=True)
    time = 0
    for z in ab:
        deli = z[0] ; pick = z[1]
        time += pick
        if time >= deli:
            time = max(deli,time-pick) ; break
    ans.append(str(time))
print('\n'.join(ans))

"""info
Created on Tue Nov  9 12:52:54 2021
@author: Asus
https://codeforces.com/problemset/problem/1443/C
1443C-The Delivery Dilemma
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Petya is preparing for his birthday. He decided that there would be n different dishes on the dinner table, numbered from 1 to n. Since Petya doesn't like to cook, he wants to order these dishes in restaurants.
Unfortunately, all dishes are prepared in different restaurants and therefore Petya needs to pick up his orders from n different places. To speed up this process, he wants to order courier delivery at some restaurants. Thus, for each dish, there are two options for Petya how he can get it:
the dish will be delivered by a courier from the restaurant i, in this case the courier will arrive in ai minutes,
Petya goes to the restaurant i on his own and picks up the dish, he will spend bi minutes on this.
Each restaurant has its own couriers and they start delivering the order at the moment Petya leaves the house. In other words, all couriers work in parallel. Petya must visit all restaurants in which he has not chosen delivery, he does this consistently.
For example, if Petya wants to order n=4 dishes and a=[3,7,4,5], and b=[2,1,2,4], then he can order delivery from the first and the fourth restaurant, and go to the second and third on your own. Then the courier of the first restaurant will bring the order in 3 minutes, the courier of the fourth restaurant will bring the order in 5 minutes, and Petya will pick up the remaining dishes in 1+2=3 minutes. Thus, in 5 minutes all the dishes will be at Petya's house.
Find the minimum time after which all the dishes can be at Petya's home.

Input
The first line contains one positive integer t (1≤t≤2⋅10**5) — the number of test cases. Then t test cases follow.
Each test case begins with a line containing one integer n (1≤n≤2⋅10**5) — the number of dishes that Petya wants to order.
The second line of each test case contains n integers a1…an (1≤ai≤10**9) — the time of courier delivery of the dish with the number i.
The third line of each test case contains n integers b1…bn (1≤bi≤10**9) — the time during which Petya will pick up the dish with the number i.
The sum of n over all test cases does not exceed 2⋅10**5.
Output
For each test case output one integer — the minimum time after which all dishes can be at Petya's home.
Example
input
4
4
3 7 4 5
2 1 2 4
4
1 2 3 4
3 3 3 3
2
1 2
10 10
2
10 10
1 2
output
5
3
2
3

2
53 28
10 47
out: 28
"""