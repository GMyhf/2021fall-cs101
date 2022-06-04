# -*- coding: utf-8 -*-
input()
*a, = map(int, input().split())
x = max(a)
an = [0]*(x+1)
for i in a:
    an[i] += 1
dp = [0]*(x+1)
for j in range(1,x+1):
    dp[j] = max(dp[j-1], dp[j-2] + an[j]*j)
print(dp[-1])

# open great space: replacing x = max(a) with x = 100000

# code by amazing tuple assignment, x+2 to allow renew a's value for the last time
input()
*arr, = map(int, input().split())
x = max(arr)
an = [0]*(x+2)
for i in arr:
    an[i] += i
a=b=0
for n in an:
    a, b = max(a,b), a+n
print(a)

"""info
Created on Mon Nov 22 12:09:36 2021
@author: Asus
https://codeforces.com/problemset/problem/455/A
455A-Boredom
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Alex doesn't like boredom. That's why whenever he gets bored, he comes up with games. One long winter evening he came up with a game and decided to play it.
Given a sequence a consisting of n integers. The player can make several steps. In a single step he can choose an element of the sequence (let's denote it ak) and delete it, at that all elements equal to ak + 1 and ak - 1 also must be deleted from the sequence. That step brings ak points to the player.
Alex is a perfectionist, so he decided to get as many points as possible. Help him.

Input
The first line contains integer n (1 ≤ n ≤ 10**5) that shows how many numbers are in Alex's sequence.
The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 10**5).
Output
Print a single integer — the maximum number of points that Alex can earn.
Examples
input
2
1 2
output
2
input
3
1 2 3
output
4
input
9
1 2 1 3 2 2 2 2 3
output
10
Note
Consider the third test example. At first step we need to choose any element equal to 2. After that step our sequence looks like this [2, 2, 2, 2]. Then we do 4 steps, on each step we choose any element equals to 2. In total we earn 10 points.
"""