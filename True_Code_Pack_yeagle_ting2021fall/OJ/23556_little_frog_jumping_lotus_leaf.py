# -*- coding: utf-8 -*-
n = int(input())
dp = [1, 1] + [0]*(n-1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])    # same with dp[-1]

"""info
Created on Tue Dec 28 16:44:05 2021
@author: Asus
http://cs101.openjudge.cn/practice/23556/
23556:小青蛙跳荷叶
总时间限制: 1000ms 内存限制: 65536kB
描述
小青蛙生活在池塘里觉得很无聊，于是它在池塘里的荷叶上跳来跳去，假设池塘里的荷叶分布呈一条线，按距离小青蛙所在的岸边的远近从0开始编号，小青蛙每次都从岸边同一个位置往池塘里跳，并且它想跳到对岸，如果它轻轻跳，可以跳到下一个荷叶上，如果它用力跳，可以跳更远跳到下两个荷叶上。小青蛙想知道从岸边开始，跳到最后一个荷叶上有几种跳法，你能帮帮它吗？
输入
输入只有为一行，是一个整数n，代表池塘里有多少荷叶。1 <= n <= 1000
输出
输出一个整数，代表从岸边跳到最后一个荷叶上的跳法数目。
样例
Sample Input1:
3
Sample Output1:
3
解释：跳到编号为2的荷叶有三种跳法，也就是从岸边先跳步长为1的一步，再跳步长为2的一步，或者先跳步长为1的一步再跳步长为2的一步，或者跳3次步长为1的。
Explanation: There are three jumping methods to jump to the lotus leaf numbered 2. 
That is, from the shore, jump a step with length of 1, then a step with length of 2, 
or a step with length 2 first and then a step with length 1, or 3 times with a step of length1.

Sample Input2:
4
Sample Output2:
5 
解释：跳到编号为3的跳法有：
（1）步长1 ->步长1 -> 步长1 -> 步长1
（2）步长1 ->步长1 -> 步长2
（3）步长1 ->步长2 -> 步长1
（4）步长2 -> 步长1 -> 步长1
（5）步长2 -> 步长2

提示
tags: dp
备注：建议用python完成，因为其他语言会有数据溢出的问题。
提示：1）通过观察你是否发现了什么规律吗？你如何进一步把这个问题抽象成动态规划的子问题呢？2）睡了一觉/出门吹吹风/刷牙/跑步 之后，突然感觉好像与 斐波那契数列 有关系。
"""