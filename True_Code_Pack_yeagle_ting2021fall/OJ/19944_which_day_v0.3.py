# -*- coding: utf-8 -*-
day=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
ans=[]
for i in range(int(input())):
    dt=input()
    c=int(dt[0:2]) ; y=int(dt[2:4]) ; m=int(dt[4:6]) ; d=int(dt[6:8])
    if m<3 and y==0: m+=12 ; y=99 ; c-=1
    if m<3: m+=12 ; y-=1
    w = (y + y//4 + c//4 - 2*c + (26*(m+1))//10 + d -1)%7
    ans.append(day[w])
for a in ans: print(a)

"""info # mock 211014
Created on Thu Oct 14 15:13:44 2021
@author: Asus
http://cs101.openjudge.cn/practice/19944/
19944:这一天星期几v0.3(math)
总时间限制: 1000ms 内存限制: 65536kB
描述
在日常生活中，计算某一个具体的日期是星期几，往往需要去翻阅日历。请你帮助更快地计算出每个日期在一星期是第几天。
参考：
蔡勒公式（Zeller's congruence），是一种计算任何一日属一星期中哪一日的算法，由德国数学家克里斯提安·蔡勒推算出来，可以计算1582年10月15日之后的情况。
公式都是基于公历的置闰规则来考虑。
公式中的符号含义如下：
w：星期（计算所得的数值对应的星期：0-Sunday；1-Monday；2-Tuesday；3-Wednesday；4-Thursday；5-Friday；6-Saturday
c：年份前两位数
y：年份后两位数
m：月（m的取值范围为3至14，即在蔡勒公式中，某年的1、2月要看作上一年的13、14月来计算，比如2003年1月1日要看作2002年的13月1日来计算）
d：日
[ ]：称作高斯符号，代表向下取整，即，取不大于原数的最大整数。
mod：同余（这里代表括号里的答案除以7后的余数）
输入
第一行1个整数n，代表输入日期的个数。
接下来n行分别为n个以8位数字表示的日期，如20190101
保证所有输入都在蔡勒公式的计算范围之内。
输出
共n行，每行为该日期对应的weekday名称（Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday）。
样例输入
15
19850706
19710710
20041125
20141220
19841128
19760429
19931102
19951002
20161006
20151226
19790715
20080410
20091104
19910621
19891012
样例输出
Saturday
Saturday
Thursday
Saturday
Wednesday
Thursday
Tuesday
Monday
Thursday
Saturday
Sunday
Thursday
Wednesday
Friday
Thursday
"""