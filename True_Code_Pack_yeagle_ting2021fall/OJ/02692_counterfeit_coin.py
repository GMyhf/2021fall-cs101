# -*- coding: utf-8 -*-
ans = []
for _ in range(int(input())):
    clue = [input().split() for _ in range(3)]
    for coin in 'ABCDEFGHIJKL':
        heavy = light = True
        for word in clue:
            left, right, r_stat = word
            h1 = coin in left and r_stat == 'up'
            h2 = coin in right and r_stat == 'down'
            h3 = coin not in left + right and r_stat == 'even'
            heavy &= any((h1, h2, h3))
            l1 = coin in left and r_stat == 'down'
            l2 = coin in right and r_stat == 'up'
            l3 = coin not in left + right and r_stat == 'even'
            light &= any((l1, l2, l3))
        fake = ''
        if heavy: fake = 'heavy'
        if light: fake = 'light'
        if fake:
            ans.append("%s is the counterfeit coin and it is %s."%(coin, fake))
            break
print('\n'.join(ans))

# refer to code of YiChen-Li in 2020fall-cs101.openjudge.cn_problems.pdf

"""info
Created on Sun Oct  3 10:58:16 2021  # solved on Fri Dec 17
@author: Asus
http://cs101.openjudge.cn/practice/1694/
1694:假币问题
总时间限制: 1000ms 内存限制: 65536kB
描述
赛利有12枚银币。其中有11枚真币和1枚假币。假币看起来和真币没有区别，但是重量不同。但赛利不知道假币比真币轻还是重。于是他向朋友借了一架天平。朋友希望赛利称三次就能找出假币并且确定假币是轻是重。例如:如果赛利用天平称两枚硬币，发现天平平衡，说明两枚都是真的。如果赛利用一枚真币与另一枚银币比较，发现它比真币轻或重，说明它是假币。经过精心安排每次的称量，赛利保证在称三次后确定假币。
输入
第一行有一个数字n，表示有n组测试用例。
对于每组测试用例：
输入有三行，每行表示一次称量的结果。赛利事先将银币标号为A-L。每次称量的结果用三个以空格隔开的字符串表示：天平左边放置的硬币 天平右边放置的硬币 平衡状态。其中平衡状态用``up'', ``down'', 或 ``even''表示, 分别为右端高、右端低和平衡。天平左右的硬币数总是相等的。
输出
输出哪一个标号的银币是假币，并说明它比真币轻还是重(heavy or light)。
样例输入
1
ABCD EFGH even 
ABCI EFJK up 
ABIJ EFGH even 
样例输出
K is the counterfeit coin and it is light.
"""