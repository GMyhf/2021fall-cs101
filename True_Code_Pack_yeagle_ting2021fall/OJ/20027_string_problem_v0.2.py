# -*- coding: utf-8 -*-
conv = [ord(a)-96 for a in input()]
conv.reverse()
for n in range(len(conv)):
    conv[n] *= 26**n
num = sum(conv) + int(input())+1 ; idd=[]
while num!=0:
    tmp=num%26 ; num//=26
    if not tmp:
        idd.insert(0,26)
        num-=1 ; continue
    idd.insert(0,tmp)
print(''.join([chr(i+96) for i in idd]))

"""info
Created on Sun Oct 17 17:03:46 2021
@author: Asus
http://cs101.openjudge.cn/practice/20027/
20027:字符串问题v0.2
总时间限制: 1000ms 内存限制: 65536kB
描述
已知一个全是小写字母的字符串a，现在想寻找一个于a长度相等的字符串b，使得若按字典排列，全是小写字母且长度与a相同的字符串恰好有k个排在a之后、b之前。
输入
两行，第一行为字符串a，第二行为正整数k，数据保证此题有解
输出
要求的字符串b
样例输入
Sample1 Input:
a
1
Sample1 Output:
c
样例输出
Sample2 Input:
aaz
10
Sample2 Output:
abk
"""