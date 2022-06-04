# -*- coding: utf-8 -*-
all_ans = []
for _ in range(int(input())):
    n = int(input())
    *a, = map(int, input().split())
    pre = a[0]
    ans = 0
    for i in range(1, n):
        now = a[i]
        if pre*now < 0:
            ans += pre
            pre = now
        else:
            pre = max(pre, now)
    else: ans += pre
    all_ans.append(ans)
print('\n'.join(map(str, all_ans)))

# maybe this is a dp without using list? variable will do.

"""info
Created on Thu Dec 16 19:34:37 2021
@author: Asus
https://codeforces.com/problemset/problem/1343/C
1343C-Alternating Subsequence
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Recall that the sequence b is a a subsequence of the sequence a if b can be derived from a by removing zero or more elements without changing the order of the remaining elements. For example, if a=[1,2,1,3,1,2,1], then possible subsequences are: [1,1,1,1], [3] and [1,2,1,3,1,2,1], but not [3,2,3] and [1,1,1,1,2].
You are given a sequence a consisting of n positive and negative elements (there is no zeros in the sequence).
Your task is to choose maximum by size (length) alternating subsequence of the given sequence (i.e. the sign of each next element is the opposite from the sign of the current element, like positive-negative-positive and so on or negative-positive-negative and so on). Among all such subsequences, you have to choose one which has the maximum sum of elements.
In other words, if the maximum length of alternating subsequence is k then your task is to find the maximum sum of elements of some alternating subsequence of length k.
You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤10**4) — the number of test cases. Then t test cases follow.
The first line of the test case contains one integer n (1≤n≤2⋅10**5) — the number of elements in a. The second line of the test case contains n integers a1,a2,…,an (−10**9≤ai≤10**9,ai≠0), where ai is the i-th element of a.
It is guaranteed that the sum of n over all test cases does not exceed 2⋅105 (∑n≤2⋅10**5).
Output
For each test case, print the answer — the maximum sum of the maximum by size (length) alternating subsequence of a.
Example
input
4
5
1 2 3 -1 -2
4
-1 -2 -1 -3
10
-2 8 3 8 -4 -15 5 -2 -3 1
6
1 -1000000000 1 -1000000000 1 -1000000000
output
2
-1
6
-2999999997
Note
In the first test case of the example, one of the possible answers is [1,2,3–,−1–––,−2].
In the second test case of the example, one of the possible answers is [−1,−2,−1–––,−3].
In the third test case of the example, one of the possible answers is [−2–––,8,3,8–,−4–––,−15,5–,−2–––,−3,1–].
In the fourth test case of the example, one of the possible answers is [1–,−1000000000–––––––––––––,1–,−1000000000–––––––––––––,1–,−1000000000–––––––––––––].
"""