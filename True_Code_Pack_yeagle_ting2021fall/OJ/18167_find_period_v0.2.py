# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    s = input()
    L = len(s)
    for i in range(L):
        x = i+1
        if s[0:x]==s[-x:L]:
            ans += [str(x)]
            break
print('\n'.join(ans))

"""info
Created on Mon Nov 15 23:28:53 2021
@author: Asus
http://cs101.openjudge.cn/practice/18167/
18167:寻找周期 v0.2 (data structures, string)
总时间限制: 1000ms 内存限制: 65536kB
描述
找出一个字符串的最小周期。
例如，"abcabcabcabc"，是以3为周期的字符串（注意，它也以6和12为周期）。
现输入一个长度不超过100的字符串，输出其最小周期。
输入
第一行为N,代表输入字符串的个数。
第二行之后每行为一个长度为不超过100的字符串，不包含空格。
输出
每行都是一个整数，代表字符串的最小周期。
样例输入
1
HelloHello
样例输出
5
"""