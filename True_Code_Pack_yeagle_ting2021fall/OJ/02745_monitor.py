# -*- coding: utf-8 -*-
ans = []
while True:
    s, n = input().split()
    if s == '0': del ans[-1] ; break
    s, leng = int(s), len(n)
    fu = ' ' + '-'*s + ' '
    no = ' '*(s+2)
    le = '|' + ' '*(s+1)
    ri = ' '*(s+1) + '|'
    lr = '|' + ' '*s + '|'
    show = {'1':[no,ri,no,ri,no],'2':[fu,ri,fu,le,fu],'3':[fu,ri,fu,ri,fu],
            '4':[no,lr,fu,ri,no],'5':[fu,le,fu,ri,fu],'6':[fu,le,fu,lr,fu],
            '7':[fu,ri,no,ri,no],'8':[fu,lr,fu,lr,fu],'9':[fu,lr,fu,ri,fu],
            '0':[fu,lr,no,lr,fu]}
    part = ['', '', '', '', '']
    for k in range(leng):
        num = show[n[k]]
        for i in range(5): part[i] += num[i]+' '
    for j in range(5):
        if j in {1,3}:
            for _ in range(s): ans.append(part[j])
        else: ans.append(part[j])
    ans.append(' ')
print('\n'.join(ans))

"""info
Created on Wed Dec 22 18:56:16 2021
@author: Asus
http://cs101.openjudge.cn/practice/02745/
02745:显示器
总时间限制: 1000ms 内存限制: 65536kB
描述
你的一个朋友买了一台电脑。他以前只用过计算器，因为电脑的显示器上显示的数字的样子和计算器是不一样，所以当他使用电脑的时候会比较郁闷。为了帮助他，你决定写一个程序把在电脑上的数字显示得像计算器上一样。
输入
输入包括若干行，每行表示一个要显示的数。每行有两个整数s和n (1 <= s <= 10, 0 <= n <= 99999999)，这里n是要显示的数，s是要显示的数的尺寸。
如果某行输入包括两个0，表示输入结束。这行不需要处理。
输出
显示的方式是：用s个'-'表示一个水平线段，用s个'|'表示一个垂直线段。这种情况下，每一个数字需要占用s+2列和2s+3行。另外，在两个数字之间要输出一个空白的列。在输出完每一个数之后，输出一个空白的行。注意：输出中空白的地方都要用空格来填充。
样例输入
2 12345
3 67890
0 0
样例输出
      --   --        -- 
   |    |    | |  | | 
   |    |    | |  | | 
      --   --   --   -- 
   | |       |    |    |
   | |       |    |    |
      --   --        -- 

 ---   ---   ---   ---   --- 
|         | |   | |   | |   |
|         | |   | |   | |   |
|         | |   | |   | |   |
 ---         ---   --- 
|   |     | |   |     | |   |
|   |     | |   |     | |   |
|   |     | |   |     | |   |
 ---         ---   ---   ---
提示
数字(digit)指的是0，或者1，或者2……或者9。
数(number)由一个或者多个数字组成。
"""