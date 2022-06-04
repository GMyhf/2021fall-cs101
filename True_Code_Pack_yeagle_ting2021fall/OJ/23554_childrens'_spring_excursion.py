# -*- coding: utf-8 -*-
# using sort
n = int(input())
kids = sorted(map(int, input().split()))
lost = [i for i in range(1, n+1) if i not in kids]
more = [j for j in kids if j > n+1]
print(*lost)
print(*more)

# without sort, brute force
n = int(input())
*kids, = map(int, input().split())
lost, more = [], []
for i in range(1, n+1):
    if i not in kids:
        lost.append(i)
for j in range(n+2, 10001):
    if j in kids:
        k = kids.count(j)
        more.extend([j]*k)
print(*lost)
print(*more)

"""info
Created on Tue Dec 28 14:53:06 2021
@author: Asus
http://cs101.openjudge.cn/practice/23554/
23554:小朋友春游
总时间限制: 1000ms 内存限制: 65536kB
描述
假设你是一位老师，带着一个班级的小朋友去春游，每个小朋友身上都有一个从1开始的编号，到达公园后，你清点人数的时候发现有几位小朋友不见了，并且混入了几个其他班级的小朋友，你很着急，因为小朋友们并没有按照序号排好队，而你想要尽快知道走丢的小朋友们的编号，还想知道哪些小朋友是别的班级走散到你们班级队伍的。那么如果本班级原本小朋友的总数是n，剩余的x个小朋友的编号为一个数组，你要如何尽快知道走丢的小朋友的编号，并且找出其他班级走散的小朋友呢？
注意：
1）为了简化问题，我们假定其他班小朋友的编号一定是大于n的，并且小于等于10000，而本班小朋友编号一定小于等于n。
2）其他班的小朋友编号是有可能重复的，因为可能a班有个10号b班也有一个10号。
3）题目数据保证走丢的小朋友和其他班乱入的小朋友都最少有一个。
输入
输入为两行。
第一行是一个整数n，代表原本共有n个小朋友。1 <= n <= 200
第二行是一串用空格分隔的整数，代表剩下的小朋友的编号，注意我们不知道剩下的小朋友有多少个，观测到的编号也不是有序的。
输出
输出为两行。
第一行是一串空格分隔的整数，代表本班级走丢的小朋友的编号，按升序排列。
第二行是一串空格分隔的整数，代表其他班级乱入本班队伍的小朋友们的编号，按升序排列。

样例
Sample Input1:
10
2 6 1 8 4 10 33 1000
Sample Output1:
3 5 7 9
33 1000

Sample Input2:
13
7 8 2 3 1 5 6 13 400 2000
Sample Output2:
4 9 10 11 12
400 2000

提示
tags: implementation,sort
在时间充裕的时候，例如考试后，可以思考：
能不使用排序完成吗？如何尽可能少的使用额外空间？
"""