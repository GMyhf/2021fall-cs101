# -*- coding: utf-8 -*-
n = int(input())
*arr, = map(int, input().split())
so_arr = sorted(arr)
pre = arr[0]
left = 1 ; right = n
for i in range(1, n):
    if arr[i] < pre:
        left = i
        break
    pre = arr[i]
for j in range(left, n):
    if arr[j] > pre:
        right = j
        break
re_arr = arr[:left-1] + [*reversed(arr[left-1:right])] + arr[right:]
if arr == so_arr:
    print('yes')
    print('1 1')
elif re_arr == so_arr:
    print('yes')
    print(left, right)
else:
    print('no')

# isn't beautiful code

"""info
Created on Mon Nov 29 15:53:40 2021
@author: Asus
https://codeforces.com/problemset/problem/451/B
451B-Sort the Array
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Being a programmer, you like arrays a lot. For your birthday, your friends have given you an array a consisting of n distinct integers.
Unfortunately, the size of a is too small. You want a bigger array! Your friends agree to give you a bigger array, but only if you are able to answer the following question correctly: is it possible to sort the array a (in increasing order) by reversing exactly one segment of a? See definitions of segment and reversing in the notes.

Input
The first line of the input contains an integer n (1 ≤ n ≤ 10**5) — the size of array a.
The second line contains n distinct space-separated integers: a[1], a[2], ..., a[n] (1 ≤ a[i] ≤ 10**9).
Output
Print "yes" or "no" (without quotes), depending on the answer.
If your answer is "yes", then also print two space-separated integers denoting start and end (start must not be greater than end) indices of the segment to be reversed. If there are multiple ways of selecting these indices, print any of them.
Examples
input
3
3 2 1
output
yes
1 3
input
4
2 1 3 4
output
yes
1 2
input
4
3 1 2 4
output
no
input
2
1 2
output
yes
1 1
Note
Sample 1. You can reverse the entire array to get [1, 2, 3], which is sorted.
Sample 3. No segment can be reversed such that the array will be sorted.
Definitions
A segment [l, r] of array a is the sequence a[l], a[l + 1], ..., a[r].
If you have an array a of size n and you reverse its segment [l, r], the array will become:
a[1], a[2], ..., a[l - 2], a[l - 1], a[r], a[r - 1], ..., a[l + 1], a[l], a[r + 1], a[r + 2], ..., a[n - 1], a[n].
"""