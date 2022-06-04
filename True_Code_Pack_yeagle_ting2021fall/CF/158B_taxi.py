# -*- coding: utf-8 -*-
input() ; g = input()
n3 = g.count('3')
n2 = g.count('2')
n1 = g.count('1')
ans = g.count('4') + n3 + n2//2
if n2%2:
    n1-=2 ; ans+=1
if n1>n3:
    n1-=n3 ; ans += -((-n1)//4)
print(ans)

"""info
Created on Sat Oct 23 12:07:10 2021
@author: Asus
https://codeforces.com/problemset/problem/158/B
158B-Taxi
time limit per test: 3 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

After the lessons n groups of schoolchildren went outside and decided to visit Polycarpus to celebrate his birthday. We know that the i-th group consists of si friends (1 ≤ si ≤ 4), and they want to go to Polycarpus together. They decided to get there by taxi. Each car can carry at most four passengers. What minimum number of cars will the children need if all members of each group should ride in the same taxi (but one taxi can take more than one group)?

Input
The first line contains integer n (1 ≤ n ≤ 10**5) — the number of groups of schoolchildren. The second line contains a sequence of integers s1, s2, ..., sn (1 ≤ si ≤ 4). The integers are separated by a space, si is the number of children in the i-th group.
Output
Print the single number — the minimum number of taxis necessary to drive all children to Polycarpus.
Examples
input
5
1 2 4 3 3
output
4
input
8
2 3 4 4 2 1 3 1
output
5
Note
In the first test we can sort the children into four cars like this:
the third group (consisting of four children),
the fourth group (consisting of three children),
the fifth group (consisting of three children),
the first and the second group (consisting of one and two children, correspondingly).
There are other ways to sort the groups into four cars.
"""