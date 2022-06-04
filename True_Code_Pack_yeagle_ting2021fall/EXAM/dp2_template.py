# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- some classic 'bags'
--- Longest Ordered Subsequence
# ! as dp had too much content, parts above put in dp1_template.py
--- Prefix Sum
--- others
"""
# warning once again:
# !!! author DID NOT REALLY & FULLY unterstand types of 'bag problem' !!!
# !!! template below is depend on personal understanding and ideas !!!

""" template below for Prefix Sum """

# 368B-Sereja and Suffixes, https://codeforces.com/problemset/problem/368/B
n,m = map(int, input().split())
array = [*reversed(input().split())]
distinct = set()    # assisting set
n_dstt = [0]*n      # stores data of dp
for i in range(n):
    a = array[i]
    if a not in distinct: distinct.add(a)
    n_dstt[-i-1] = len(distinct)           # do prefix sum, specialised to condition given
print('\n'.join([str(n_dstt[int(input())-1]) for _ in range(m)]))

# 313B-Ilya and Queries, https://codeforces.com/contest/313/problem/B
s = input()
same, cnt, ans = [0], 0, []    # 'same' stores data of dp, 'cnt' is assisting variable
for i in range(1, len(s)):                # this loop do prefix sum, specialised too
    if s[i] == s[i-1]: cnt += 1
    same.append(cnt)
for _ in range(int(input())):
    li, ri = map(int, input().split())
    ans.append(same[ri-1]-same[li-1])     # extract answer by calculation
print('\n'.join(map(str, ans)))

# 706B-Interesting drink, https://codeforces.com/problemset/problem/706/B
n = int(input())
price = [*map(int,input().split())]
x = max(price)
buy = [0]*(x+1)               # 'buy' stores data of dp
for i in price:               # first loop do preparation with data in 'price'
    buy[i] += 1
for j in range(2, x+1):       # second loop do prefix sum, classic style
    buy[j] += buy[j-1]
day = int(input())
ans = [0]*day
for d in range(day):          # this loop get answer according to input
    m = int(input())
    if m<x: ans[d] = buy[m]
    else: ans[d] = n
print('\n'.join(map(str, ans)))

# 455A-Boredom, https://codeforces.com/problemset/problem/455/A
# kinda similar to 706B-Interesting drink, but this is a merge with 'bag problem'
input()
*a, = map(int, input().split())
x = max(a)        # get the upper boundary of dp operation
an = [0]*(x+1)    # assisting list
for i in a:       # doing preparation
    an[i] += 1
dp = [0]*(x+1)    # stores data of dp
for j in range(1, x+1):
    dp[j] = max(dp[j-1], dp[j-2] + an[j]*j)    # special style of prefix sum (?)
print(dp[-1])
# open great space: replacing 'x = max(a)' with 'x = 100000', also nice

# 02753:fibonacci_sequence, http://cs101.openjudge.cn/practice/02753/
# a very classic dp, must learn this when learning dp
def fib(n):
    if n<3: return 1
    memo = [1,1] + [0]*(n-2)
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1]





""" template below for others """

# 02760:the triangle, http://cs101.openjudge.cn/practice/02760/
# http://cs101.openjudge.cn/practice/01163/ (English version)

# going up
n = int(input())
tri = [[*map(int, input().split())] for _ in range(n)]
for i in range(n-2, -1, -1):
    for j in range(i+1):                                # from lower layer,
        tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])    # take bigger in left & right
print(tri[0][0])    # answer is at the top

# going down
n = int(input())
tri = [[0, *map(int, input().split()), 0] for _ in range(n)]    # protected edge
for i in range(1, n):
    for j in range(1, i+2):                             # from upper layer,
        tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])    # take bigger in left & right
print(max(tri[-1]))    # several answers at the bottom, take max

''' sample input:
5
7
3 8
8 1 0 
2 7 4 4
4 5 2 6 5
output: 30
'''



# 02806:Common Subsequence, actually is another classic, but we rarely use
# http://cs101.openjudge.cn/practice/02806/
# http://cs101.openjudge.cn/practice/01458/ (English version)
# bottom-up dp

def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]
ans = []
while True:
    try: x, y = input().split()
    except EOFError: break
    ans.append(lcs_dp(x, y))
print('\n'.join(map(str, ans)))
''' sample input:
abcfbc         abfcab
programming    contest 
abcd           mnp
output:
4
2
0
'''
# it can be solved by recursive method too, but it can be TLE...



# 04117:easy integar distribution, http://cs101.openjudge.cn/practice/04117/
# refer to code of BoHai-Li in 2020fall-cs101.openjudge.cn_problems.pdf
ans = []
while True:
    try: n = int(input())
    except EOFError: break
    dp = [[0]*(n+1) for _ in range(n+1)]
    for k in range(n+1):
        dp[k][1] = 1
        dp[0][k] = 1
    for i in range(1, n+1):
        for j in range(2, n+1):
            dp[i][j] = dp[i][j-1]
            if i >= j: dp[i][j] += dp[i-j][j]
    ans.append(dp[n][n])
print('\n'.join(map(str, ans)))

# I didn't understand the hard one, so I didn't rewrite the code ...