# -*- coding: utf-8 -*-
n, wx = map(int, input().split())
cp=[]
for _ in range(n):
    v, w = map(int, input().split())
    cp.append([v/w, v, w])
cp.sort(reverse=1) ; ans=0
for x in cp:
    if x[2] <= wx:
        ans += x[1]
        wx -= x[2]
    else:
        ans += wx*x[0]
        break
print('%.1f'%ans)

"""info
Created on Mon Nov  1 10:37:46 2021
@author: Asus
http://cs101.openjudge.cn/practice/04110/
04110:圣诞老人的礼物-Santa Clau’s Gifts
总时间限制: 1000ms 内存限制: 65536kB
描述
圣诞节来临了，在城市A中圣诞老人准备分发糖果，现在有多箱不同的糖果，每箱糖果有自己的价值和重量，每箱糖果都可以拆分成任意散装组合带走。圣诞老人的驯鹿最多只能承受一定重量的糖果，请问圣诞老人最多能带走多大价值的糖果。
输入
第一行由两个部分组成，分别为糖果箱数正整数n(1 <= n <= 100)，驯鹿能承受的最大重量正整数w（0 < w < 10000），两个数用空格隔开。其余n行每行对应一箱糖果，由两部分组成，分别为一箱糖果的价值正整数v和重量正整数w，中间用空格隔开。
输出
输出圣诞老人能带走的糖果的最大总价值，保留1位小数。输出为一行，以换行符结束。
样例输入
4 15
100 4
412 8
266 7
591 2
样例输出
1193.0
"""