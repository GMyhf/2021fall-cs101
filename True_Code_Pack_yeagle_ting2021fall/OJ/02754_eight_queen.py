# -*- coding: utf-8 -*-
# recursive_dfs_code
sol=[]
def queen8_rec(S, cx=0):
    if len(sol) > 45: return
    if cx == 8:
        sol.append(''.join([str(i+1) for i in S]))
        return
    for c in range(8):
        for r in range(cx):
            if S[r] == c or abs(S[r]-c) == cx - r: break
        else:
            S[cx] = c
            queen8_rec(S, cx+1)
queen8_rec([0]*8)
full_sol = sol[:] + [*reversed([str(99999999-int(s)) for s in sol])]
print('\n'.join([full_sol[int(input())-1] for _ in range(int(input()))]))

# using_stack_dfs_code
def queen8_stack(sol):
    stack = [([0]*8, 0)]
    while stack:
        S, cx = stack.pop()
        if cx == 8:
            sol.append(''.join([str(i+1) for i in S]))
            continue
        for c in range(7, -1, -1):
            for r in range(cx):
                if S[r] == c or abs(S[r]-c) == cx - r: break
            else:
                S[cx] = c
                stack.append((S[:], cx+1))
    return sol
full_sol = queen8_stack([])
print('\n'.join([full_sol[int(input())-1] for _ in range(int(input()))]))

"""info
Created on Tue Nov 30 20:53:43 2021
@author: Asus
http://cs101.openjudge.cn/practice/02754/
02754:八皇后
总时间限制: 1000ms 内存限制: 65536kB
描述
会下国际象棋的人都很清楚：皇后可以在横、竖、斜线上不限步数地吃掉其他棋子。如何将8个皇后放在棋盘上（有8 * 8个方格），使它们谁也不能被吃掉！这就是著名的八皇后问题。
对于某个满足要求的8皇后的摆放方法，定义一个皇后串a与之对应，即a=b1b2...b8，其中bi为相应摆法中第i行皇后所处的列数。已经知道8皇后问题一共有92组解（即92个不同的皇后串）。
给出一个数b，要求输出第b个串。串的比较是这样的：皇后串x置于皇后串y之前，当且仅当将x视为整数时比y小。
输入
第1行是测试数据的组数n，后面跟着n行输入。每组测试数据占1行，包括一个正整数b(1 <= b <= 92)
输出
输出有n行，每行输出对应一个输入。输出应是一个正整数，是对应于b的皇后串。
样例输入
2
1
92
样例输出
15863724
84136275
"""