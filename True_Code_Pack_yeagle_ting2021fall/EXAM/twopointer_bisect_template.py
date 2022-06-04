# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- two pointer-like
--- bisect-like
"""

""" template below for two pointer-like """
# usually 'two-pointer' is two variables control two index
# classic is left & right, can be head & tail, or something else
# frequently, two-pointer comes with greedy

# 466C-Number of Ways, https://codeforces.com/problemset/problem/466/C
n = int(input())
a = [*map(int, input().split())]
s = sum(a) ; ans = 0
if s%3==0:
    n1_3 = s/3
    n2_3 = 2*n1_3
    sum_i = match = 0
    for i in range(n-1):
        sum_i += a[i]
        if sum_i == n2_3:
            ans += match
        if sum_i == n1_3:
            match += 1
print(ans)

# 279B-Books, https://codeforces.com/problemset/problem/279/B
n, t = map(int, input().split())
book = [*map(int, input().split())]
ri = time = read = 0
for li in range(n):
    while ri < n and time + book[ri] <= t:
        time += book[ri]
        ri += 1
    read = max(read, ri-li)
    time -= book[li]
print(read)

# 18211: arms race v0.2, http://cs101.openjudge.cn/practice/18211/
p = int(input())
weapon = sorted(map(int, input().split()))
extra = left = 0
right = len(weapon)-1
while left <= right:
    make, sell = weapon[left], weapon[right]
    if p >= make:
        extra += 1
        p -= make
        left += 1
    else:
        if left == right: break
        p += sell
        extra -= 1
        if extra < 0:
            extra = 0
            break
        right -= 1
print(extra)

# deleting head and tail with 'del'
p = int(input())
weapon = sorted(map(int, input().split()))
if p < weapon[0]:
    ans = 0
else:
    me = enemy = 0
    while weapon:
        make, sell = weapon[0], weapon[-1]
        if p >= make:
            p -= make
            me += 1
            del weapon[0]
        elif len(weapon) > 2 and sell + p >= make:
            p += sell
            enemy += 1
            del weapon[-1]
        else: break
    ans = me - enemy
print(ans)

# 02287: Tian Ji -- The Horse Racing, http://cs101.openjudge.cn/practice/02287/
# this greedy is not easy, strategy need to be clear and accurate
ans = []
while True:
    n = int(input())
    if n == 0: break
    tian = sorted(map(int, input().split()), reverse=True)
    king = sorted(map(int, input().split()), reverse=True)
    win = lost = 0
    for _ in range(n):
        if tian[0] > king[0]:
            win += 1
            del tian[0], king[0]
        elif tian[-1] > king[-1]:
            win += 1
            del tian[-1], king[-1]
        elif tian[-1] < king[0]:
            lost += 1
            del tian[-1], king[0]
    ans += [200*(win - lost)]
print('\n'.join(map(str, ans)))

# 381A-Sereja and Dima, https://codeforces.com/problemset/problem/381/A
# deleting head and tail too
input()
card = [*map(int, input().split())]
s = d = k = 0
while card:
    k += 1
    if card[0] > card[-1]:
        take = card[0]
        del card[0]
    else:
        take = card[-1]
        del card[-1]
    if k%2:
        s += take
    else:
        d += take
print(s, d)

# 1343C-Alternating Subsequence, https://codeforces.com/problemset/problem/1343/C
# maybe this is a dp without using list? variable will do.
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





""" template below for bisect-like """
import bisect
a1 = [1, 3, 5, 7]
print(bisect.bisect_left(a1, 2))     # 1
print(bisect.bisect_right(a1, 2))    # 1
print(bisect.bisect_left(a1, 5))     # 2
print(bisect.bisect_right(a1, 5))    # 3
a2 = [2, 4, 6, 8]
bisect.insort(a2, 3) ; print(a2)     # [2, 3, 4, 6, 8]
bisect.insort(a2, 4) ; print(a2)     # [2, 3, 4, 4, 6, 8]
# both bisect & insort default to right
# for insort left & right, result is the same (details refer to help(bisect))

# 706B-Interesting drink, https://codeforces.com/problemset/problem/706/B
from bisect import bisect_right as bi_r
i, p = int, input ; p()
price = sorted(map(i, p().split()))
ans = [bi_r(price, i(p())) for _ in range(i(p()))]
print('\n'.join(map(str, ans)))

# 474B-Worms, https://codeforces.com/problemset/problem/474/B
from bisect import bisect_left as bil
n = int(input())
piles = [*map(int, input().split())]
for i in range(1,n):
    piles[i] += piles[i-1]
input()
juicy = [*map(int, input().split())]
ans = [bil(piles, j) + 1 for j in juicy]
print('\n'.join(map(str, ans)))

# 18164: cut rope, http://cs101.openjudge.cn/practice/18164/
# refer to bisect code of classmate Huang-ZhangYi
import bisect
N, cost = int(input()), 0
part = sorted(map(int, input().split()))
while len(part) != 1:
    link = part.pop(0) + part.pop(0)
    bisect.insort(part, link)
    cost += link
print(cost)

# when we can't directly apply bisect, it will be harder...

# 04135: monthly expenses, http://cs101.openjudge.cn/practice/04135/
# https://blog.csdn.net/qq_51767234/article/details/118034450
# translated from C++ code, specialised binary search
N, M = map(int, input().split())
days = [0]*N
max_exp = sum_exp = 0
for d in range(N):
    exp = int(input())
    days[d] = exp
    max_exp = max(max_exp, exp)
    sum_exp += exp
low = max_exp
upp = sum_exp
mid = low + (upp-low)//2
while low != upp:
    fajo = 1
    sum_tmp = 0
    for i in range(N):
        sum_tmp += days[i]
        if sum_tmp > mid:
            fajo += 1
            sum_tmp = days[i]
        elif sum_tmp == mid:
            fajo += 1
            sum_tmp = 0
    if fajo <= M:
        upp = mid-1
    else:
        low = mid+1
    mid = low + (upp-low)//2
print(mid)

# river hopscotch, http://cs101.openjudge.cn/practice/08210/
L, N, M = map(int, input().split())
rock = [0, *[int(input()) for _ in range(N)], L]
def too_far(x):
    num_rock = cur_rock = 0
    for i in range(1, N+2):
        if rock[i] - cur_rock < x:
            num_rock += 1
        else:
            cur_rock = rock[i]
        if num_rock > M:
            return True
    else: return False
low, upp = 0, L
while low != upp:           # do the search untill low == upp
    mid = (low + upp)//2
    if too_far(mid):
        upp = mid           # when 'too_far', 'upp' can't exceed 'mid'
    else:
        low = mid+1         # else 'low' should be higher a little bit
print(low-1)