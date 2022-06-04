# -*- coding: utf-8 -*-
import re
print(['YES','NO'][re.search('h.*e.*l.*l.*o',input())==None])

"""info
Created on Thu Oct 14 08:48:09 2021
@author: Asus
https://codeforces.com/problemset/problem/58/A
58A-Chat room
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word s.

Input
The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.
Output
If Vasya managed to say hello, print "YES", otherwise print "NO".
Examples
input
ahhellllloou
output
YES
input
hlelo
output
NO
"""