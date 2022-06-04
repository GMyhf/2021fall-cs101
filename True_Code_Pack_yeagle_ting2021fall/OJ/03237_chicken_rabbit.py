# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    a = int(input())
    if a%4==0:
        x=a/4 ; y=a/2
    elif a%2==0:
        x=(a+2)/4 ; y=a/2
    else: x=0 ; y=0
    x = str(int(x))
    y = str(int(y))
    ans.append(x+' '+y)
print('\n'.join(ans))

"""info
Created on Mon Nov  1 09:29:55 2021
@author: Asus
http://cs101.openjudge.cn/practice/03237/
03237:鸡兔同笼
总时间限制: 1000ms 内存限制: 65536kB
描述
一个笼子里面关了鸡和兔子（鸡有2只脚，兔子有4只脚，没有例外）。已经知道了笼子里面脚的总数a，问笼子里面至少有多少只动物，至多有多少只动物
输入
第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，每行一个正整数a (a < 32768)
输出
输出包含n行，每行对应一个输入,包含两个正整数，第一个是最少的动物数，第二个是最多的动物数，两个正整数用一个空格分开
如果没有满足要求的答案，则输出两个0。
样例输入
2
3
20
样例输出
0 0
5 10
"""