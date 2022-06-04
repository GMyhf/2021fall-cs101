# -*- coding: utf-8 -*-
#do_it_like_human_code
n=int(input()) ; ans=[]
while n!=0:
    ans.insert(0,str(n%8)) ; n//=8
print(''.join(ans))

#simple_code
print(oct(int(input()))[2:])

"""info
Created on Mon Oct 18 10:59:20 2021
@author: Asus
http://cs101.openjudge.cn/practice/02734/
02734:十进制到八进制
总时间限制: 1000ms 内存限制: 65536kB
描述
把一个十进制正整数转化成八进制。
输入
一行，仅含一个十进制表示的整数a(0 < a < 65536)。
输出
一行，a的八进制表示。
样例输入
9
样例输出
11
"""