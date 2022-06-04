# -*- coding: utf-8 -*-
ans=[]
while True:
    try:
        len_str = []
        for _ in range(int(input())):
            x = input()
            if x=='stop': break
            len_str.append([len(x),x])
        ans.extend(sorted(len_str))
    except EOFError: break
for a in ans: print(a[1])

"""info
Created on Fri Oct 22 23:24:21 2021
@author: Asus
http://cs101.openjudge.cn/practice/02915/
02915:字符串排序
总时间限制: 1000ms 内存限制: 65536kB
描述
先输入你要输入的字符串的个数。然后换行输入该组字符串。每个字符串以回车结束，每个字符串少于一百个字符。如果在输入过程中输入的一个字符串为“stop”，也结束输入。
然后将这输入的该组字符串按每个字符串的长度，由小到大排序，按排序结果输出字符串。
输入
字符串的个数，以及该组字符串。每个字符串以‘\n’结束。如果输入字符串为“stop”，也结束输入.
输出
将输入的所有字符串按长度由小到大排序输出(如果有“stop”，不输出“stop”)。
样例输入
5
sky is grey
cold
very cold
stop
3
it is good enough to be proud of
good
it is quite good
样例输出
cold
very cold
sky is grey
good
it is quite good
it is good enough to be proud of
提示
根据输入的字符串个数来动态分配存储空间（采用new()函数）。每个字符串会少于100个字符。
测试数据有多组，注意使用while()循环输入。
"""