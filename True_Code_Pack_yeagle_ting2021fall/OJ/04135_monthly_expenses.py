# -*- coding: utf-8 -*-
# https://blog.csdn.net/qq_51767234/article/details/118034450
# translated from C++ code, specialised binary search
N, M = map(int, input().split())
days = [0]*N
max_exp = sum_exp = 0
for d in range(N):
    exp = int(input())
    days[d] = exp
    max_exp = max(max_exp, exp)
    sum_exp += exp
low = max_exp
upp = sum_exp
mid = low + (upp-low)//2
while low != upp:
    fajo = 1
    sum_tmp = 0
    for i in range(N):
        sum_tmp += days[i]
        if sum_tmp > mid:
            fajo += 1
            sum_tmp = days[i]
        elif sum_tmp == mid:
            fajo += 1
            sum_tmp = 0
    if fajo <= M:
        upp = mid-1
    else:
        low = mid+1
    mid = low + (upp-low)//2
print(mid)

# code from GMyhf
n,m = map(int, input().split())
expenditure = []
for _ in range(n):
    expenditure.append(int(input()))

lower = max(expenditure)
upper = sum(expenditure)

def check(x):
    num, s = 1, 0
    for i in range(n):
        if s + expenditure[i] > x:
            s = expenditure[i]
            num += 1
        else:
            s += expenditure[i]
    return [False, True][num > m]

while lower < upper:
    mid = (lower + upper) // 2
    if check(mid):
        lower = mid + 1
    else:
        upper = mid
        
print(lower)

"""info
Created on Tue Dec  7 14:58:54 2021
@author: Asus
http://cs101.openjudge.cn/practice/04135/
04135:月度开销
总时间限制: 1000ms 内存限制: 65536kB
描述
农夫约翰是一个精明的会计师。他意识到自己可能没有足够的钱来维持农场的运转了。他计算出并记录下了接下来 N (1 ≤ N ≤ 100,000) 天里每天需要的开销。
约翰打算为连续的M (1 ≤ M ≤ N) 个财政周期创建预算案，他把一个财政周期命名为fajo月。每个fajo月包含一天或连续的多天，每天被恰好包含在一个fajo月里。
约翰的目标是合理安排每个fajo月包含的天数，使得开销最多的fajo月的开销尽可能少。
输入
第一行包含两个整数N,M，用单个空格隔开。
接下来N行，每行包含一个1到10000之间的整数，按顺序给出接下来N天里每天的开销。
输出
一个整数，即最大月度开销的最小值。
样例输入
7 5
100
400
300
100
500
101
400
样例输出
500
提示
若约翰将前两天作为一个月，第三、四两天作为一个月，最后三天每天作为一个月，则最大月度开销为500。其他任何分配方案都会比这个值更大。
"""