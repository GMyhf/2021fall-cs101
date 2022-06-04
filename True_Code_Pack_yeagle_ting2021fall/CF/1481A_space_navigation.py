# -*- coding: utf-8 -*-
ans = []
for _ in range(int(input())):
    x, y = map(int, input().split())
    d = {'U':0, 'D':0, 'R':0, 'L':0}
    s = input()
    for i in s: d[i] += 1
    dx = -d['L'] <= x <= d['R']
    dy = -d['D'] <= y <= d['U']
    ans.append(['NO', 'YES'][dx and dy])
print('\n'.join(ans))

"""info
Created on Wed Dec 15 19:59:25 2021
@author: Asus
https://codeforces.com/problemset/problem/1481/A
1481A-Space Navigation
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

You were dreaming that you are traveling to a planet named Planetforces on your personal spaceship. Unfortunately, its piloting system was corrupted and now you need to fix it in order to reach Planetforces.
Space can be represented as the XY plane. You are starting at point (0,0), and Planetforces is located in point (px,py).
The piloting system of your spaceship follows its list of orders which can be represented as a string s. The system reads s from left to right. Suppose you are at point (x,y) and current order is si:
if si=U, you move to (x,y+1);
if si=D, you move to (x,y−1);
if si=R, you move to (x+1,y);
if si=L, you move to (x−1,y).
Since string s could be corrupted, there is a possibility that you won't reach Planetforces in the end. Fortunately, you can delete some orders from s but you can't change their positions.
Can you delete several orders (possibly, zero) from s in such a way, that you'll reach Planetforces after the system processes all orders?

Input
The first line contains a single integer t (1≤t≤1000) — the number of test cases.
Each test case consists of two lines. The first line in each test case contains two integers px and py (−105≤px,py≤105; (px,py)≠(0,0)) — the coordinates of Planetforces (px,py).
The second line contains the string s (1≤|s|≤10**5: |s| is the length of string s) — the list of orders.
It is guaranteed that the sum of |s| over all test cases does not exceed 10**5.
Output
For each test case, print "YES" if you can delete several orders (possibly, zero) from s in such a way, that you'll reach Planetforces. Otherwise, print "NO". You can print each letter in any case (upper or lower).
Example
input
6
10 5
RRRRRRRRRRUUUUU
1 1
UDDDRLLL
-3 -5
LDLDLDDDR
1 2
LLLLUU
3 -2
RDULRLLDR
-1 6
RUDURUUUUR
output
YES
YES
YES
NO
YES
NO
Note
In the first case, you don't need to modify s, since the given s will bring you to Planetforces.
In the second case, you can delete orders s2, s3, s4, s6, s7 and s8, so s becomes equal to "UR".
In the third test case, you have to delete order s9, otherwise, you won't finish in the position of Planetforces.
"""