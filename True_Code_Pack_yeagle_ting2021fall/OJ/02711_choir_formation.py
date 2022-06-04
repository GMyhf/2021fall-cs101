# -*- coding: utf-8 -*-
n = int(input())
stud = [*map(int,input().split())]
dp_up = [1]*n
for i in range(n):
    for j in range(i):
        if stud[j] < stud[i]:
            dp_up[i] = max(dp_up[i], dp_up[j]+1)
stud.reverse()
dp_down = [1]*n
for i in range(n):
    for j in range(i):
        if stud[j] < stud[i]:
            dp_down[i] = max(dp_down[i], dp_down[j]+1)
dp_down.reverse()
dp = [dp_up[x] + dp_down[x]-1 for x in range(n)]
print(n-max(dp))

# application of 02757:longest_ordered_subsequence
# refer to 02995:climb_mountain

"""info
Created on Sun Dec 12 10:33:22 2021
@author: Asus
http://cs101.openjudge.cn/practice/02711/
02711:合唱队形
总时间限制: 1000ms 内存限制: 65536kB
描述
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学不交换位置就能排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1, 2, …, K，他们的身高分别为T1, T2, …, TK，则他们的身高满足T1 < T2 < … < Ti , Ti > Ti+1 > … > TK (1 <= i <= K)。
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
输入
输入的第一行是一个整数N（2 <= N <= 100），表示同学的总数。第一行有n个整数，用空格分隔，第i个整数Ti（130 <= Ti <= 230）是第i位同学的身高（厘米）。
输出
输出包括一行，这一行只包含一个整数，就是最少需要几位同学出列。
样例输入
8
186 186 150 200 160 130 197 220
样例输出
4
"""