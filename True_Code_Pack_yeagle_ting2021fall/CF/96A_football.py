# -*- coding: utf-8 -*-
s = input()
s0 = s.find('0000000')<0
s1 = s.find('1111111')<0
if s0 and s1: print("NO")
else: print("YES")

#improved_code
s=input() ; print(['NO','YES'][('0'*7 in s)or('1'*7 in s)])

"""info
Created on Fri Oct  1 09:25:44 2021
@author: Asus
https://codeforces.com/problemset/problem/96/A
96A-Football
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Petya loves football very much. One day, as he was watching a football match, he was writing the players' current positions on a piece of paper. To simplify the situation he depicted it as a string consisting of zeroes and ones. A zero corresponds to players of one team; a one corresponds to players of another team. If there are at least 7 players of some team standing one after another, then the situation is considered dangerous. For example, the situation 00100110111111101 is dangerous and 11110111011101 is not. You are given the current situation. Determine whether it is dangerous or not.

Input
The first input line contains a non-empty string consisting of characters "0" and "1", which represents players. The length of the string does not exceed 100 characters. There's at least one player from each team present on the field.
Output
Print "YES" if the situation is dangerous. Otherwise, print "NO".
Examples
    input
        001001
    output
        NO
    input
        1000000001
    output
        YES
"""