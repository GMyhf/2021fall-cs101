# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- some special lines
--- sys
--- re
--- heapq
--- collections
math in math_template.py
bisect in twopointer_bisect_template.py
"""

""" template below for some special lines """
# simplify the import, if in spyder, the analysis is fine
from math import *
print(ceil(1.23))

from bisect import bisect_right as bir
print(bir([1, 3, 5], 4))

""" template below for sys """
# I seldom use it, but it's cool
import sys

# a faster input():
sys.stdin.readline()
# a faster print():
sys.stdout.write('string')
# suggestion: if test or debug needed, run both of above on leetcode playground

# when heavy recursion is needed, we can:
sys.setrecursionlimit = 100000

# when we want to know a data contains how much memory:
sys.getsizeof(1)
sys.getsizeof('word')
sys.getsizeof([1, 2, 3, 4, 5])



""" template below for re """
# regular expression, powerful tool to deal with string
# but, I hadn't learnt a lot about it
# search on web for details of using re
import re
string = 'ascjaacc'
re.match('.s..aac[ac]', string)    # pattern need to be full
re.search('ac', string)            # pattern need to be full
re.findall('a.', string)           # find all matched and return a list

# 03087: verify mail, http://cs101.openjudge.cn/practice/03087/
ans=[] ; frmt='[^@\.]+(\.[^@\.]+)*@[^@\.]+(\.[^@\.]+)+$'
while True:
    try:
        if re.match(frmt, input()): ans.append('YES')
        else: ans.append('NO')
    except EOFError: break
print('\n'.join(ans))



""" template below for heapq """
# Python documentation: https://docs.python.org/zh-cn/3/library/heapq.html
import heapq
N = int(input())
cut = [*map(int, input().split())]
heapq.heapify(cut)
ans = 0
for _ in range(N-1):
    a = heapq.heappop(cut)
    b = heapq.heappop(cut)
    cost = a + b
    heapq.heappush(cut, cost)
    ans += cost
print(ans)

array = [1, 5, 7, 8, 9, 6, 3, 10, 4, 2]
heapq.heapify(array)        # turn a list into a heap
# array becomes [1, 2, 3, 4, 5, 6, 7, 10, 8, 9]
heapq.heappop(array)        # pop smallest, maintaining heap
# array becomes [2, 4, 3, 8, 5, 6, 7, 10, 9]
heapq.heappush(array, 2)    # push 9 onto heap, maintaining heap
# array becomes [2, 2, 3, 8, 4, 6, 7, 10, 9, 5]



""" template below for collections """
# actually, collections got MANY useful function, worth to take a look
# unfortunately, I got no time for that... here's what I solved using collections:

# 1335C-Two Teams Composing, https://codeforces.com/problemset/problem/1335/C
from collections import Counter
ans=[]
for _ in range(int(input())):
    n = int(input())
    stu = sorted(map(int, input().split()))
    if n < 2: ans.append(0) ; continue
    diff = len(set(stu))
    same = Counter(stu).most_common(1)[0][1]
    ans.append(max(min(diff, same-1), min(diff-1, same)))
print('\n'.join(map(str, ans)))
# collections.Counter.most_common(x) get first x most common elements
Counter('abcdeabcdabcaba').most_common(3)
# out: [('a', 5), ('b', 4), ('c', 3)]