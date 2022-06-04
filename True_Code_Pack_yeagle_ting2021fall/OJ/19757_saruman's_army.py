# -*- coding: utf-8 -*-
ans = []
while True:
    R, n = map(int, input().split())
    if R < 0: break
    army = sorted(map(int, input().split()))
    if R:
        i = need = 0
        while i < n:
            left = army[i]
            i += 1
            while i < n and army[i] <= left + R:
                i += 1
            midd = army[i-1]
            while i < n and army[i] <= midd + R:
                i += 1
            need += 1
        ans.append(need)
    else: ans.append(len(set(army)))
print('\n'.join(map(str, ans)))

"""info
Created on Sat Dec 18 11:06:00 2021
@author: Asus
http://cs101.openjudge.cn/practice/19757/
19757:Saruman's Army
总时间限制: 1000ms 内存限制: 65536kB
描述
Saruman the White must lead his army along a straight path from Isengard to Helm’s Deep. To keep track of his forces, Saruman distributes seeing stones, known as palantirs, among the troops. Each palantir has a maximum effective range of R units, and must be carried by some troop in the army (i.e., palantirs are not allowed to “free float” in mid-air). Help Saruman take control of Middle Earth by determining the minimum number of palantirs needed for Saruman to ensure that each of his minions is within R units of some palantir.
输入
The input test file will contain multiple cases. Each test case begins with a single line containing an integer R, the maximum effective range of all palantirs (where 0 ≤ R ≤ 1000), and an integer n, the number of troops in Saruman’s army (where 1 ≤ n ≤ 1000). The next line contains n integers, indicating the positions x1, …, xn of each troop (where 0 ≤ xi ≤ 1000). The end-of-file is marked by a test case with R = n = −1.
输出
For each test case, print a single integer indicating the minimum number of palantirs needed.
样例输入
0 3
10 20 20
10 7
70 30 1 7 15 20 50
-1 -1
样例输出
2
4
提示
In the first test case, Saruman may place a palantir at positions 10 and 20. Here, note that a single palantir with range 0 can cover both of the troops at position 20.
In the second test case, Saruman can place palantirs at position 7 (covering troops at 1, 7, and 15), position 20 (covering positions 20 and 30), position 50, and position 70. Here, note that palantirs must be distributed among troops and are not allowed to “free float.” Thus, Saruman cannot place a palantir at position 60 to cover the troops at positions 50 and 70.
"""