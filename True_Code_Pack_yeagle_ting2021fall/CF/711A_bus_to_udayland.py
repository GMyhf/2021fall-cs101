# -*- coding: utf-8 -*-
bus=[]
seat = False
for _ in range(int(input())):
    row = input()
    if not seat and 'OO' in row:
        seat = True
        row = row.replace('OO', '++', 1)
    bus.append(row)
if seat:
    print('\n'.join(['YES', *bus]))
else:
    print('NO')

"""info
Created on Thu Dec  2 14:05:00 2021
@author: Asus
https://codeforces.com/problemset/problem/711/A
711A-Bus to Udayland
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

ZS the Coder and Chris the Baboon are travelling to Udayland! To get there, they have to get on the special IOI bus. The IOI bus has n rows of seats. There are 4 seats in each row, and the seats are separated into pairs by a walkway. When ZS and Chris came, some places in the bus was already occupied.
ZS and Chris are good friends. They insist to get a pair of neighbouring empty seats. Two seats are considered neighbouring if they are in the same row and in the same pair. Given the configuration of the bus, can you help ZS and Chris determine where they should sit?

Input
The first line of the input contains a single integer n (1 ≤ n ≤ 1000) — the number of rows of seats in the bus.
Then, n lines follow. Each line contains exactly 5 characters, the first two of them denote the first pair of seats in the row, the third character denotes the walkway (it always equals '|') and the last two of them denote the second pair of seats in the row.
Each character, except the walkway, equals to 'O' or to 'X'. 'O' denotes an empty seat, 'X' denotes an occupied seat. See the sample cases for more details.
Output
If it is possible for Chris and ZS to sit at neighbouring empty seats, print "YES" (without quotes) in the first line. In the next n lines print the bus configuration, where the characters in the pair of seats for Chris and ZS is changed with characters '+'. Thus the configuration should differ from the input one by exactly two charaters (they should be equal to 'O' in the input and to '+' in the output).
If there is no pair of seats for Chris and ZS, print "NO" (without quotes) in a single line.
If there are multiple solutions, you may print any of them.
Examples
input
6
OO|OX
XO|XX
OX|OO
XX|OX
OO|OO
OO|XX
output
YES
++|OX
XO|XX
OX|OO
XX|OX
OO|OO
OO|XX

input
4
XO|OX
XO|XX
OX|OX
XX|OX
output
NO

input
5
XX|XX
XX|XX
XO|OX
XO|OO
OX|XO
output
YES
XX|XX
XX|XX
XO|OX
XO|++
OX|XO

Note
Note that the following is an incorrect configuration for the first sample case because the seats must be in the same pair.
O+|+X
XO|XX
OX|OO
XX|OX
OO|OO
OO|XX
"""