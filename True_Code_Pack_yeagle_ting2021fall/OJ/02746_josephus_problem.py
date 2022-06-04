# -*- coding: utf-8 -*-
ans=[]
def josephus(n,m):
    if n==1: return 0
    return (josephus(n-1,m)+m)%n
while 1:
    n,m = map(int,input().split())
    if n==0: break
    ans.append(josephus(n,m)+1)
for a in ans: print(a)

"""info
Created on Mon Nov  1 12:09:15 2021
@author: Asus
http://cs101.openjudge.cn/practice/02746/
02746:约瑟夫问题
总时间限制: 1000ms 内存限制: 65536kB
描述
约瑟夫问题：有ｎ只猴子，按顺时针方向围成一圈选大王（编号从１到ｎ），从第１号开始报数，一直数到ｍ，数到ｍ的猴子退出圈外，剩下的猴子再接着从1开始报数。就这样，直到圈内只剩下一只猴子时，这个猴子就是猴王，编程求输入ｎ，ｍ后，输出最后猴王的编号。
输入
每行是用空格分开的两个整数，第一个是 n, 第二个是 m ( 0 < m,n <=300)。最后一行是：
0 0
输出
对于每行输入数据（最后一行除外)，输出数据也是一行，即最后猴王的编号
样例输入
6 2
12 4
8 3
0 0
样例输出
5
1
7
"""