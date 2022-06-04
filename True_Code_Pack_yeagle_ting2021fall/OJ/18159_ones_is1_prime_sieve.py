# -*- coding: utf-8 -*-
ns=[] ; ans=[] ; k=0
for _ in range(int(input())): ns.append(int(input()))
def sieve(e):
    p_id = [1]*(e+1)
    for i in range(2,int(e**0.5)+1):
        if p_id[i]:
            for j in range(i*i,e+1,i): p_id[j]=0
    return [x for x in range(2,e+1) if p_id[x]]
p_list = sieve(max(ns))
for n in ns:
    if n<12: ans.append(['NULL'])
    else:
        tmp=[]
        for p in p_list:
            if p<n and p%10==1: tmp.append(p)
            elif p>=n: break
        ans.append(tmp)
for a in ans:
    k+=1
    print('Case%d:'%k)
    print(*a)

"""info
Created on Thu Oct 28 11:04:53 2021
@author: Asus
http://cs101.openjudge.cn/practice/18159/
18159:个位为 1 的质数个数(Sieve of Eratosthenes)
总时间限制: 1000ms 内存限制: 65536kB
描述
当输入一个整数 n(2<=n<=10001),要求输出所有从 1 到这个整数之间(不包括 1 和这个整数)且个位数是 1 的素数, 如果没有则输出NULL
输入
第一行是一个整数T，1 < T <10001, 表示有T个数据需要测试。
接下来的T行每行有一个大于1的正整数n。
注意时间复杂度，提示不要对每一个测试数据都从头开始找一遍素数。
输出
注意参照样例，Cases等字符也要输出。
然后输出所有从 1 到这个整数n之间(不包括 1 和这个整数) 且个位为 1 的素数(素数之间用空格隔开,每一行输出的最后面都没有空格),
如果没有则输出NULL。
样例输入
3
5
12
110
样例输出
Case1:
NULL
Case2:
11
Case3:
11 31 41 61 71 101
"""