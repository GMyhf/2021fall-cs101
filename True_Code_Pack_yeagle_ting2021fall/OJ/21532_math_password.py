# -*- coding: utf-8 -*-
n = int(input())
for i in range(6, n+1):
    if n%i == 0:
        print(n//i)
        break
    
# original way by xzonn (modified code)
factor = [i for i in range(1, n+1) if not n%i]
for f in factor:
    if f >= 6:
        print(factor[-1]//f)
        break

"""info
Created on Sun Dec  5 17:04:29 2021
@author: Asus
http://cs101.openjudge.cn/practice/21532/
21532:数学密码 (brute force)
总时间限制: 1000ms 内存限制: 65536kB
描述
小明和同学一起去玩密室逃脱，这个密室的老板特别喜欢数学，所以他设置了一个密码门。在搜集了房间里的有价值信息后，小明总结出的信息为：三个互不相同的正整数和为231，那么这三个互不相同正整数的最大公因数就是密码。小明很快的算出了密码。
回到学校后，小明希望写一个程序，对于给定的三个互不相同的正整数的和，快速求出这三个正整数的最大公因数。
描述部分对应英文：
Xiao Ming went to play escape room with his classmates. The owner of this room is especially fond of mathematics, so he set up a password door. After collecting valuable information from the room, Xiao Ming concluded the information as follows: three mutually dissimilar positive integers and 231, then the greatest common factor of these three mutually dissimilar positive integers is the password. Xiao Ming quickly worked out the password.
After returning to school, Xiao Ming wishes to write a program to quickly find the greatest common factor of the three mutually dissimilar positive integers for a given sum of these three positive integers.
输入
输入为三个互不相同的正整数的和 (6 ≤ N ≤ 10**9).
输出
输出三个数的最大公因数.

样例
sample1 in:
231
sample1 out:
33

sample2 in:
1234
sample2 out:
2

sample3 in:
88
sample3 out:
11
"""