# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    x,n,m = map(int,input().split())
    for _ in range(n):
        if x > 20:
            x = x//2 + 10
        else:
            break
    x -= 10*m
    if x>0:
        ans += ['NO']
    else:
        ans += ['YES']
print('\n'.join(ans))

"""info
Created on Fri Nov 19 08:45:59 2021
@author: Asus
https://codeforces.com/problemset/problem/1337/B
1337B-Kana and Dragon Quest game
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

Kana was just an ordinary high school girl before a talent scout discovered her. Then, she became an idol. But different from the stereotype, she is also a gameholic.
One day Kana gets interested in a new adventure game called Dragon Quest. In this game, her quest is to beat a dragon.
The dragon has a hit point of x initially. When its hit point goes to 0 or under 0, it will be defeated. In order to defeat the dragon, Kana can cast the two following types of spells.
Void Absorption
Assume that the dragon's current hit point is h, after casting this spell its hit point will become ⌊h2⌋+10. Here ⌊h2⌋ denotes h divided by two, rounded down.
Lightning Strike
This spell will decrease the dragon's hit point by 10. Assume that the dragon's current hit point is h, after casting this spell its hit point will be lowered to h−10.
Due to some reasons Kana can only cast no more than n Void Absorptions and m Lightning Strikes. She can cast the spells in any order and doesn't have to cast all the spells. Kana isn't good at math, so you are going to help her to find out whether it is possible to defeat the dragon.
Input
The first line contains a single integer t (1≤t≤1000)  — the number of test cases.
The next t lines describe test cases. For each test case the only line contains three integers x, n, m (1≤x≤10**5, 0≤n,m≤30)  — the dragon's intitial hit point, the maximum number of Void Absorptions and Lightning Strikes Kana can cast respectively.
Output
If it is possible to defeat the dragon, print "YES" (without quotes). Otherwise, print "NO" (without quotes).
You can print each letter in any case (upper or lower).

Example
input
7
100 3 4
189 3 4
64 2 3
63 2 3
30 27 7
10 9 1
69117 21 2
output
YES
NO
NO
YES
YES
YES
YES
Note
One possible casting sequence of the first test case is shown below:
Void Absorption ⌊1002⌋+10=60.
Lightning Strike 60−10=50.
Void Absorption ⌊502⌋+10=35.
Void Absorption ⌊352⌋+10=27.
Lightning Strike 27−10=17.
Lightning Strike 17−10=7.
Lightning Strike 7−10=−3.
"""