# -*- coding: utf-8 -*-
# just lay out every permutation
ans=[]
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    p = a+b+c+d ; h = -a+b+c+d
    q = a-b+c+d ; i = -a-b+c+d
    r = a+b-c+d ; j = -a+b-c+d
    s = a+b+c-d ; k = -a+b+c-d
    t = a+b-c-d ; l = -a+b-c-d
    x = a-b+c-d ; m = -a-b+c-d
    y = a-b-c+d ; n = -a-b-c+d
    z = a-b-c-d
    if 24 in (h,i,j,k,l,m,n,p,q,r,s,t,x,y,z): ans.append('YES')
    else: ans.append('NO')
for a in ans: print(a)

# be smarter with the for_s
ans=[]
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    can = 0
    for w in(a,-a):
        if can: break
        for x in(b,-b):
            if can: break
            for y in(c,-c):
                if can: break
                for z in(d,-d):
                    if w+x+y+z==24: can=1
                    elif can: break
    if can: ans.append('YES')
    else: ans.append('NO')
for a in ans: print(a)

"""info
Created on Mon Oct 25 14:05:47 2021
@author: Asus
http://cs101.openjudge.cn/practice/18223/
18223:24点
总时间限制: 1000ms 内存限制: 65536kB
描述
给定4个整数，判断是否能只用加减运算（即在4个数中间插入3个+或-符号，可以调换数字顺序），使得运算结果为24。
输入
第一行1个整数，代表m组数据（1≤m≤100）
接下来m行，每行为4个整数， Xi (1≤Xi≤10^100)，注意整数可能很大。
输出
共m行，每行为YES或者NO，代表是否能凑成24点。
对于如下输入，6+6+6+6=24,25-3+1+1=24，100000000000000000000000-100000000000000000000000-100000000000000000000000+100000000000000000000024=24
样例输入
4
6 6 6 6
3 25 1 1
100000000000000000000000 100000000000000000000000 100000000000000000000000 100000000000000000000024
2 3 4 5
样例输出
YES
YES
YES
NO
"""