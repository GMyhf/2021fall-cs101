# -*- coding: utf-8 -*-
# refer to code of classmate Ding-YiChen
def conv(date:str):
    m, d = map(int, date.split('.'))
    if m == 1: return d-7
    else: return 24+d
plan = []
for _ in range(int(input())):
    start, end, love = input().split()
    s, e = conv(start), conv(end)
    if e > 44: continue
    plan.append([s, e, int(love)])
plan.sort(key = lambda x:x[1])
dp = [0]*46
for p in plan:
    s, e, love = p
    dp[e+1] = max(dp[e+1], max(dp[:s+1])+love)
print(max(dp))

"""info
Created on Tue Dec 28 19:11:51 2021
@author: Asus
http://cs101.openjudge.cn/practice/23568/
23568:幸福的寒假生活
总时间限制: 1000ms 内存限制: 65536kB
描述
p大计划延长2021-2022学年度的寒假——从1月7日到2月20日共45天。Casper和Emily得知这个消息后非常激动，迫不及待地开始规划起寒假日程，希望能从中获得满满的幸福。
现在，可供Casper选择的有n​​​​​​​​​个浪漫计划，包括开始日期和结束日期，以及通过参加这个计划能得到的幸福值，请计算Casper在这个假期能够获得的最大幸福值。
注意所有参加的计划不能有任何时间上的重叠，在第x​天结束的计划和在第x​​天开始的计划不可同时选择；此外，由于Emily必须在2月21日返校，所以不能参加在2月20日之后结束的计划。
输入
第一行包含一个整数n​，表示有n​个浪漫计划（n<200​）​
紧接着的n​​​行，每一行由3个部分组成，首先是第 i ​​​个计划开始的日期 si，然后是结束日期 ei，最后是Casper和Emily在这个计划中能获得的幸福值 vi​​​​​​，以空格分隔。输入保证每个计划的时长都在1天至10天的范围内，且计划的开始日期都在寒假范围内。
输出
输出他们所能获得的最大幸福值

样例
Sample Input1:
3
1.8 1.27 100
1.23 1.27 20
2.4 2.8 81
Sample Output1:
181

Sample Input2:
5
1.8 1.27 100
1.10 1.19 90
1.23 1.27 20
2.4 2.8 81
2.10 2.23 100
Sample Output2:
191

提示
tag: dp
先把日期映射到[0,44]​​​的区间上，然后利用动态规划算法求解，子问题可以考虑为：前i个计划下所能得到的最大幸福值
"""