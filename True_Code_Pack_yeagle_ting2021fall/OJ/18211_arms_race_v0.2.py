# -*- coding: utf-8 -*-
p = int(input())
weapon = sorted(map(int, input().split()))
if p < weapon[0]:
    ans = 0
else:
    me = enemy = 0
    while weapon:
        make = weapon[0]
        sell = weapon[-1]
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

# truely two pointer code
p = int(input())
weapon = sorted(map(int, input().split()))
extra = left = 0
right = len(weapon)-1
while left <= right:
    make = weapon[left]
    sell = weapon[right]
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

"""info
Created on Tue Nov 23 09:10:17 2021
@author: Asus
http://cs101.openjudge.cn/practice/18211/
18211:军备竞赛(greedy, two pointers) v0.2
总时间限制: 1000ms 内存限制: 65536kB
描述
鸣人是木叶村的村长，最近在跟敌国进行军备竞赛，他手边有N份武器设计图，每张设计图有制作成本（大于等于零）且最多使用一次，可以选择花钱制作或是以同样的价钱卖给敌国，同时任意时刻敌国的武器不能比我国更多，鸣人的目标是在不负债的前提下武器种类比敌国越多越好。
输入
第一行为起始整数经费p,并且0≤p。且要求任何时刻p不能小于0.
第二行为n个整数，以空格分隔，并且0≤每个整数。代表每张设计图的制作成本，同时也是卖价，最多用一次(无法又制作又卖).
输出
一个整数，代表武器种类最多比敌国多多少.

样例
Sample1 Input:
10
20 30 40
Sample1 Output:
0
解释: 10元不足以制作20元的武器，所以为0，也不能先卖50元的，不能让敌国武器比木叶多

Sample2 Input:
10
15 5
Sample2 Output:
1
解释: 10元可以制作5元的武器，木叶的武器比对手多一件

Sample3 Input:
40
20 80 60 40
Sample3 Output:
2
解释: 先制作20元的武器，再贩卖80元的武器，这时经费为100，再制作40、60的武器，木叶的武器比对手多二件
"""