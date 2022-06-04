# -*- coding: utf-8 -*-
code = [*input(), 'end']
ans = ''
while len(code) > 1:
    x = code[0]
    y = code[1]
    if x == '-':
        if y == '.':
            ans += '1'
            del code[:2]
        elif y == '-':
            ans += '2'
            del code[:2]
    elif x == '.':
        ans += '0'
        del code[0]
print(ans)

"""info
Created on Fri Dec 10 22:02:05 2021
@author: Asus
https://codeforces.com/problemset/problem/32/B
32B-Borze
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.

Input
The first line contains a number in Borze code. The length of the string is between 1 and 200 characters. It's guaranteed that the given string is a valid Borze code of some ternary number (this number can have leading zeroes).
Output
Output the decoded ternary number. It can have leading zeroes.
Examples
input
.-.--
output
012
input
--.
output
20
input
-..-.--
output
1012
"""