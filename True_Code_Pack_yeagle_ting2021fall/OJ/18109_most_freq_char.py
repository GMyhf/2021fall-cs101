# -*- coding: utf-8 -*-
X = input().lower()
dic = {}
for i in X:
    dic[i]=X.count(i)
val = max(dic.values())
for k in dic:
    if dic[k]==val:
        key=k ; break
print(key, val)

"""info
Created on Fri Oct  1 09:40:24 2021
@author: Asus
http://cs101.openjudge.cn/practice/18109/
18109:最频繁字符(dictionary)
总时间限制: 1000ms 内存限制: 65536kB
描述
在一个字符串中找出出现次数最多的字母，不区分大小写，并输出他出现的次数。
输入
一个字符串，长度大于0，且不超过1000，全部由大写或小写字母组成。
输出
输出为出现次数最多的小写字母(如果出现次数相同，输出第一个)和出现的次数，中间用一个空格隔开,末尾没有空格。
样例输入
aAABBbBCCCaaaaa
样例输出
a 8
"""