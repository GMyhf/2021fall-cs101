# -*- coding: utf-8 -*-
a = int(input())
print(['Y','N'][a%4!=0 or (a%100==0 and a%400!=0)])

'''#v1.0
a = int(input())
if a%100!=0 and a%4==0:
    print("Y")
elif a%100==0 and a%400==0:
    print("Y")
else:
    print("N")
'''
"""info
Created on Tue Sep 21 12:13:48 2021
@author: Asus
http://cs101.openjudge.cn/practice/2733
2733:判断闰年
总时间限制: 1000ms 内存限制: 65536kB
描述
判断某年是否是闰年。
输入
输入只有一行，包含一个整数a(0 < a < 3000)
输出
一行，如果公元a年是闰年输出Y，否则输出N
样例
输入：2006 ；输出： N
提示
公历纪年法中，能被4整除的大多是闰年，但能被100整除而不能被400整除的年份不是闰年， 能被3200整除的也不是闰年，如1900年是平年，2000年是闰年，3200年不是闰年。
"""