# -*- coding: utf-8 -*-
trn = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,
       'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,
       'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,
       'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,
       'seventy':70,'eighty':80,'ninety':90,'thousand':1000,'million':1000000}
raw = input().split()
neg = raw[0]=='negative'
if neg: del raw[0]
x = y = 0
for i in raw:
    if i in {'million', 'thousand'}:
        x += y*trn[i]
        y = 0
    elif i == 'hundred':
        y *= 100
    else:
        y += trn[i]
ans = x + y
print([ans,-ans][neg])

"""info
Created on Tue Oct  5 09:07:52 2021
@author: Asus
http://cs101.openjudge.cn/practice/12757/
12757:阿尔法星人翻译官
总时间限制: 1000ms 内存限制: 65536kB
描述
阿尔法星人为了了解地球人，需要将地球上所有的语言转换为他们自己的语言，其中一个小模块是要将地球上英文表达的数字转换为阿尔法星人也理解的阿拉伯数字。 请你为外星人设计这个模块，即给定一个用英文表示的整数，将其转换成用阿拉伯数字表示的整数。这些数的范围从－999,999,999到＋999,999,999。 下列单词是你的程序中将遇到的所有有关数目的英文单词：
negative, zero, one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, hundred, thousand, million
输入
输入一行，由几个表示数目的英文单词组成(长度不超多200)。注意：负号将由单词negative表示。
当数的大小超过千时，并不用完全单词hundred表示。例如1600将被写为"one thousand six hundred", 而不是"sixteen hundred"。
输出
输出一行，表示答案。
样例输入
negative seven hundred twenty nine
样例输出
-729
提示
其他参考样例：
six ： 6
one million one hundred one： 1000101
eight hundred fourteen thousand twenty two： 814022
"""