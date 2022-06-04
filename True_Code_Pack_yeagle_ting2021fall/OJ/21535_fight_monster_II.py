# -*- coding: utf-8 -*-
mon = []
n,w = map(int,input().split())
atk = sum(map(int,input().split()))
for _ in range(n):
    df,hp = map(int,input().split())
    if atk >= df: mon += [hp]
mon.sort() ; m = len(mon)
for i in range(m):
    w -= mon[i]
    if w<0: ans = i ; break
else: ans = m
print(ans)

"""info
Created on Mon Nov 15 14:00:12 2021
@author: Asus

21535:打怪兽II (implementation)
总时间限制: 1000ms 内存限制: 65536kB
描述
Q神在打败了怪兽之后，耗费了很多的魔法值，只剩下了 w 点魔法值，并且只能释放一个技能。
但是，Q神得到了一件可以强化技能魔法权杖，这个魔法权杖对Q神的技能，具有增幅效果（强化后的技能伤害等于原技能伤害加上强化值）。
与此同时，怪兽也得到了进一步的加强，每一个怪兽都有一个大小为 x 的魔法护盾和大小为 y 的生命值。
1）如果经过强化后的技能伤害小于怪兽的魔法护盾，那么Q神就无法战胜这个怪兽，
2）如果强化后的技能伤害大于等于怪兽的魔法护盾，那么Q神就可以击败这个怪兽，但是会消耗 y 点魔法值。
如果魔法值小于 y，则无法释放技能，自然不能打败怪兽。
Q神想知道自己最多能打败多少只怪兽。

输入
第一行为两个整数 n 和 w，其中 n 表示怪兽的数量, w 表示剩余魔法值
第二行为两个整数 P 和 Q，其中 P 表示技能的基础伤害，Q表示增幅效果
接下来的 n 行，每行两个整数 xi 和 yi，分别表示第 i 只怪兽的魔法护盾值和生命值
数据范围：0 <= n,w <= 5000，0 <= P,Q <= 200
0 <= x <= 1000，0 <= y <= 70
输出
一个整数，表示Q神最多能打败的怪兽的数量.

样例

sample1 in:
10 13
108 76
33 6
36 18
102 19
98 5
114 11
0 5
39 12
108 6
99 0
34 4
sample1 out:
3

sample2 in:
5 14
25 99
150 18
57 16
131 11
197 0
96 17
sample2 out:
0

sample3 in:
3 4
38 64
184 9
70 1
57 3
sample3 out:
2
"""