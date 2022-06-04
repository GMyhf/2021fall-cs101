# -*- coding: utf-8 -*-
n, m = map(int, input().split())
total = 0
shop, sale = {}, {}
for _ in range(n):
    s, p = map(int, input().split())
    try: shop[s].append(p)
    except: shop[s] = [p]
    total += p
total -= 30*(total//200)
for i in range(1, m+1):
    q, x = map(int, input().split('-'))
    sale[i] = (q, x)
for s in shop:
    if sum(shop[s]) >= sale[s][0]:
        total -= sale[s][1]
print(total)

"""info
Created on Tue Dec 28 15:47:48 2021
@author: Asus
http://cs101.openjudge.cn/practice/23566/
23566:决战双十一
总时间限制: 1000ms 内存限制: 65536kB
描述
双十一来临之际，某猫推出了一系列眼花缭乱的活动。Casper希望借此机会，狠狠薅一把羊毛。他在购物车里准备了n个商品，分别来自店铺si，双十一狂欢价为pi。除了跨店的满200减30活动以外，总共m家店铺，每个都有自己的店铺券qj - xj，表示在该店铺中，商品狂欢价金额之和满qj即可减掉xj。
由于最终成交金额只有在支付页面才能看到，而Casper现在就想知道自己最终能薅到多少羊毛，希望你能帮他计算出最终的成交价。
注意每一家店铺只能使用一张店铺券；跨店满减计算的总价是双十一狂欢价的金额总和，每满200减30。
输入
第一行为两个整数n​和m​，分别表示有n​个商品和m​家店铺（1 < n <10000，1 < m < 100）
接下来n行分别是商品i的店铺si与它的双十一狂欢价pi（1 <= si <= m，1<= i<= n）
最后m行中，每一行表示第j家店铺的优惠券，用qj - xj表示，满足qj >= xj（1 <= j <= m）
输出
输出最终的成交价

样例
Sample Input1:
2 2
1 100
2 100
100-20
200-50
Sample Output1:
150

#解释：150：有两件商品，总价为100+100=200，跨店满减能减30，
针对店铺优惠券，能在第一个店铺使用，能减20，总共能减50，
所以最后成交价为150。
There are two goods, and the total price is 100 plus 100, equal to 200.
 Through the cross-store activity, the price can be reduced by 30. 
As for store coupons, we can use one in store 1, since the price is not
 less than 100, so the price can be reduced by 20.
 So the final transaction price is 200-30-20=150.

Sample Input2:
5 3
1 100
1 150
2 30
3 40
3 20
100-10
50-5
100-20
Sample Output2:
300

#解释：300:共5件商品，总价340，跨店满减能减30；只有第一个商店能使
用店铺优惠券，能减10，所以最终成交价为340-30-10=300。
The total price of five goods is 340. Through the cross-store activity, 
the price can be reduced by 30. Since we can only use the store coupon
 in the 1st store, which can reduce 10, the final transaction price is 
340-30-10=300.

提示
tag: implementation
"""