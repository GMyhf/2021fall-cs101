# -*- coding: utf-8 -*-
ans=[]
sq = [1,4,9,16,25,36,49,64,81,100,101]
for _ in range(int(input())):
    n = int(input())
    for i in range(10):
        if sq[i]<= n <sq[i+1]:
            ans+=[str(i+1)]
print('\n'.join(ans))

# this code surely can be better but I cann't get it

"""info
Created on Mon Nov 15 14:40:02 2021
@author: Asus
http://cs101.openjudge.cn/practice/01218/
01218:THE DRUNK JAILER
总时间限制: 1000ms 内存限制: 65536kB
描述
A certain prison contains a long hall of n cells, each right next to each other. Each cell has a prisoner in it, and each cell is locked.
One night, the jailer gets bored and decides to play a game. For round 1 of the game, he takes a drink of whiskey,and then runs down the hall unlocking each cell. For round 2, he takes a drink of whiskey, and then runs down the
hall locking every other cell (cells 2, 4, 6, ?). For round 3, he takes a drink of whiskey, and then runs down the hall. He visits every third cell (cells 3, 6, 9, ?). If the cell is locked, he unlocks it; if it is unlocked, he locks it. He
repeats this for n rounds, takes a final drink, and passes out.
Some number of prisoners, possibly zero, realizes that their cells are unlocked and the jailer is incapacitated. They immediately escape.
Given the number of cells, determine how many prisoners escape jail.
输入
The first line of input contains a single positive integer. This is the number of lines that follow. Each of the following lines contains a single integer between 5 and 100, inclusive, which is the number of cells n.
输出
For each line, you must print out the number of prisoners that escape when the prison has n cells.
样例输入
2
5
100
样例输出
2
10
"""