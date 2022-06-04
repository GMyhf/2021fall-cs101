# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    L, n = map(int,input().split())
    ant = [*map(int, input().split())]
    min_time = int(max([L/2 - abs(x-L/2) for x in ant]))
    max_time = max(L-min(ant), max(ant))
    ans.append([min_time, max_time])
for a in ans: print(*a)

"""info
Created on Mon Nov  1 13:08:06 2021
@author: Asus
http://cs101.openjudge.cn/practice/01852/
01852:Ants
总时间限制: 1000ms 内存限制: 65536kB
描述
An army of ants walk on a horizontal pole of length l cm, each with a constant speed of 1 cm/s. When a walking ant reaches an end of the pole, it immediatelly falls off it. When two ants meet they turn back and start walking in opposite directions. We know the original positions of ants on the pole, unfortunately, we do not know the directions in which the ants are walking. Your task is to compute the earliest and the latest possible times needed for all ants to fall off the pole.
输入
The first line of input contains one integer giving the number of cases that follow. The data for each case start with two integer numbers: the length of the pole (in cm) and n, the number of ants residing on the pole. These two numbers are followed by n integers giving the position of each ant on the pole as the distance measured from the left end of the pole, in no particular order. All input integers are not bigger than 1000000 and they are separated by whitespace.
输出
For each case of input, output two numbers separated by a single space. The first number is the earliest possible time when all ants fall off the pole (if the directions of their walks are chosen appropriately) and the second number is the latest possible such time.
样例输入
2
10 3
2 6 7
214 7
11 12 7 13 176 23 191
样例输出
4 8
38 207
"""