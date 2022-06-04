# -*- coding: utf-8 -*-
X = input()
if str.isupper(X[0]): print(X)
else:
    X = str.upper(X[0]) + X[1:]
    print(X)

#packed_code(but slower?)
X=input()
print(X if str.isupper(X[0]) else str.upper(X[0])+X[1:])

#come_on_it's_simple_code
x=input() ; print(x[0].upper()+x[1:])

"""info
Created on Fri Sep 24 20:28:08 2021
@author: Asus
https://codeforces.com/problemset/problem/281/A
281A-Word Capitalization
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.
Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 10**3.
Output
Output the given word after capitalization.
Examples
    input
        ApPLe
    output
        ApPLe
    input
        konjac
    output
        Konjac
"""