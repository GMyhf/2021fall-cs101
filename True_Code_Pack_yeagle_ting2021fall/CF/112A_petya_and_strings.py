# -*- coding: utf-8 -*-
lst = []
for n in range(2):
    lst.append(input())
s1=str.lower(lst[0]) ; s2=str.lower(lst[1])
if s1 == s2:
    print(0)
else:
    for i in range(len(s1)) :     
        if s1 > s2 :
            print(1)
            break
        else :
            print(-1)
            break

#improved_code
s1=input().lower()
s2=input().lower()
if s1>s2: print(1)
elif s1<s2: print(-1)
else: print(0)

#legend_code
i=input;a=i().lower();b=i().lower()
print((a>b)-(a<b))

"""info
Created on Fri Sep 24 16:15:31 2021
@author: Asus
https://codeforces.com/problemset/problem/112/A
112A-Petya and Strings
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Little Petya loves presents. His mum bought him two strings of the same size for his birthday. The strings consist of uppercase and lowercase Latin letters. Now Petya wants to compare those two strings lexicographically. The letters' case does not matter, that is an uppercase letter is considered equivalent to the corresponding lowercase letter. Help Petya perform the comparison.

Input
Each of the first two lines contains a bought string. The strings' lengths range from 1 to 100 inclusive. It is guaranteed that the strings are of the same length and also consist of uppercase and lowercase Latin letters.
Output
If the first string is less than the second one, print "-1". If the second string is less than the first one, print "1". If the strings are equal, print "0". Note that the letters' case is not taken into consideration when the strings are compared.
Examples
    input
        aaaa
        aaaA
    output
        0
    input
        abs
        Abz
    output
        -1
    input
        abcdefg
        AbCdEfF
    output
        1
Note
If you want more formal information about the lexicographical order (also known as the "dictionary order" or "alphabetical order"), you can visit the following site:
http://en.wikipedia.org/wiki/Lexicographical_order
"""