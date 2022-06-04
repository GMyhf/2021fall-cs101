# -*- coding: utf-8 -*-
ans=[]
x = int(input())
if x%2 or x<5:
    print('Error!')
else:
    def eratosthenes(n):
        isprime = [1]*(n+1)
        for i in range(2, int(n**0.5)+1):
            if isprime[i]:
                for j in range(i*i,n+1,i): isprime[j]=0
        return [x for x in range(2,n+1) if isprime[x]]
    x_prime = set(eratosthenes(x))
    for i in range(2, x//2 +1):
        j = x-i
        if i in x_prime and j in x_prime:
            ans += ['%d=%d+%d'%(x, i, j)]
print('\n'.join(ans))

# without def eratosthenes:
ans=[]
x = int(input())
if x%2 or x<5:
    print('Error!')
else:
    isprime = [1]*(x+1)
    for i in range(2, int(x**0.5)+1):
        if isprime[i]:
            for j in range(i*i,x+1,i): isprime[j]=0
    x_prime = set(x for x in range(2,x+1) if isprime[x])
    for i in range(2, x//2 +1):
        j = x-i
        if i in x_prime and j in x_prime:
            ans += ['%d=%d+%d'%(x, i, j)]
print('\n'.join(ans))

"""info
Created on Thu Nov 25 15:18:36 2021
@author: Asus
http://cs101.openjudge.cn/practice/03143/
03134:验证“歌德巴赫猜想”
总时间限制: 1000ms 内存限制: 65536kB
描述
验证“歌德巴赫猜想”，即：任意一个大于等于6的偶数均可表示成两个素数之和。
输入
输入只有一个正整数x。(x<=2000)
输出
如果x不是“大于等于6的偶数”，则输出一行：
Error!
否则输出这个数的所有分解形式，形式为：
x=y+z
其中x为待验证的数，y和z满足y+z=x，而且y<=z，y和z均是素数。
如果存在多组分解形式，则按照y的升序输出所有的分解，每行一个分解表达式。
注意输出不要有多余的空格。

样例输入
输入样例1:
7
输入样例2:
10
输入样例3:
100

样例输出
输出样例1:
Error!
输出样例2:
10=3+7
10=5+5
输出样例3:
100=3+97
100=11+89
100=17+83
100=29+71
100=41+59
100=47+53
"""