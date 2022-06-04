# -*- coding: utf-8 -*-
x=int(input()) ; ans=[]
while x!=1:
    if x%2:
        y = x*3 + 1
        ans.append('{}*3+1={}'.format(x,y))
    else:
        y = int(x/2)
        ans.append('{}/2={}'.format(x,y))
    x = y
for a in ans: print(a)

"""info
Created on Wed Oct 20 23:13:37 2021
@author: Asus
http://cs101.openjudge.cn/practice/21459/
21459:How old are you？(implementation)
查看提交统计提问
总时间限制: 1000ms 内存限制: 65536kB
描述
在一次社团迎新活动上，小翔和小叶抽到了How old are you这个游戏，游戏规则如下：
1) 1号玩家任意报出一个正整数x
2) 2号玩家开始进行如下计算：如果x是奇数，那么把他乘以3再加1；如果是偶数，那么就把他除以2，按照这样的规则重复处理
3) 如果最终2号玩家能够得到1，那么2号玩家获胜，否则1号玩家获胜
由于小翔知道对于任意正整数x，经过有限的变换后都能够得到1，为了讨得小叶开心，他主动选择当1号玩家。而结果，自然每次都是小叶获胜。面对这样的情况，戏精小翔面露囧色的问到：“怎么老是你？
输入
一个正整数x (x>1)
输出
从输入整数到1的变换步骤，每一步为一行，每一步中描述计算过程

sample1 in
3
sample1 out
3*3+1=10
10/2=5
5*3+1=16
16/2=8
8/2=4
4/2=2
2/2=1

sample2 in
5
sample2 out
5*3+1=16
16/2=8
8/2=4
4/2=2
2/2=1
提示
如果:
x = 2
y = 7
print("{}*3+1={}".format(x, y))
会输出 2*3+1=7
"""