# -*- coding: utf-8 -*-
x = int(input())
if x%5==0:
    ans = int(x/5)
else:
    ans = int(x//5 +1)
print(ans)

"""info
Created on Sat Sep 25 11:15:43 2021
@author: Asus
https://codeforces.com/problemset/problem/617/A
617A-Elephant
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.

Input
The first line of the input contains an integer x (1 ≤ x ≤ 1 000 000) — The coordinate of the friend's house.
Output
Print the minimum number of steps that elephant needs to make to get from point 0 to point x.
Examples
    input
        5
    output
        1
    input
        12
    output
        3
Note
In the first sample the elephant needs to make one step of length 5 to reach the point x.
In the second sample the elephant can get to point x if he moves by 3, 5 and 4. There are other ways to get the optimal answer but the elephant cannot reach x in less than three moves.
"""