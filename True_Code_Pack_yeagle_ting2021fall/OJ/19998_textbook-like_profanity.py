# -*- coding: utf-8 -*-
n, m = map(int, input().split())
mons = sorted([*map(int, input().split())]+[*map(int, input().split())])
done = 0
while True:
    n -= 1 ; m -= 2
    if n < 0 or m < 0: break
    mons = [hp-1 for hp in mons]
    kill = False
    while True:
        if not mons:
            done = 1 ; break
        elif mons[0]:
            if kill:
                n += 1 ; m += 2
                kill = False
            else: break
        else:
            kill = True
            del mons[0]
    if done: break
print(['NO', 'YES'][done])

"""info
Created on Thu Dec 23 10:40:08 2021
@author: Asus
http://cs101.openjudge.cn/practice/19998/
19998:教科书般的亵渎
总时间限制: 1000ms 内存限制: 65536kB
描述
在《炉石传说》这款游戏中，有一种名叫“亵渎”的法术，其效果为：对场上所有随从造成1点伤害，如果有随从死亡，则再次施放该法术（再次施放是自动的，无需从手牌中打出另一张“亵渎”）。每次你从手牌中打出一张“亵渎”，你的可用费用会减2。
输入
第一行为两个整数，M和N，M代表你手牌中“亵渎”的数量(0≤M≤2)，N代表你目前的可用费用（0≤N≤10）；
接下来2行每行7个整数，分别代表你场上7个随从的生命值和对手场上7个随从的生命值(1≤x≤10)。
输出
若能够达到清场的效果（即场上所有随从都死亡），则输出YES，否则输出NO。
样例
Sample1 Input：
2 10
3 3 5 2 2 6 4 
1 1 4 8 8 3 7 
Sample1 Output:
YES

Sample2 Input：
2 4
8 1 5 8 8 6 2 
1 5 9 8 4 8 5 
Sample2 Output:
NO
"""