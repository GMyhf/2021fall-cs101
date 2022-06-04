# -*- coding: utf-8 -*-
a=int(input()) ; b=int(input()) ; c=int(input())
num=[a,b,c]
if sum(num)==3: print(3)
elif num.count(1)==2:
    if b!=1: print(sum(num))
    else: print(2*max(num))
elif a==1 or c==1: print(a*(b+1)*c)
elif b==1: print((min(a,c)+1)*max(a,c))
else: print(a*b*c)

#make_it_easy_code
a=int(input()) ; b=int(input()) ; c=int(input())
h=a+b+c ; j=a*b*c ; k=(a+b)*c ; l=a*(b+c)
print(max(h,j,k,l))

"""info
Created on Sun Oct 17 11:15:40 2021
@author: Asus
https://codeforces.com/problemset/problem/479/A
479A-Expression
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output
Petya studies in a school and he adores Maths. His class has been studying arithmetic expressions. On the last class the teacher wrote three positive integers a, b, c on the blackboard. The task was to insert signs of operations '+' and '*', and probably brackets between the numbers so that the value of the resulting expression is as large as possible. Let's consider an example: assume that the teacher wrote numbers 1, 2 and 3 on the blackboard. Here are some ways of placing signs and brackets:
1+2*3=7
1*(2+3)=5
1*2*3=6
(1+2)*3=9
Note that you can insert operation signs only between a and b, and between b and c, that is, you cannot swap integers. For instance, in the given sample you cannot get expression (1+3)*2.
It's easy to see that the maximum value that you can obtain is 9.
Your task is: given a, b and c print the maximum value that you can get.

Input
The input contains three integers a, b and c, each on a single line (1 ≤ a, b, c ≤ 10).
Output
Print the maximum value of the expression that you can obtain.
Examples
input
1
2
3
output
9
input
2
10
3
output
60
"""