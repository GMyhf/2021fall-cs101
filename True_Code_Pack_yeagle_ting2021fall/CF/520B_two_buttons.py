# -*- coding: utf-8 -*-
# greedy/math/implementation_code
n, m = map(int, input().split())
if n > m:
    ans = n-m
else:
    ans = 0
    while n < m:
        if m%2: m += 1
        else: m //= 2
        ans += 1
    if n > m:
        ans += n-m
print(ans)

# bfs will do but I didn't try

"""info
Created on Mon Dec 20 08:19:12 2021
@author: Asus
https://codeforces.com/problemset/problem/520/B
520B-Two Buttons
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Vasya has found a strange device. On the front panel of a device there are: a red button, a blue button and a display showing some positive integer. After clicking the red button, device multiplies the displayed number by two. After clicking the blue button, device subtracts one from the number on the display. If at some point the number stops being positive, the device breaks down. The display can show arbitrarily large numbers. Initially, the display shows number n.
Bob wants to get number m on the display. What minimum number of clicks he has to make in order to achieve this result?

Input
The first and the only line of the input contains two distinct integers n and m (1 ≤ n, m ≤ 10**4), separated by a space .
Output
Print a single number — the minimum number of times one needs to push the button required to get the number m out of number n.
Examples
input
4 6
output
2
input
10 1
output
9
Note
In the first example you need to push the blue button once, and then push the red button once.
In the second example, doubling the number is unnecessary, so we need to push the blue button nine times.
"""