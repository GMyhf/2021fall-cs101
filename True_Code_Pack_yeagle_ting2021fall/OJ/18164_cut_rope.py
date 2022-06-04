# -*- coding: utf-8 -*-
# Python documentation: https://docs.python.org/zh-cn/3/library/heapq.html
import heapq
N = int(input())
cut = [*map(int, input().split())]
heapq.heapify(cut)
ans = 0
for _ in range(N-1):
    a = heapq.heappop(cut)
    b = heapq.heappop(cut)
    cost = a + b
    heapq.heappush(cut, cost)
    ans += cost
print(ans)

# refer to bisect code of classmate Huang-ZhangYi
import bisect
N, cost = int(input()), 0
part = sorted(map(int, input().split()))
while len(part) != 1:
    link = part.pop(0) + part.pop(0)
    bisect.insort(part, link)
    cost += link
print(cost)

"""info
Created on Tue Dec 14 14:29:48 2021
@author: Asus
http://cs101.openjudge.cn/practice/18164/
18164:剪绳子(greedy,huffman)
总时间限制: 12000ms 内存限制: 65536kB
描述
小张要将一根长度为L的绳子剪成N段。准备剪的绳子的长度为L1,L2,L3...,LN，未剪的绳子长度恰好为剪后所有绳子长度的和。  
每次剪断绳子时，需要的开销是此段绳子的长度。
比如，长度为10的绳子要剪成长度为2,3,5的三段绳子。长度为10的绳子切成5和5的两段绳子时，开销为10。再将5切成长度为2和3的绳子，开销为5。因此总开销为15。
请按照目标要求将绳子剪完最小的开销时多少。
已知，1<=N <= 20000，0<=Li<= 50000
输入
第一行：N，将绳子剪成的段数。
第二行：准备剪成的各段绳子的长度。
输出
最小开销
样例输入
3
2 3 5
样例输出
15
"""