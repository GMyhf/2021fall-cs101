# -*- coding: utf-8 -*-
move=[]
for _ in range(int(input())):
    n = int(input()) ; m=0
    a = [int(x) for x in input().split()]
    b = [int(y) for y in input().split()]
    an = min(a) ; bn = min(b)
    for i in range(n):
        m += max( a[i]-an , b[i]-bn )
    move.append(str(m))
print('\n'.join(move))

"""info
Created on Sat Nov  6 21:05:45 2021
@author: Asus
https://codeforces.com/problemset/problem/1399/B
1339B-Gifts Fixing
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You have n gifts and you want to give all of them to children. Of course, you don't want to offend anyone, so all gifts should be equal between each other. The i-th gift consists of ai candies and bi oranges.
During one move, you can choose some gift 1≤i≤n and do one of the following operations:
eat exactly one candy from this gift (decrease ai by one);
eat exactly one orange from this gift (decrease bi by one);
eat exactly one candy and exactly one orange from this gift (decrease both ai and bi by one).
Of course, you can not eat a candy or orange if it's not present in the gift (so neither ai nor bi can become less than zero).
As said above, all gifts should be equal. This means that after some sequence of moves the following two conditions should be satisfied: a1=a2=⋯=an and b1=b2=⋯=bn (and ai equals bi is not necessary).
Your task is to find the minimum number of moves required to equalize all the given gifts.
You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤1000) — the number of test cases. Then t test cases follow.
The first line of the test case contains one integer n (1≤n≤50) — the number of gifts. The second line of the test case contains n integers a1,a2,…,an (1≤ai≤109), where ai is the number of candies in the i-th gift. The third line of the test case contains n integers b1,b2,…,bn (1≤bi≤10**9), where bi is the number of oranges in the i-th gift.

Output
For each test case, print one integer: the minimum number of moves required to equalize all the given gifts.

Example
input
5
3
3 5 6
3 2 3
5
1 2 3 4 5
5 4 3 2 1
3
1 1 1
2 2 2
6
1 1000000000 1000000000 1000000000 1000000000 1000000000
1 1 1 1 1 1
3
10 12 8
7 5 4
output
6
16
0
4999999995
7
Note
In the first test case of the example, we can perform the following sequence of moves:
choose the first gift and eat one orange from it, so a=[3,5,6] and b=[2,2,3];
choose the second gift and eat one candy from it, so a=[3,4,6] and b=[2,2,3];
choose the second gift and eat one candy from it, so a=[3,3,6] and b=[2,2,3];
choose the third gift and eat one candy and one orange from it, so a=[3,3,5] and b=[2,2,2];
choose the third gift and eat one candy from it, so a=[3,3,4] and b=[2,2,2];
choose the third gift and eat one candy from it, so a=[3,3,3] and b=[2,2,2].

"""