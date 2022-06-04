# -*- coding: utf-8 -*-
ans = []
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = set(input().split())
    b = set(input().split())
    c = a&b
    if c:
        ans.append('YES')
        ans.append('1 %s'%c.pop())
    else:
        ans.append('NO')
print('\n'.join(ans))

"""info
Created on Sat Dec 11 08:33:45 2021
@author: Asus
https://codeforces.com/problemset/problem/1382/A
1382A-Common Subsequence
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

You are given two arrays of integers a1,…,an and b1,…,bm.
Your task is to find a non-empty array c1,…,ck that is a subsequence of a1,…,an, and also a subsequence of b1,…,bm. If there are multiple answers, find one of the smallest possible length. If there are still multiple of the smallest possible length, find any. If there are no such arrays, you should report about it.
A sequence a is a subsequence of a sequence b if a can be obtained from b by deletion of several (possibly, zero) elements. For example, [3,1] is a subsequence of [3,2,1] and [4,3,1], but not a subsequence of [1,3,3,7] and [3,10,4].

Input
The first line contains a single integer t (1≤t≤1000)  — the number of test cases. Next 3t lines contain descriptions of test cases.
The first line of each test case contains two integers n and m (1≤n,m≤1000)  — the lengths of the two arrays.
The second line of each test case contains n integers a1,…,an (1≤ai≤1000)  — the elements of the first array.
The third line of each test case contains m integers b1,…,bm (1≤bi≤1000)  — the elements of the second array.
It is guaranteed that the sum of n and the sum of m across all test cases does not exceed 1000 (∑i=1tni,∑i=1tmi≤1000).
Output
For each test case, output "YES" if a solution exists, or "NO" otherwise.
If the answer is "YES", on the next line output an integer k (1≤k≤1000)  — the length of the array, followed by k integers c1,…,ck (1≤ci≤1000)  — the elements of the array.
If there are multiple solutions with the smallest possible k, output any.
Example
input
5
4 5
10 8 6 4
1 2 3 4 5
1 1
3
3
1 1
3
2
5 3
1000 2 2 2 3
3 1 5
5 5
1 2 3 4 5
1 2 3 4 5
output
YES
1 4
YES
1 3
NO
YES
1 3
YES
1 2
Note
In the first test case, [4] is a subsequence of [10,8,6,4] and [1,2,3,4,5]. This array has length 1, it is the smallest possible length of a subsequence of both a and b.
In the third test case, no non-empty subsequences of both [3] and [2] exist, so the answer is "NO".
"""