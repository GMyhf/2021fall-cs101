# -*- coding: utf-8 -*-
# no more set but how?
ans=[]
for _ in range(int(input())):
    a,b,c,r = map(int,input().split())
    left = min(a,b)
    right = max(a,b)
    r_le = c-r
    r_ri = c+r
    if left == right:
        lost = 0
    elif r_le <= left < r_ri <= right:
        lost = right - r_ri
    elif left <= r_le < right <= r_ri:
        lost = r_le - left
    elif left <= r_le < r_ri <= right:
        lost = r_le - left + right - r_ri
    elif r_le <= left and r_ri >= right:
        lost = 0
    else:
        lost = right - left
    ans.append(lost)
print('\n'.join(map(str, ans)))

# memory exceed
ans=[]
for _ in range(int(input())):
    a,b,c,r = map(int,input().split())
    contact = set(j for j in range(c-r,c+r))
    if a>b: time = set(i for i in range(b,a) if i not in contact)
    else: time = set(i for i in range(a,b) if i not in contact)
    ans.append(str(len(time)))
print('\n'.join(ans))

"""info
Created on Mon Nov  1 08:20:25 2021
@author: Asus
http://cs101.openjudge.cn/practice/20162/
20162:失联
总时间限制: 1000ms 内存限制: 65536kB
描述
考古学院的A同学到一片郊区考古，这片郊区可以看作线性数轴Ox，A同学从x=a移动到x=b，每分钟移动一个单位长度。
他的女朋友非常关心他，一直同他进行聊天，然而不幸的是，郊区的信号并不好，只有在信号塔附近手机才有信号，否则就会失联。现在在Ox上的x=c点有一个信号塔，其信号覆盖半径为r。
需要求出在A同学从a移动到b的过程中，他失联的时间。
输入
第一行输入一个整数t(1≤t≤1000)为测试数据组数，以下为t组测试数据。
每组测试数据由一行组成，依次为a,b,c,r(-10^8a,b,c可以相等（两两相等或者三个都相等均可以）
输出
输出一个整数，为同学A失联的时间。
样例输入
9
1 10 7 1
3 3 3 0
8 2 10 4
8 2 10 100
-10 20 -17 2
-3 2 2 0
-3 1 2 0
2 3 2 3
-1 3 -2 2
样例输出
7
0
4
0
30
5
4
0
3
"""