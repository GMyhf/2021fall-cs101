# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    n = int(input())
    candy = [*map(int, input().split())]
    total = sum(candy)
    if n == 1:
        ans += [0]
    elif total%n:
        ans += [-1]
    else:
        k = [x for x in candy if x > total//n]
        ans += [len(k)]
print('\n'.join(map(str,ans)))

# maybe a little faster code:
ans=[]
for _ in range(int(input())):
    n = int(input())
    candy = [*map(int, input().split())]
    total = sum(candy)
    if n == 1:
        ans += [0]
    elif total%n:
        ans += [-1]
    else:
        candy.sort(reverse=True)
        average = total//n
        k = 0
        for x in candy:
            if x > average:
                k += 1
            else:
                break
        ans += [k]
print('\n'.join(map(str,ans)))

"""info
Created on Mon Nov 22 11:50:01 2021
@author: Asus
https://codeforces.com/problemset/problem/1538/B
1538B-Friends and Candies
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Polycarp has n friends, the i-th of his friends has ai candies. Polycarp's friends do not like when they have different numbers of candies. In other words they want all ai to be the same. To solve this, Polycarp performs the following set of actions exactly once:
Polycarp chooses k (0≤k≤n) arbitrary friends (let's say he chooses friends with indices i1,i2,…,ik);
Polycarp distributes their ai1+ai2+…+aik candies among all n friends. During distribution for each of ai1+ai2+…+aik candies he chooses new owner. That can be any of n friends. Note, that any candy can be given to the person, who has owned that candy before the distribution process.
Note that the number k is not fixed in advance and can be arbitrary. Your task is to find the minimum value of k.
For example, if n=4 and a=[4,5,2,5], then Polycarp could make the following distribution of the candies:
Polycarp chooses k=2 friends with indices i=[2,4] and distributes a2+a4=10 candies to make a=[4,4,4,4] (two candies go to person 3).
Note that in this example Polycarp cannot choose k=1 friend so that he can redistribute candies so that in the end all ai are equal.
For the data n and a, determine the minimum value k. With this value k, Polycarp should be able to select k friends and redistribute their candies so that everyone will end up with the same number of candies.

Input
The first line contains one integer t (1≤t≤10**4). Then t test cases follow.
The first line of each test case contains one integer n (1≤n≤2⋅10**5).
The second line contains n integers a1,a2,…,an (0≤ai≤10**4).
It is guaranteed that the sum of n over all test cases does not exceed 2⋅10**5.
Output
For each test case output:
the minimum value of k, such that Polycarp can choose exactly k friends so that he can redistribute the candies in the desired way;
"-1" if no such value k exists.
Example
input
5
4
4 5 2 5
2
0 4
5
10 8 5 1 4
1
10000
7
1 1 1 1 1 1 1
output
2
1
-1
0
0
"""