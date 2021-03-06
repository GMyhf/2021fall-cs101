# -*- coding: utf-8 -*-
n, m = map(int, input().split())
rank = sorted(map(int, input().split()))
diff = []
if n==m or n<2:
    print(0)
else:
    for i in range(n-1, 0, -1):
        diff += [rank[i] - rank[i-1]]
    diff.sort(reverse=True)
    print(sum(diff[m-1:]))

"""info
Created on Thu Nov 25 13:36:18 2021
@author: Asus
http://cs101.openjudge.cn/practice/19948/
19948:因材施教(greedy)
总时间限制: 1000ms 内存限制: 65536kB
描述
有一所魔法高校招入一批学生，为了贯彻因材施教的理念，学校打算根据他们的魔法等级进行分班教育。在确定班级数目的情况下，班级内学生的差异要尽可能的小，也就是各个班级内学生的魔法等级要尽可能的接近。
例如：现在有(n = 7)位学生，他们的魔法等级分别为(r = [2, 7, 9, 9, 16, 28, 45])，我们要将他们分配到(m = 3)个班级，如果按照([2, 7], [9, 9], [16, 28, 45])的方式分班，则他们的总体差异为(d = (7 - 2) + (9 - 9) + (45 - 16) = 34)。
输入
第一行为两个整数:学生人数n和班级数目m，1 <= m <= n <= 10^5。
第二行为n个整数：每位学生的魔法等级ri，1 <= ri <= 10^9。
输出
一个整数：学生的最小总体差异d。

样例
Sample1 Input
7 3
2 7 9 9 16 28 45
Sample1 Output
14
解释：最小总体差异的分班方式为([2, 7, 9, 9, 16], [28], [45])

Sample2 Input
15 9
90 73 116 47 400 212 401 244 13 372 248 56 194 482 177
Sample2 Output
65
解释：最小总体差异的分班方式为([13], [47, 56, 73, 90], [116], [177, 194], [212], [244, 248], [372], [400, 401], [482])
"""