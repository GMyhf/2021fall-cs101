# -*- coding: utf-8 -*-
ans=[]
while True:
    try:
        n, k = map(int, input().split())
        if n == k or k == 0:
            a = 1
        elif n-k == 1 or k == 1:
            a = n%2
        else:
            a = 0
        ans.append(a)
    except EOFError: break
print('\n'.join(map(str, ans)))

"""info
Created on Fri Dec 10 22:56:31 2021
@author: Asus
http://cs101.openjudge.cn/practice/02986/
02986:二项式系数
总时间限制: 5000ms 内存限制: 131072kB
描述
二项式系数C(n, k)因它在组合数学中的重要性而被广泛地研究。二项式系数可以如下递归的定义：
C(1, 0) = C(1, 1) = 1；
C(n, 0) = 1对于所有n > 0；
C(n, k) = C(n − 1, k − 1) + C(n − 1, k)对于所有0 < k ≤ n。
给出n和k，你要确定C(n, k)的奇偶性。
输入
输入包含多组测试数据。每组测试数据一对整数n和k(0 ≤ k ≤ n < 2**31)，占据独立一行。
文件结束符（EOF）表示输入结束。
输出
对每组测试数据，输出一行，包含一个“0” 或一个“1”，即C(n, k)除以2的余数。
样例输入
1 1
1 0
2 1
样例输出
1
1
0
"""