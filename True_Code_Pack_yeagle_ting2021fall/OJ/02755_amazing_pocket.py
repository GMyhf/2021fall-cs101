# -*- coding: utf-8 -*-
# refer to https://blog.csdn.net/qq_38969094/article/details/104349992
memo = [0]*21
def solve(v, k):
    if v == 0: return 1
    if k == 0: return 0
    return solve(v-memo[k], k-1) + solve(v, k-1)
n = int(input())
for i in range(1, n+1):
    memo[i] = int(input())
print(solve(40, n))

"""info
Created on Mon Dec 20 23:17:48 2021
@author: Asus
http://cs101.openjudge.cn/practice/02755/
02755:神奇的口袋
总时间限制: 10000ms 内存限制: 65536kB
描述
有一个神奇的口袋，总的容积是40，用这个口袋可以变出一些物品，这些物品的总体积必须是40。John现在有n个想要得到的物品，每个物品的体积分别是a1，a2……an。John可以从这些物品中选择一些，如果选出的物体的总体积是40，那么利用这个神奇的口袋，John就可以得到这些物品。现在的问题是，John有多少种不同的选择物品的方式。
输入
输入的第一行是正整数n (1 <= n <= 20)，表示不同的物品的数目。接下来的n行，每行有一个1到40之间的正整数，分别给出a1，a2……an的值。
输出
输出不同的选择物品的方式的数目。
样例输入
3
20
20
20
样例输出
3
"""