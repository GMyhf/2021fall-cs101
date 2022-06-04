# -*- coding: utf-8 -*-
n = 10000
isprime = [1]*(n+1)
for i in range(2, int(n**0.5)+1):
    if isprime[i]:
        for j in range(i*i, n+1, i): isprime[j]=0
t_prime = set(x**2 for x in range(2, n+1) if isprime[x])
ans = []
m, n = map(int, input().split())
for _ in range(m):
    sum_mark = 0
    lesson = [*map(int, input().split())]
    for mark in lesson:
        if mark in t_prime:
            sum_mark += mark
    if sum_mark:
        ans.append('%.2f'%(sum_mark/len(lesson)))
    else:
        ans.append('0')
print('\n'.join(ans))

"""info
Created on Mon Dec 13 23:19:48 2021
@author: Asus
http://cs101.openjudge.cn/practice/18176/
18176:2050年成绩计算(Sieve of Eratosthenes)
总时间限制: 400ms 内存限制: 65536kB
描述
随着人工智能技术和基因编辑技术的普及，2050年的学生成绩计算与目前2018年的规则很不一样。课程成绩要求是t-prime，才是有效成绩，否则按照零分计算。
现在需要统计每位学生在一个学期中，所有有效成绩课程的平均分，需要你的帮忙。
（素数是指除了1和它本身以外,不能被任何整数整除的数。 类似地，如果整数t恰好有且仅有三个不同的正除数，我们将称为它为t-prime。）
输入
第一行位两个整数，m个学生（1≤m≤2000），n门课（1≤n≤100，每个学生选课数可以不一样）
接下来m行，每行代表学生选课获得成绩。成绩由空格分隔，成绩是整数 Xi (1≤Xi≤10^8)。
输出
共m行，每行对应一位学生有效成绩课程的平均分（小数点后保留两位）。如果该生所有选课有效成绩是零分，则输出零。
对如下样例，第一个学生所有成绩都不是t-prime，因此输出0，注意这里不保留两位小数。
第二位学生只有4分是有效分数，故输出4/3 = 1.33
第三位学生只有两门课有成绩，4和25均为t-prime，因此输出平均值14.50
样例输入
3 3
100 120 2
3 4 5
4 25
样例输出
0
1.33
14.50
"""
# btw hope this will not become true in the future...