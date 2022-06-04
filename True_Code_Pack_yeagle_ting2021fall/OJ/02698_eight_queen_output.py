# -*- coding: utf-8 -*-
def queen8_stack(sol):
    stack = [([0]*8, 0)]
    while stack:
        S, cx = stack.pop()
        if cx == 8:
            sol.append(S[:])
            continue
        for c in range(7, -1, -1):
            for r in range(cx):
                if S[r] == c or abs(S[r]-c) == cx - r: break
            else:
                S[cx] = c
                stack.append((S[:], cx+1))
    return sol
full_sol = queen8_stack([])

for n in range(92):
    out = [[0]*8 for _ in range(8)]
    for i in range(8): out[ full_sol[n][i] ][i] = 1
    print('No. ' + str(n+1))
    for row in out: print(*row)

# another kind of output a huge string
output=[]
for n in range(92):
    out = [[0]*8 for _ in range(8)]
    for i in range(8): out[ full_sol[n][i] ][i] = 1
    output.append('No. ' + str(n+1))
    for row in out: output.append(' '.join(map(str, row)))
print('\n'.join(output))
    
"""info
Created on Wed Dec  1 11:22:50 2021
@author: Asus
http://cs101.openjudge.cn/practice/02698/
02698:八皇后问题
总时间限制: 10000ms 内存限制: 65536kB
描述
在国际象棋棋盘上放置八个皇后，要求每两个皇后之间不能直接吃掉对方。
输入
无输入。
输出
按给定顺序和格式输出所有八皇后问题的解（见Sample Output）。
样例输入
样例输出
No. 1
1 0 0 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 
0 1 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 0 1 0 0 
0 0 1 0 0 0 0 0 
No. 2
1 0 0 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 0 1 0 0 0 0 
0 0 0 0 0 1 0 0 
0 0 0 0 0 0 0 1 
0 1 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 1 0 0 0 0 0 
No. 3
1 0 0 0 0 0 0 0 
0 0 0 0 0 1 0 0 
0 0 0 0 0 0 0 1 
0 0 1 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 0 1 0 0 0 0 
0 1 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 
No. 4
1 0 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 
0 0 0 0 0 1 0 0 
0 0 1 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 1 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 
No. 5
0 0 0 0 0 1 0 0 
1 0 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 
0 1 0 0 0 0 0 0 
0 0 0 0 0 0 0 1 
0 0 1 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 0 1 0 0 0 0 
No. 6
0 0 0 1 0 0 0 0 
1 0 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 
0 1 0 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 1 0 0 0 0 0 
0 0 0 0 0 1 0 0 
No. 7
0 0 0 0 1 0 0 0 
1 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 1 
0 0 0 1 0 0 0 0 
0 1 0 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 1 0 0 0 0 0 
0 0 0 0 0 1 0 0 
No. 8
0 0 1 0 0 0 0 0 
1 0 0 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 
0 1 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 0 1 0 0 
No. 9
0 0 0 0 1 0 0 0 
1 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 0 1 0 0 
0 0 0 0 0 0 0 1 
0 1 0 0 0 0 0 0 
0 0 0 0 0 0 1 0 
0 0 1 0 0 0 0 0 
...以下省略
提示
此题可使用函数递归调用的方法求解。
"""