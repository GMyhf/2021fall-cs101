# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- some classic 'bags'
--- Longest Ordered Subsequence
# ! as dp had too much content, parts below put in dp2_template.py
--- Prefix Sum
--- others
"""
# !!! author DID NOT REALLY & FULLY unterstand types of 'bag problem' !!!
# !!! template below is depend on personal understanding and ideas !!!

""" template below for some classic 'bags' """

# thief's bag, http://cs101.openjudge.cn/practice/23421/
# If possible, avoid using matrix(2D-list) as 'dp',
# lower the dimension where index of 'dp' is one of the data,
# and each element in 'dp' will be paired with its index.
N, maxi = map(int, input().split())    # input depend on data's format
E = [*map(int, input().split())]       # E = earn, same idea with 'value'
M = [*map(int, input().split())]       # M = mass, same idea with 'costs'
pair = [*zip(E, M)]
dp = [0]*(maxi+1)                      # consider proper length and default value
for i in range(N):
    mass = pair[i][1]
    if mass > maxi: continue           # skip some impossible cases
    earn = pair[i][0]
    for bag in range(maxi, 0, -1):     # reversed index move
        if bag >= mass:                # proper controlled condition
            dp[bag] = max(dp[bag], dp[bag-mass] + earn)    # core of dp
print(dp[-1])
''' sample input:
3 4
3000 2000 1500
4 3 1
'''
# similarly, pick herb, http://cs101.openjudge.cn/practice/02773/



# enrich winter holiday, http://cs101.openjudge.cn/practice/16528/
# set some operations to 'prepare' the data, it will simplify dp
event = [-1]*61
for _ in range(int(input())):
    start, end = map(int, input().split())
    event[end] = max(event[end], start)
dp = [0]*61
for d in range(61):
    remain = dp[d-1]
    taking = dp[event[d]-1] +1
    if event[d] > -1:                  # proper controlled condition
        dp[d] = max(remain, taking)    # core of dp
    else:
        dp[d] = remain    # also core of dp
print(dp[-1])



# 189A-Cut Ribbon, https://codeforces.com/problemset/problem/189/A
# gives limiting condition to total_costs
n, a, b, c = map(int, input().split())
dp = [0]+[-4000]*n                      # default = -inf so won't bother others
cut = {k for k in {a,b,c} if k <= n}    # filter impossible cut value
for i in range(min(cut), n+1):          # start from first legal cut
    for x in cut:                       # trying each cut
        dp[i] = max(dp[i], dp[i-x]+1)   # dp[i] as can't cut, dp[i-x]+1 as can cut
print(dp[n])    # same as dp[-1] in this case



# gym, http://cs101.openjudge.cn/practice/21458/
# strictly asked for when total_costs == xx, best total_value
T, n = map(int, input().split())
plan = [[*map(int, input().split())] for _ in range(n)]
dp = [0]+[-1]*T    # if some costs(index) have no pairing value, default -1 as asked
for i in range(n):
    time, work = plan[i]
    for t in range(T, 0, -1):    # reversed index move
        if t >= time and dp[t-time] != -1:         # proper controlled condition
            dp[t] = max(dp[t], dp[t-time]+work)    # core of dp
print(dp[-1])





""" template below for Longest Ordered Subsequence """

# http://cs101.openjudge.cn/practice/02757/
# http://cs101.openjudge.cn/practice/02533/ (English version)

n = int(input())                   # n = length of 's' below
s = [*map(int,input().split())]    # s = original and full sequence
dp = [1]*n                         # a single num is shortest subseq, so default 1
for i in range(n):                 # this double 'for' is well designed,
    for j in range(i):             # explaination is put below sample input
        if s[j] < s[i]:                    # proper controlled condition
            dp[i] = max(dp[i], dp[j]+1)    # core of dp
print(max(dp))    # it will not certainly be dp[-1]
''' sample input:
7
1 7 3 5 9 4 8
output: 4
'''

# first 'for' loop go through each index i till the end of the sequence, 
# when doing that, second 'for' loop go through ecah index j that is before i.
# Result: index of 'dp' is index of 's', meaning if we take s[i] in a subsequence,
# then dp[i] will be the length of 'Longest Ordered Subsequence'.
# And that's why the max length will not be dp[-1].



# application of 'Longest Ordered Subsequence' concept

# max sum of ordered subsequence, http://cs101.openjudge.cn/practice/03532/
# the subsequence with max sum won't necessarily be the longest subsequence
# generally same with 'Longest Ordered Subsequence', refer to explaination above
n = int(input())
*s, = map(int, input().split())    # 's' is also the full sequence, just a tuple type
dp = list(s)                       # a single num is shortest subseq, so default itself
for i in range(n):
    for j in range(i):
        if s[j] < s[i]:
            dp[i] = max(dp[i], dp[j]+s[i])    # core of dp, +1 changed to +s[i]
print(max(dp))
''' sample input:
7
1 7 3 5 9 4 8
output: 18
'''



# climb moutain, http://cs101.openjudge.cn/practice/02995/
# actually, we can go down!!! so need to consider reversed condition

n = int(input())
view = [*map(int,input().split())]
dp_up = [1]*n
for i in range(n):
    for j in range(i):
        if view[j] < view[i]:
            dp_up[i] = max(dp_up[i], dp_up[j]+1)    # till here same with original
view.reverse()             # there we go, reversed the sequence
dp_down = [1]*n            # prepare another 'dp' list
for i in range(n):         # and do the samething again
    for j in range(i):
        if view[j] < view[i]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)
dp_down.reverse()          # by this got a reversed result, so need to reverse it again
dp = [dp_up[x] + dp_down[x]-1 for x in range(n)]    # then merge both 'dp', get final result
print(max(dp))
''' sample input:
8
186 186 150 200 160 130 197 220
output: 4
'''
# why -1 ? as both 'dp' take view[i], view[i] will be taken twice, so treat the bug by -1

# choir formation, http://cs101.openjudge.cn/practice/02711/
# everything, including sample, is same with climb moutain, just one thing:
print(n-max(dp))    # last line is different as asked
# sample output is just coincidence (4 == 8-4), most data will have different output