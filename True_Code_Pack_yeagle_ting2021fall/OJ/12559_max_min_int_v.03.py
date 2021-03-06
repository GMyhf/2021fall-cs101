# -*- coding: utf-8 -*-
n = int(input()) ; num = input().split()
for i in range(n-1):
    for j in range(i+1,n):
        if num[i]+num[j] < num[j]+num[i]:
            num[i],num[j] = num[j],num[i]
print(''.join(num),''.join(reversed(num)))

"""info
Created on Sun Oct 17 16:06:06 2021
@author: Asus
http://cs101.openjudge.cn/practice/12559/
12559:最大最小整数 v0.3(string,sorting)
总时间限制: 1000ms 内存限制: 65536kB
描述
假设有n个正整数，将它们连成一片，将会组成一个新的大整数。现需要求出，能组成的最大最小整数。
比如，有4个正整数，23，9，182，79，连成的最大整数是97923182，最小的整数是18223799。
输入
第一行包含一个整数n，1<=n<=1000。
第二行包含n个正整数，相邻正整数间以空格隔开。
输出
输出为一行，为这n个正整数能组成的最大的多位整数和最小的多位整数，中间用空格隔开。
样例输入
Sample1 in:
4
23 9 182 79
Sample1 out:
97923182 18223799
样例输出
Sample2 in:
2
11 113
Sample2 out:
11311 11113
提示
2020fall-cs101，汪元正。
发现：位数补齐再排序，写法是错误的。原因是：1）这里的序关系 a > b，其实是要求充分长的aaaaaaa比充分长的bbbbbbb大，但是我们是不知道“充分长”到底需要多长。2）若只截取所有数中的最大位数位，则可能出现两个数 a > b，但在这种比较下，由于位数不够多，结果a = b 导致sort中 a 排在了 b 前面。3）898,89889就是这种情况。补齐：89889 = 898889，实际 8988988 < 898898. 输出两个数：89889889,89889898,错误。
"""