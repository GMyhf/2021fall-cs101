# -*- coding: utf-8 -*-
n = input() ; yes=1
d = str(n.count('4')+n.count('7'))
for i in ['0','1','2','3','5','6','8','9']: 
    if i in d: print('NO') ; yes=0 ; break
if yes: print('YES')

'''maybe better?
n=input() ; d=str(n.count('4')+n.count('7'))
print(['NO','YES'][d.count('4')+d.count('7')==len(d)])
'''

"""info
Created on Sat Oct  9 20:09:16 2021
@author: Asus
https://codeforces.com/problemset/problem/110/A
110A-Nearly Lucky Number
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Petya loves lucky numbers. We all know that lucky numbers are the positive integers whose decimal representations contain only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.
Unfortunately, not all numbers are lucky. Petya calls a number nearly lucky if the number of lucky digits in it is a lucky number. He wonders whether number n is a nearly lucky number.

Input
The only line contains an integer n (1 ≤ n ≤ 10**18).
Please do not use the %lld specificator to read or write 64-bit numbers in С++. It is preferred to use the cin, cout streams or the %I64d specificator.
Output
Print on the single line "YES" if n is a nearly lucky number. Otherwise, print "NO" (without the quotes).
Examples
    input
        40047
    output
        NO
    input
        7747774
    output
        YES
    input
        1000000000000000000
    output
        NO
Note
In the first sample there are 3 lucky digits (first one and last two), so the answer is "NO".
In the second sample there are 7 lucky digits, 7 is lucky number, so the answer is "YES".
In the third sample there are no lucky digits, so the answer is "NO".
"""