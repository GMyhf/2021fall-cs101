# -*- coding: utf-8 -*-
def sieve(s,e):
    p_id = [1]*(e+1)
    for i in range(2,int(e**0.5)+1):
        if p_id[i]:
            for j in range(i*i,e+1,i): p_id[j]=0
    if s<2: s=2
    prime = [x for x in range(s,e+1) if p_id[x]]
    if len(prime): return prime
    else: return [-1]
ans=[]
for _ in range(int(input())):
    s,e = map(int,input().split())
    ans.append(sieve(s,e))
for a in ans: print(*a)

"""info
Created on Thu Oct 28 10:45:06 2021
@author: Asus
http://cs101.openjudge.cn/practice/18107/
18107:质数个数(Sieve of Eratosthenes)
总时间限制: 1000ms 内存限制: 65536kB
描述
输出一个区间内（包含两端点）的所有质数。
输入
第一行是一个整数 T (T <= 50) ，表示一共有 T 组数据。
接下来的每组数据为两个整数，分别为m和n，保证m<=n。
输出
每组数据对应一行，输出在m和n之间（包含m和n）的所有素数，中间用空格隔开。如果答案不存在，输出-1。
样例输入
3
4 5
1 10
8 9
样例输出
5
2 3 5 7
-1
"""