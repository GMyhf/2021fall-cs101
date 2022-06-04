# -*- coding: utf-8 -*-
def pFactors(n):
    pFact, limit, check, num = [], int(n**0.5) +1, 2, n
    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num /= check
    if num > 1: pFact.append(num)
    return pFact
memo = pFactors(int(input()))
x, y = len(memo), len(set(memo))
print(0 if x-y else [1,-1][x%2])

"""info
Created on Tue Dec 28 16:20:10 2021
@author: Asus
http://cs101.openjudge.cn/practice/23564/
23564:数论
总时间限制: 1000ms 内存限制: 65536kB
描述
M函数在数论中应用广泛，这里记为μ。
无平方数因数的数（square-free integer）是指其因数中，没有一个是平方数的正整数。简言之，将一个这样的数予以质因数分解（即，一个整数写成几个质数的乘积）后，所有质因数的幂都不会大于或等于2。
对于任何正整数n，定义μ(n)的值域为{-1, 0, 1}，μ(n)的值取决于n的质因数分解：
• 如果n是一个具有偶数个质因数，且无平方质因数的正整数，那么μ(n)=1。
• 如果n是一个具有奇数个质因数，且无平方质因数的正整数，那么μ(n)=-1。
• 如果n存在平方质因数，那么μ(n)=0。
例如n=75，存在平方质因数5，75=3*(5^2)，5是75的质因数，且次数为2。
输入
一行，一个整数n，保证 n <= 10^6。
输出
一行，一个整数 μ(n)
样例
Sample Input1:
12
Sample Output1:
0
解释
n=12=2*2*3，存在平方质因数2，故μ(n)=0。

Sample Input2:
1
Sample Output2:
1
解释
1没有质因数，质因数数量为0，0是偶数，故μ(n)=1。

Sample Input3:
25935
Sample Output3:
-1
解释
n=25935=3*5*7*13*19，含有奇数个质因数，且不存在平方质因数，故μ(n)=-1。

Sample Input4:
30013
Sample Output4:
-1
解释
30013 = 30013，有1个质因数，且不存在平方质因数，故μ(n)=-1。

提示
tags: number theory, math
通过搜索引擎，找到一个看起来可用的函数。
# https://stackoverflow.com/questions/14550794/python-integer-factorization-into-primes
def pFactors(n):
    ''' Finds the prime factors of 'n' '''
    from math import sqrt
    pFact, limit, check, num = [], int(sqrt(n)) + 1, 2, n

    for check in range(2, limit):
        while num % check == 0:
            pFact.append(check)
            num /= check
    if num > 1:
        pFact.append(num)
    return pFact

#print(pFactors(12))
#[2, 2, 3]
#print(pFactors(1))
#[]
#print(pFactors(30013))
#[30013]
"""