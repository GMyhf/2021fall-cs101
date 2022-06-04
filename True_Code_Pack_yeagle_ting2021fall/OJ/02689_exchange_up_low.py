# -*- coding: utf-8 -*-
sentence = input()
for letter in sentence:
    if str.isupper(letter):
        print(str.lower(letter),end="")
    elif str.islower(letter):
        print(str.upper(letter),end="")
    else: print(letter,end="")

#shorter,faster:
for a in input():
    if a.isupper():
        print(a.lower(),end="")
    elif a.islower():
        print(a.upper(),end="")
    else: print(a,end="")
    
"""info
Created on Sat Sep 25 10:34:29 2021
@author: Asus
http://cs101.openjudge.cn/practice/2689/
2689:大小写字母互换
总时间限制: 1000ms 内存限制: 65536kB
描述
把一个字符串中所有出现的大写字母都替换成小写字母，同时把小写字母替换成大写字母。
输入
输入一行：待互换的字符串。
输出
输出一行：完成互换的字符串（字符串长度小于80）。
样例输入
If so, you already have a Google Account. You can sign in on the right. 
样例输出
iF SO, YOU ALREADY HAVE A gOOGLE aCCOUNT. yOU CAN SIGN IN ON THE RIGHT. 
"""