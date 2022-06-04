# -*- coding: utf-8 -*-
input() ; mgc=set() ; ans=[]
num = [int(x) for x in input().split()]
mx = int(max(num)**0.5)+1
sqr = [k**2 for k in range(1,mx)]
for i in sqr:
    for j in sqr:
        mgc.add(i+j)
for x in num:
    if x in mgc:
        ans.append([bin(x),oct(x),hex(x)])
for a in ans:
    print(' '.join(a))

"""info
Created on Mon Oct 25 15:01:41 2021
@author: Asus
http://cs101.openjudge.cn/practice/18224/
18224:找魔数
总时间限制: 1000ms 内存限制: 65536kB
描述
一个数如果能表示为两个完全平方数的和（两个正整数的平方和，如：2^2+4^2=20, 1^2+4^2=17），则称为魔数。要求你在一堆数字中找出魔数，并且分别以二进制、八进制、十六进制输出这个数字。
输入
第一行1个整数，代表m个数字（1≤m≤100）
接下来1行，为m个整数， Xi (1≤Xi≤1000)。
输出
每个魔数1行，以空格间隔输出该魔数的二进制、八进制、十六进制
（注：如果出现abcdef等字母，都按小写输出）
样例输入
4
3 9 20 17
样例输出
0b10100 0o24 0x14
0b10001 0o21 0x11
"""