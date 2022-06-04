# -*- coding: utf-8 -*-
M, N = map(int, input().split())
cnt = {} ; ids = {'b':-1}
good = same = n_problem = 0
total = M*N
edge = [['b']*(N+2)]
mx = edge + [['b', *map(int, input().split()), 'b']for _ in range(M)] + edge

for i in range(total):
    try:
        point = [*map(int, input().split())]
        if n_problem == 0: n_problem = len(point)
    except: point = [0]*n_problem
    sum_pt = sum(point)
    if sum_pt in cnt:
        cnt[sum_pt] += 1
    else:
        cnt[sum_pt] = 1
    ids[i] = point

for y in range(1, M+1):
    for x in range(1, N+1):
        ct = ids[mx[y][x]]
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if ct == ids[mx[y+dy][x+dx]]: same += 1 ; break

limit = total*0.4
key_cnt = sorted(cnt, reverse=True)
for k in key_cnt:
    if good + cnt[k] > limit: break
    good += cnt[k]

print(same, good)

"""info 
Created on Tue Nov 23 15:12:28 2021
@author: Asus
http://cs101.openjudge.cn/practice/16531/
16531:上机考试 v0.2 (matrix)
总时间限制: 1000ms 内存限制: 65536kB
描述
一个班的同学在M行*N列的机房考试，给出学生的座位分布和每个人的做题情况，统计做题情况与周围（上下左右）任一同学相同的学生人数。
另外，由于考试的优秀率不能超过40%，请统计这个班的优秀人数（可能为0，相同分数的同学必须要么全是优秀，要么全不是优秀）。
输入
第一行为两个整数，M和N
接下来M行每行N个整数，代表对应学生的编号，编号各不相同，范围由0到M*N-1
接下来M*N行，顺序给出编号由0到n-1的同学的做题情况，1代表做对，0代表做错。
输出
两个整数，以空格分隔；分别代表“与周围任一同学做题情况相同的学生人数”和“班级优秀的人数”
样例输入
样例一输入
2 5
0 1 2 3 4
5 6 7 8 9
1 1 1
1 0 1
0 0 0
0 0 1
0 0 0
1 1 1
1 1 1
1 1 1
1 1 1
1 1 1
样例一输出
6 0
样例一解释：
编号为0 5 6 7 8 9的同学做题情况与周围同学相同，因此第一个整数是6。
全对的同学人数已经超过了40%，因此优秀的人数为0
样例输出
样例二输入：
1 3
1 0 2
0 1 0 0
0 0 0 0
0 0 0 0
样例二输出；
0 1
样例二解释：
并不存在与相邻同学做题情况相同的同学，并且做对一题的同学比例小于40%，因此有一人优秀
提示
1）M*N行做题情况可能为空。因为如果所有学生做题过程中，一直没有提交，则空。
2）空行(即ASCII的回车符)与空行，是“答题情况相同”。全是0的输入，与全是0，是“答题情况相同”
3）“答题情况相同”不是“答题总数一样”
4）输出的第二个数为班级优秀的人数
5）考试题目数量需要自己求，不一定是3道

#odd_long_long_code
M, N = map(int, input().split())
count = {}
ids = {'b':-1}
row = -1
total = N*M
mx = [[*map(int, input().split())] for _ in range(M)]
for i in range(total):
    try:
        point = [*map(int, input().split())]
    except:
        point = [0, 0, 0, 0]
    sum_pt = sum(point)
    if sum_pt in count:
        count[sum_pt] += 1
    else:
        count[sum_pt] = 1
    ids[i] = point
same = 0
border = [['b']*(N+2)]
pro_mx = border + [['b', *r, 'b'] for r in mx] + border
for y in range(1, M+1):
    for x in range(1, N+1):
        ct = ids[pro_mx[y][x]]
        up = ids[pro_mx[y-1][x]]
        do = ids[pro_mx[y+1][x]]
        le = ids[pro_mx[y][x-1]]
        ri = ids[pro_mx[y][x+1]]
        if any((ct==up, ct==do, ct==le, ct==ri)):
            same += 1 ; continue
key_count = sorted(count, reverse=True)
good = 0
limit = total*0.4
for k in key_count:
    if good + count[k] > limit:
        break
    else:
        good += count[k]
print(same, good)
"""