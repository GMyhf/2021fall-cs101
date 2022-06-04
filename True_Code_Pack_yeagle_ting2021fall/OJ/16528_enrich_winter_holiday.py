# -*- coding: utf-8 -*-
#greedy_code
n = int(input()) ; event=[]
for _ in range(n):
    event.append([int(x) for x in reversed(input().split())])
event.sort()             #event.sort(key = lambda x:x[1]) (replacing reversed())
end = event[0][0]
ans = 1
for i in range(1,n):
    if event[i][1]>end:
        ans += 1
        end = event[i][0]
print(ans)

#dp_code
event = [-1]*61
for _ in range(int(input())):
    start,end = map(int,input().split())
    event[end] = max(event[end],start)
dp = [0]*61
for d in range(61):
    remain = dp[d-1]
    taking = dp[event[d]-1] +1
    if event[d]>-1:
        dp[d] = max(remain,taking)
    else:
        dp[d] = remain
print(dp[60])

"""info
Created on Tue Nov  2 07:31:45 2021
@author: Asus
http://cs101.openjudge.cn/practice/16528/
16528:充实的寒假生活(greedy/dp)
总时间限制: 1000ms 内存限制: 65536kB
描述
寒假马上就要到了，龙傲天同学获得了从第0天开始到第60天结束为期61天超长寒假，他想要尽可能丰富自己的寒假生活。
现提供若干个活动的起止时间，请计算龙同学这个寒假至多可以参加多少个活动？注意所参加的活动不能有任何时间上的重叠，在第x天结束的活动和在第x天开始的活动不可同时选择。
输入
第一行为整数n，代表接下来输入的活动个数(n < 10000)
紧接着的n行，每一行都有两个整数，第一个整数代表活动的开始时间，第二个整数代表全结束时间
输出
输出至多参加的活动个数
样例输入
5
0 0
1 1
2 2
3 3
4 4
样例输出
5
"""