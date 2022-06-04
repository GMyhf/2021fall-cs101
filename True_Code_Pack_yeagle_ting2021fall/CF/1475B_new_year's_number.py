# -*- coding: utf-8 -*-
# good_math_code
ans=[]
for _ in range(int(input())):
    n = int(input())
    if n < 2020:
        ans += ['NO']
    elif n%2020 == 0 or n%2021 == 0:
        ans += ['YES']
    elif n//2020 >= n%2020:
        ans += ['YES']
    else:
        ans += ['NO']
print('\n'.join(ans))

# slow when n is so great (the for loop in else is brute force)
ans=[]
for _ in range(int(input())):
    n = int(input())
    if n < 2020:
        ans += ['NO']
    elif n%2020 == 0 or n%2021 == 0:
        ans += ['YES']
    else:
        for i in range(1, n//2021 +1):
            if (n-i)%2020 == 0:
                ans += ['YES']
                break
        else:
            ans += ['NO']
print('\n'.join(ans))

"""info
Created on Mon Nov 22 13:20:46 2021
@author: Asus
https://codeforces.com/problemset/problem/1475/B
1475B-New Year's Number
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Polycarp remembered the 2020-th year, and he is happy with the arrival of the new 2021-th year. To remember such a wonderful moment, Polycarp wants to represent the number n as the sum of a certain number of 2020 and a certain number of 2021.
For example, if:
n=4041, then the number n can be represented as the sum 2020+2021;
n=4042, then the number n can be represented as the sum 2021+2021;
n=8081, then the number n can be represented as the sum 2020+2020+2020+2021;
n=8079, then the number n cannot be represented as the sum of the numbers 2020 and 2021.
Help Polycarp to find out whether the number n can be represented as the sum of a certain number of numbers 2020 and a certain number of numbers 2021.

Input
The first line contains one integer t (1≤t≤10**4) — the number of test cases. Then t test cases follow.
Each test case contains one integer n (1≤n≤10**6) — the number that Polycarp wants to represent as the sum of the numbers 2020 and 2021.
Output
For each test case, output on a separate line:
"YES" if the number n is representable as the sum of a certain number of 2020 and a certain number of 2021;
"NO" otherwise.
You can output "YES" and "NO" in any case (for example, the strings yEs, yes, Yes and YES will be recognized as positive).
Example
input
5
1
4041
4042
8081
8079
output
NO
YES
YES
YES
NO
"""