# -*- coding: utf-8 -*-
# code refer to Shubhanshu_sharma on CF, this problem seems not friendly to python...
ans = []
for _ in range(int(input())):
    n = int(input())
    arr = [*map(int,input().split())]
    cnt = [float('inf')]*(n+1)
    if n > 1 and len(set(arr)) == 1:
        ans.append(-1)
        continue
    for i in range(n):
        if cnt[arr[i]] == float('inf'):
            cnt[arr[i]] = 1
        else:
            cnt[arr[i]] += 1
    key = min(cnt)
    if key > 1:
        ans.append(-1)
        continue
    ans.append(arr.index(cnt.index(key)) +1)
print('\n'.join(map(str, ans)))

# tle code by myself...
ans = []
for _ in range(int(input())):
    n = input()
    arr = [*map(int, input().split())]
    odd = []
    new = []
    for i in arr:
        if i in new:
            new.remove(i)
            odd.append(i)
        elif i in odd:
            pass
        else:
            new.append(i)
    new.sort()
    if new:
        ans.append(arr.index(new[0])+1)
    else:
        ans.append(-1)
print('\n'.join(map(str, ans)))

"""info
Created on Thu Dec  9 22:21:08 2021
@author: Asus
https://codeforces.com/problemset/problem/1454/B
1454B-Unique Bid Auction
time limit per test: 1 second
memory limit per test:　256 megabytes
input：　standard input
output：　standard output

There is a game called "Unique Bid Auction". You can read more about it here: https://en.wikipedia.org/wiki/Unique_bid_auction (though you don't have to do it to solve this problem).
Let's simplify this game a bit. Formally, there are n participants, the i-th participant chose the number ai. The winner of the game is such a participant that the number he chose is unique (i. e. nobody else chose this number except him) and is minimal (i. e. among all unique values of a the minimum one is the winning one).
Your task is to find the index of the participant who won the game (or -1 if there is no winner). Indexing is 1-based, i. e. the participants are numbered from 1 to n.
You have to answer t independent test cases.

Input
The first line of the input contains one integer t (1≤t≤2⋅10**4) — the number of test cases. Then t test cases follow.
The first line of the test case contains one integer n (1≤n≤2⋅10**5) — the number of participants. The second line of the test case contains n integers a1,a2,…,an (1≤ai≤n), where ai is the i-th participant chosen number.
It is guaranteed that the sum of n does not exceed 2⋅10**5 (∑n≤2⋅10**5).
Output
For each test case, print the answer — the index of the participant who won the game (or -1 if there is no winner). Note that the answer is always unique.
Example
input
6
2
1 1
3
2 1 3
4
2 2 2 3
1
1
5
2 3 2 4 2
6
1 1 5 5 4 4
output
-1
2
4
1
2
-1
"""