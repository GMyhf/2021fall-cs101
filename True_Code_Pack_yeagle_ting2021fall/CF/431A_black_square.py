# -*- coding: utf-8 -*-
c = [int(x) for x in input().split()]
ans = 0
for i in input(): ans+=c[int(i)-1]
print(ans)

"""info
Created on Fri Nov  5 08:06:23 2021
@author: Asus
https://codeforces.com/problemset/problem/431/A
431A-Black Square
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Quite recently, a very smart student named Jury decided that lectures are boring, so he downloaded a game called "Black Square" on his super cool touchscreen phone.
In this game, the phone's screen is divided into four vertical strips. Each second, a black square appears on some of the strips. According to the rules of the game, Jury must use this second to touch the corresponding strip to make the square go away. As Jury is both smart and lazy, he counted that he wastes exactly ai calories on touching the i-th strip.
You've got a string s, describing the process of the game and numbers a1, a2, a3, a4. Calculate how many calories Jury needs to destroy all the squares?

Input
The first line contains four space-separated integers a1, a2, a3, a4 (0 ≤ a1, a2, a3, a4 ≤ 10**4).
The second line contains string s (1 ≤ |s| ≤ 10**5), where the і-th character of the string equals "1", if on the i-th second of the game the square appears on the first strip, "2", if it appears on the second strip, "3", if it appears on the third strip, "4", if it appears on the fourth strip.
Output
Print a single integer — the total number of calories that Jury wastes.
Examples
input
1 2 3 4
123214
output
13
input
1 5 3 2
11221
output
13
"""