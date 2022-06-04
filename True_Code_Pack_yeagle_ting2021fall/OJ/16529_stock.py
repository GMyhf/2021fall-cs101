# -*- coding: utf-8 -*-
input() #useless
s = [float(i) for i in input().split()]
mx=s[0] ; mn=s[0] ; pro=1
for i in s[1:]:
    if i>mx: mx=i
    if i<mn: mx=i ; mn=i
    if mx/mn>pro: pro=mx/mn
print('%.2f'%(pro*100))

"""info
Created on Sun Oct 17 15:42:38 2021
@author: Asus
http://cs101.openjudge.cn/practice/16529/
16529:股票 (greedy)
总时间限制: 1000ms 内存限制: 65536kB
描述
假设小明一开始有100块钱，给出每天的股票价格，小明可以在这些天内先后进行一次买操作和一次卖操作，或者什么也不干。
问小明最后最多可以得到多少钱？
注意：1. 一定要先买后卖
      2. 股票最后一定要卖掉
      3. 数据量较大，如果简单枚举（买入价，卖出价）会超时
输入
第一行为天数N(1 <= N <= 100000)
接下来一行有N个数Pi，为每天的股票价格，0 < Pi
输出
最后小明可以得到最多的钱数（小数点后保留两位）。
样例输入
Sample Input1
5
0.1 0.8 20 0.5 0.01
Sample Output1
20000.00
Sample Input2
6
599 600 301 599 300 301
Sample Output2
199.00
样例输出
Sample Input3
5
5 4 3 2 1
Sample Output3
100.00
Sample Input4
5
5 4 3 21 1
Sample Output4
700.00
提示
N天内只能买进一次，卖出一次。并且可以买非整数股。
"""