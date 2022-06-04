# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    n,m,b = map(int,input().split())
    skill={}
    for _ in range(n):
        ti,xi = map(int,input().split())
        if ti in skill: skill[ti].append(xi)
        else: skill[ti] = [xi]
    time = sorted(skill)
    for t in time:
        pro = sorted(skill[t],reverse=True)
        b -= sum(pro[:m])
        if b<1: ans.append(str(t)) ; break
    else: ans.append('alive')
print('\n'.join(ans))

"""info
Created on Tue Nov  9 08:17:42 2021
@author: Asus
http://cs101.openjudge.cn/practice/18182/
18182:打怪兽(sorting,math)v0.2
总时间限制: 1000ms 内存限制: 131072kB
描述
Q神无聊的时候经常打怪兽。现在有一只怪兽血量是b，Q神在一些时刻可以选择一些技能打怪兽，每次释放技能都会让怪兽掉血。
现在给出一些技能ti,xi，代表这个技能可以在ti时刻使用，并且使得怪兽的血量下降xi。这个打怪兽游戏有个限制，每一时刻最多可以使用m个技能（一个技能只能用一次）。如果技能使用得当，那么怪兽会在哪一时刻死掉呢？
输入
第一行是数据组数nCases, nCases<=100
对于每组数据，第一行是三个整数n,m,b，n代表技能的个数，m代表每一时刻可以使用最多m个技能，b代表怪兽初始的血量。
1<=n<=1000，1<=m<=1000，1<=b<=10^9
接下来n行，每一行一个技能ti,xi，1<=ti<=10^9，1<=xi<=10^9
输出
对于每组数据，输出怪兽在哪一时刻死掉，血量小于等于0就算挂，如果不能杀死怪兽，输出alive
样例输入
2
1 1 10
1 5
2 2 10
1 5
1 5
样例输出
alive
1
提示
技能不保证按照时刻顺序输入
"""