# -*- coding: utf-8 -*-
ans = []
for _ in range(int(input())):
    n, a, b, c, d = map(int, input().split())
    mini, maxi = n*(a-b), n*(a+b)
    low, upp = c-d, c+d
    flag = 0
    for p in (low, upp):
        if mini <= p <= maxi and not flag:
            flag = 1
    for m in (mini, maxi):
        if low <= m <= upp and not flag:
            flag = 1
    ans.append(['No','Yes'][flag])
print('\n'.join(ans))

# should have a easier way...

"""info
Created on Wed Dec 22 15:55:35 2021
@author: Asus
https://codeforces.com/problemset/problem/1341/A
1341A-Nastya and Rice
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Nastya just made a huge mistake and dropped a whole package of rice on the floor. Mom will come soon. If she sees this, then Nastya will be punished.
In total, Nastya dropped n grains. Nastya read that each grain weighs some integer number of grams from a−b to a+b, inclusive (numbers a and b are known), and the whole package of n grains weighs from c−d to c+d grams, inclusive (numbers c and d are known). The weight of the package is the sum of the weights of all n grains in it.
Help Nastya understand if this information can be correct. In other words, check whether each grain can have such a mass that the i-th grain weighs some integer number xi (a−b≤xi≤a+b), and in total they weigh from c−d to c+d, inclusive (c−d≤∑i=1nxi≤c+d).

Input
The input consists of multiple test cases. The first line contains a single integer t (1≤t≤1000)  — the number of test cases.
The next t lines contain descriptions of the test cases, each line contains 5 integers: n (1≤n≤1000)  — the number of grains that Nastya counted and a,b,c,d (0≤b<a≤1000,0≤d<c≤1000)  — numbers that determine the possible weight of one grain of rice (from a−b to a+b) and the possible total weight of the package (from c−d to c+d).
Output
For each test case given in the input print "Yes", if the information about the weights is not inconsistent, and print "No" if n grains with masses from a−b to a+b cannot make a package with a total mass from c−d to c+d.
Example
input
5
7 20 3 101 18
11 11 10 234 2
8 9 7 250 122
19 41 21 321 10
3 10 8 6 1
output
Yes
No
Yes
No
Yes
Note
In the first test case of the example, we can assume that each grain weighs 17 grams, and a pack 119 grams, then really Nastya could collect the whole pack.
In the third test case of the example, we can assume that each grain weighs 16 grams, and a pack 128 grams, then really Nastya could collect the whole pack.
In the fifth test case of the example, we can be assumed that 3 grains of rice weigh 2, 2, and 3 grams, and a pack is 7 grams, then really Nastya could collect the whole pack.
In the second and fourth test cases of the example, we can prove that it is impossible to determine the correct weight of all grains of rice and the weight of the pack so that the weight of the pack is equal to the total weight of all collected grains.
"""