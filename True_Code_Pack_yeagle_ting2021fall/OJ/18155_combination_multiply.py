# -*- coding: utf-8 -*-
# refer to code of WenGang 2018-fallcs101, brute force with special import
from functools import reduce
from itertools import combinations
t = int(input())
s = [*map(int, input().split())]
multiply = []
for i in range(1, len(s) +1):
    for j in combinations(s, i):
        multiply.append(reduce(lambda x, y : x*y, j))
if t in multiply:
    print('YES')
else:
    print('NO')

"""info
Created on Sat Dec  4 23:34:56 2021
@author: Asus
http://cs101.openjudge.cn/practice/18155/
18155:组合乘积(combination)
总时间限制: 1000ms 内存限制: 65536kB
描述
给定整数集合S和一个目标数T，判断是否可以从S中挑选一个非空子集，子集中的数相乘的乘积为T。
输入
输入为两行。
第一行为目标数T。
第二行为S中的N个元素，以空格隔开。
其中 N <= 16。
输出
如果可以，则输出YES，否则输出NO。
样例输入
Sample Input 1:
12
1 2 3 4 5
Sample Output 1:
YES
样例输出
Sample Input 2:
33
4 2 8 7 5
Sample Output 2:
NO
"""