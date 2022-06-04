# -*- coding: utf-8 -*-
n, p = map(int, input().split())
cal = 0
if n >= 30:
    cal += 30*12
    n -= 30
else:
    cal += n*12
    n = 0
if n >= 60:
    cal += 60*10
    n -= 60
else:
    cal += n*10
    n = 0
if n >= 90:
    cal += 90*6
    n -= 90
else:
    cal += n*6
    n = 0
if n >= 180:
    cal += 180*4
else:
    cal += n*4
print(cal*p)

"""info
Created on Mon Dec 20 23:34:39 2021
@author: Asus
http://cs101.openjudge.cn/practice/18189/
18189:燃烧我的卡路里
总时间限制: 1000ms 内存限制: 65536kB
描述
西红柿首富决定减脂肪保险计划，投保人每消耗卡路里能拿到一定量的钱，假设每卡平均价格为p元。
每个人能参加4项运动，每项运动消耗卡路里不同，并且每项运动一个人每天最多只能参与一定量的时间。
慢走 240卡/小时，最多3小时      # 240//60 = 4  max 180min last
快跑 720 卡/小时 ，最多0.5小时  # 720//60 = 12 max 30min  first
单车 360 卡/小时，最多1.5小时   # 360//60 = 6  max 90min  third
游泳 600 卡/小时，最多1小时     # 600//60 = 10 mxa 60min  second
已知小王作为投保人之一，但是他每天只能有n分钟的时间用来训练消耗卡路里，请问他应该如何安排自己的时间获得更多的钱。
说明：n超出所有允许的运动量时间后，不再得钱。
输入
为n,p,均为整数。分别代表每天训练的时间（分钟）和每卡能拿到的钱（元）。
输出
小王最多得到的钱（元），为整数。

样例
Sample Input1：
120 2
Sample Output1：
2280
解释：快跑半小时，游泳一小时，单车半小时

Sample Input2：
20 3
Sample Output2:
720
"""