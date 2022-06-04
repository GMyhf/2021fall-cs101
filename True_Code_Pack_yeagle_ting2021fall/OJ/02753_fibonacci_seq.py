# -*- coding: utf-8 -*-
def fib(n):
    if n<3: return 1
    memo = [1,1]+[0]*(n-2)
    for i in range(2,n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1]
ans=[]
for _ in range(int(input())):
    ans.append(str(fib(int(input()))))
print('\n'.join(ans))

# build fibonacci upto biggest n, then do index (without def)
ns = [int(input()) for _ in range(int(input()))]
nx = max(ns) ; memo = [1,1]
if nx>2:
    memo += [0]*(nx-2)
    for i in range(2,nx):
        memo[i] = memo[i-1] + memo[i-2]
ans = [str(memo[n-1]) for n in ns]
print('\n'.join(ans))

"""info
Created on Wed Nov  3 13:36:07 2021
@author: Asus
http://cs101.openjudge.cn/practice/02753/
02753:菲波那契数列
总时间限制: 1000ms 内存限制: 65536kB
描述
菲波那契数列是指这样的数列: 数列的第一个和第二个数都为1，接下来每个数都等于前面2个数之和。
给出一个正整数a，要求菲波那契数列中第a个数是多少。
输入
第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数a(1 <= a <= 20)
输出
输出有n行，每行输出对应一个输入。输出应是一个正整数，为菲波那契数列中第a个数的大小
样例输入
4
5
2
19
1
样例输出
5
1
4181
1
"""