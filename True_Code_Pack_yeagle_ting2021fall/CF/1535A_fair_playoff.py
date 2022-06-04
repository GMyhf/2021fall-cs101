# -*- coding: utf-8 -*-
ans=[]
for _ in range(int(input())):
    s = [*map(int,input().split())]
    sx = sorted(s)
    if {max(s[0:2]),max(s[2:4])}-{sx[2],sx[3]}:
        ans+=['NO']
    else: ans+=['YES']
print('\n'.join(ans))

# line6: min(s[0:2])>max(s[2:4]) or max(s[0:2])<min(s[2:4])

"""info
Created on Sun Nov 14 09:10:38 2021
@author: Asus
https://codeforces.com/problemset/problem/1535/A
1535A-Fair Playoff
time limit per test: 2 seconds
memory limit per test: 256 megabytes
input: standard input
output: standard output

Four players participate in the playoff tournament. The tournament is held according to the following scheme: the first player will play with the second, and the third player with the fourth, then the winners of the pairs will play in the finals of the tournament.
It is known that in a match between two players, the one whose skill is greater will win. The skill of the i-th player is equal to si and all skill levels are pairwise different (i. e. there are no two identical values in the array s).
The tournament is called fair if the two players with the highest skills meet in the finals.
Determine whether the given tournament is fair.

Input
The first line contains a single integer t (1≤t≤10**4) — the number of test cases.
A single line of test case contains four integers s1,s2,s3,s4 (1≤si≤100) — skill of the players. It is guaranteed that all the numbers in the array are different.
Output
For each testcase, output YES if the tournament is fair, or NO otherwise.
Example
input
4
3 7 9 5
4 5 6 9
5 3 8 1
6 5 3 2
output
YES
NO
YES
NO
Note
Consider the example:
in the first test case, players 2 and 3 with skills 7 and 9 advance to the finals;
in the second test case, players 2 and 4 with skills 5 and 9 advance to the finals. The player with skill 6 does not advance, but the player with skill 5 advances to the finals, so the tournament is not fair;
in the third test case, players 1 and 3 with skills 5 and 8 advance to the finals;
in the fourth test case, players 1 and 3 with skills 6 and 3 advance to the finals. The player with skill 5 does not advance, but the player with skill 3 advances to the finals, so the tournament is not fair.
"""