# -*- coding: utf-8 -*-
key = 'qwertyuiopasdfghjkl;zxcvbnm,./'
if input()=='L': move = 1
else: move = -1
msg = input() ; ori_msg=''
for i in range(len(msg)):
    ori_msg += key[key.index(msg[i])+move]
print(ori_msg)

"""info
Created on Wed Nov  3 08:44:25 2021
@author: Asus
https://codeforces.com/problemset/problem/474/A
474A-Keyboard
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Our good friend Mole is trying to code a big message. He is typing on an unusual keyboard with characters arranged in following way:
qwertyuiop
asdfghjkl;
zxcvbnm,./
Unfortunately Mole is blind, so sometimes it is problem for him to put his hands accurately. He accidentally moved both his hands with one position to the left or to the right. That means that now he presses not a button he wants, but one neighboring button (left or right, as specified in input).
We have a sequence of characters he has typed and we want to find the original message.

Input
First line of the input contains one letter describing direction of shifting ('L' or 'R' respectively for left or right).
Second line contains a sequence of characters written by Mole. The size of this sequence will be no more than 100. Sequence contains only symbols that appear on Mole's keyboard. It doesn't contain spaces as there is no space on Mole's keyboard.
It is guaranteed that even though Mole hands are moved, he is still pressing buttons on keyboard and not hitting outside it.
Output
Print a line that contains the original message.
Examples
input
R
s;;upimrrfod;pbr
output
allyouneedislove
"""