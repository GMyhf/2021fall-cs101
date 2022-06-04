# -*- coding: utf-8 -*-
# code refer from GMyhf
n = int(input())
name = [input() for _ in range(n)]
name.sort()
Lmid = name[n//2 -1]
Rmid = name[n//2]
leng = len(Lmid)
ansr = ''
temp = ''
done = False
id_L = 0
while id_L < leng:
    for i in range(26):
        ansr = temp
        ansr += chr(65+i)
        if Lmid <= ansr < Rmid:
            done = True ; break
    if done: break
    temp += Lmid[id_L]
    id_L += 1
print(ansr)

# my odd code which didn't work...
n = int(input())
paper = [input() for _ in range(n)]
paper.sort()
left = [ord(x) for x in paper[n//2 -1]]
right = [ord(y) for y in paper[n//2]]
L = len(left) ; R = len(right)
L_short = L_long = False
if L > R:
    right += [90]*(L-R)
    L_long = True
if L < R:
    left += [65]*(R-L)
    L_short = True
ans = ''
for i in range(max(L, R)):
    if right[i] - left[i] > 1:
        if i+1 >= min(L, R):
            ans += chr(left[i])
            if L_short:
                ans = ans[:-1]
            if L_long:
                ans = ans[:-1] + chr(left[i]+1)
        else:
            ans += chr(left[i]+1)
        break
    ans += chr(left[i])
print(ans)

"""info
Created on Mon Nov 29 21:31:01 2021
@author: Asus
http://cs101.openjudge.cn/practice/16530/
16530:改卷子 v0.2(string)
总时间限制: 1000ms 内存限制: 65536kB
描述
闫老师希望将所有学生的卷子按姓名分成两摞，交给两位助教批改。假设每位考生姓名由大写字母组成。
你想出来一个好办法：你给出一个字符串，然后让闫老师将每位同学姓名的每个字母依次与该字符串比较。为了使这个过程更简单，你认为这个字符串应该尽可能的短。
现在有n位学生，请你找出这样一个字符串S，使得学生姓名小于或等于S的有一半，而另一半学生姓名大于S。如果有多个字符串满足最短长度，那么就取字母排序最小的那个字符串。
输入
每组数据以n开始，代表n个学生。(n >= 2 && n <= 1000 && n为偶数)。
接下来n行为学生姓名。每个名字都由大写字母组成，长度小于30个字母。
输出
针对每组数据，一行输出一个符合条件的最短字符串（大写字母）。
样例
Sample Input1:
2
LARHONDA
LARSEN
Sample Output1:
LARI

Sample Iutput2:
4
SAM
FRED
JOE
MARGARET
Sample Output2:
K

Sample Iutput3:
2
A
C
Sample Output3:
A

Sample Iutput4:
2
AYZZ
AZ
Sample Output4:
AYZZ
"""