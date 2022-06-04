# -*- coding: utf-8 -*-
a = int(input())
if a%4==0:
    print(int(a/4), int(a/2))
elif a%2==0:
    print(int((a+2)/4), int(a/2))
else:
    print(0, 0)

#print int at final
a = int(input())
if a%4==0:
    x=a/4 ; y=a/2
elif a%2==0:
    x=(a+2)/4 ; y=a/2
else: x=0 ; y=0
print(int(x),int(y))

"""info
Created on Tue Sep 21 12:12:57 2021
@author: Asus
http://cs101.openjudge.cn/practice/2750
2750:鸡兔同笼
总时间限制: 1000ms 内存限制: 65536kB
描述
一个笼子里面关了鸡和兔子（鸡有2只脚，兔子有4只脚，没有例外）。
已经知道了笼子里面脚的总数a，问笼子里面至少有多少只动物，至多有多少只动物。
输入
一行，一个正整数a (a < 32768)。
输出
一行，包含两个正整数，第一个是最少的动物数，第二个是最多的动物数，两个正整数用一个空格分开。
如果没有满足要求的答案，则输出两个0，中间用一个空格分开。
样例
输入： 20 ； 输出： 5 10
"""