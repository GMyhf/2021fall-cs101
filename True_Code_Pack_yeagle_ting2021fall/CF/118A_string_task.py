# -*- coding: utf-8 -*-
string = input().lower()
vowels = ['a','o','y','e','u','i']
ans = []
for i in string:
    if i not in vowels:
        ans.append("."+i)
print("".join(ans))

#improved_code
ans = []
for i in input().lower():
    if i not in 'aoyeui':
        ans.append("."+i)
print("".join(ans))

"""info
Created on Tue Sep 28 08:20:49 2021
@author: Asus
https://codeforces.com/problemset/problem/118/A
118A-String Task
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:
1.deletes all the vowels,
2.inserts a character "." before each consonant,
3.replaces all uppercase consonants with corresponding lowercase ones.
Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.
Help Petya cope with this easy task.

Input
The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.
Output
Print the resulting string. It is guaranteed that this string is not empty.
Examples
    input
        tour
    output
        .t.r
    input
        Codeforces
    output
        .c.d.f.r.c.s
    input
        aBAcAba
    output
        .b.c.b
"""