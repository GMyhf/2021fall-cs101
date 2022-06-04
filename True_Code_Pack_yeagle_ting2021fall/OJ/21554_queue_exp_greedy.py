# -*- coding: utf-8 -*-
n = int(input())
queue = enumerate(map(int, input().split()), start=1)
q_sort = sorted(queue, key = lambda x:x[1])
q_indx = []
time = 0
k = n-1
for stud in q_sort:
    indx, wait = stud
    time += k * wait
    q_indx.append(indx)
    k -= 1
print(*q_indx)
print('%.2f'%(time/n))

# odd code remastered
n = int(input())
queue = [*map(int, input().split())]
q_sort = sorted(queue)
q_indx = []
j = time = 0
for k in range(n-1, -1, -1):
    time += q_sort[j]*k
    i = queue.index(q_sort[j])
    q_indx.append(i+1)
    queue[i] = 0
    j += 1
print(*q_indx)
print('%.2f'%(time/n))

# odd code
n = int(input())
q = [int(x) for x in input().split()]
qs = sorted(q) ; qi=[] ; j=0 ; time=0
for k in range(n-1,-1,-1):
    time += qs[j]*k
    i = q.index(qs[j])
    qi.append(i+1)
    q[i]=0 ; j+=1
print(*qi)
print('%.2f'%(time/n))

"""info
Created on Thu Oct 28 09:36:04 2021
@author: Asus
http://cs101.openjudge.cn/practice/21554/
21554:排队做实验 (greedy)
总时间限制: 1000ms 内存限制: 65536kB
描述
某学院的学生都需要在某月的1号到2号期间完成课程实验，他们每个人的实验需要持续不同的时长。而实验室管理员要安排这些学生，按照一定顺序，在1号到2号期间全部完成实验。假设该学院的实验室同时只能容纳一名学生实验，而这些学生都非常积极，都希望被排在1号的第一个尽快完成实验。
假设该学院有n个学生，实验室管理员收到了n个学生每位需要占用实验室的时长T1,T2,...,Tn，由于学生发送预约邮件的时间比较接近，没办法按照先到先得的办法给学生分配实验时间。管理员很犯愁，他希望有一种能让所有学生平均等待时间尽可能小的顺序，来安排这n位同学的实验时间，请问你能帮帮他吗？
输出
输出为2行
第一行为一种学生实验顺序，即1到n的一种排列
第二行为这种方案下的平均等待时间（精确到小数点后两位）

样例
Sample1 Input:
10
81 365 72 99 22 7 444 203 1024 203
Sample1 Output:
6 5 3 1 4 8 10 2 7 9
431.90

Sample2 Input:
18
490 329 970 969 435 981 839 177 616 857 583 551 443 565 393 237 804 398 
Sample2 Output:
8 16 2 15 18 5 13 1 12 14 11 9 17 7 10 4 3 6
3750.89

提示
等待时间的定义是从时刻0开始的。第i个学生要等待前面i-1个学生都做完实验。
"""