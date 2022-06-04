# -*- coding: utf-8 -*-
word_1, word_2 = input(), input()
for i in range(len(word_1), 0, -1):
    x = word_1[i-1:]
    if x == word_2[0:len(x)]:
        print(i-1)
        break

# old code
word_1 = input()
word_2 = input()
for i in range(len(word_1),0,-1):
    x = word_1[i-1:]
    if x==word_2[0:len(x)]:
        print(i-1)
        break
    else: pass

"""info #第一次 OJ 的 Wrong Answer (range倒序)
Created on Tue Sep 28 08:41:28 2021
@author: Asus
http://cs101.openjudge.cn/practice/16527/
16527:字符串连接位置(string)
总时间限制: 1000ms 内存限制: 65536kB
描述
给定两个字符串A和B，如果A的某一后缀恰好和B的某一前缀相同，则定义字符串A可以连接到B。
例如，字符串 xxxxxabc 可以连接到字符串 abc******** ，因为
xxxxxabc
     abc********
输入
输入为两行，分别为字符串A和B。
输入保证A和B是可连接的。
输出
字符串连接的位置，从0开始计数。
如果存在多个可连接位置，则输出值最大的位置。
样例
    Sample Input1:
        xxxxxabc
        abc********
    Sample Output1:
        5
    Sample Input2:
        a
        abcd
    Sample Output2:
        0
"""