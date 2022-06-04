# -*- coding: utf-8 -*-
n = int(input())
ans = []
for i in range(1,n+1):
    c1 = '7' not in str(i)
    c2 = i%7!=0
    if c1 and c2: ans.append(i**2)
print(sum(ans))

#packed_code
ans = []
for i in range(1,int(input())+1):
    if ('7' not in str(i)) and (i%7!=0):
        ans.append(i**2)
print(sum(ans))

#better_without_list
ans=0
for i in range(1,int(input())+1):
    if ('7' not in str(i)) and (i%7!=0):
        ans+=i**2
print(ans)

"""info
Created on Thu Oct  7 08:55:30 2021
@author: Asus
http://cs101.openjudge.cn/practice/2701/
2701:与7无关的数
总时间限制: 1000ms 内存限制: 65536kB
描述
一个正整数,如果它能被7整除,或者它的十进制表示法中某一位上的数字为7,则称其为与7相关的数.现求所有小于等于n(n < 100)的与7无关的正整数的平方和.
输入
输入为一行,正整数n(n < 100)
输出
输出一行，包含一个整数，即小于等于n的所有与7无关的正整数的平方和。
样例输入
21
样例输出
2336
"""