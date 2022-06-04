# -*- coding: utf-8 -*-
#do_it_like_human_code
n=input() ; l=len(n)-1 ; ans=0 ; x=-1
for i in range(l,-1,-1):
    x+=1 ; ans += int(n[i])*(8**x)
print(ans)

#simple_code
print(int(input(),8))

"""info
Created on Mon Oct 18 10:39:58 2021
@author: Asus
http://cs101.openjudge.cn/practice/02735/
02735:八进制到十进制
总时间限制: 1000ms 内存限制: 65536kB
描述
把一个八进制正整数转化成十进制。
输入
一行，仅含一个八进制表示的正整数a，a的十进制表示的范围是(0, 65536)。
输出
一行，a的十进制表示。
样例输入
11
样例输出
9
"""