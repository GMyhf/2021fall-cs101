# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    w,h,n = map(int,input().split())
    area = w*h ; card=1 ; ok=0
    while area%2==0:
        area/=2 ; card*=2
        if card>=n: ok=1 ; break
    ans.append(['NO','YES'][ok or n<2])
print('\n'.join(ans))

"""info
Created on Sat Nov 13 08:19:10 2021
@author: Asus
https://codeforces.com/problemset/problem/1472/A
1472A-Cards for Friends
time limit per test: 1 second
memory limit per test: 256 megabytes
input: standard input
output: standard output

For the New Year, Polycarp decided to send postcards to all his n friends. He wants to make postcards with his own hands. For this purpose, he has a sheet of paper of size w×h, which can be cut into pieces.
Polycarp can cut any sheet of paper w×h that he has in only two cases:
If w is even, then he can cut the sheet in half and get two sheets of size w2×h;
If h is even, then he can cut the sheet in half and get two sheets of size w×h2;
If w and h are even at the same time, then Polycarp can cut the sheet according to any of the rules above.
After cutting a sheet of paper, the total number of sheets of paper is increased by 1.
Help Polycarp to find out if he can cut his sheet of size w×h at into n or more pieces, using only the rules described above.

Input
The first line contains one integer t (1≤t≤10**4) — the number of test cases. Then t test cases follow.
Each test case consists of one line containing three integers w, h, n (1≤w,h≤10**4,1≤n≤10**9) — the width and height of the sheet Polycarp has and the number of friends he needs to send a postcard to.
Output
For each test case, output on a separate line:
"YES", if it is possible to cut a sheet of size w×h into at least n pieces;
"NO" otherwise.
You can output "YES" and "NO" in any case (for example, the strings yEs, yes, Yes and YES will be recognized as positive).
Example
input
5
2 2 3
3 3 2
5 10 2
11 13 1
1 4 4
output
YES
NO
YES
YES
YES
Note
In the first test case, you can first cut the 2×2 sheet into two 2×1 sheets, and then cut each of them into two more sheets. As a result, we get four sheets 1×1. We can choose any three of them and send them to our friends.
In the second test case, a 3×3 sheet cannot be cut, so it is impossible to get two sheets.
In the third test case, you can cut a 5×10 sheet into two 5×5 sheets.
In the fourth test case, there is no need to cut the sheet, since we only need one sheet.
In the fifth test case, you can first cut the 1×4 sheet into two 1×2 sheets, and then cut each of them into two more sheets. As a result, we get four sheets 1×1.
"""