# -*- coding: utf-8 -*-
ans = []
def josephus(n, p, m):
    kid = [i+1 for i in range(n)]
    seq = []
    out = kid.index(p)
    while n:
        out += m-1
        if out >= n: out %= n
        seq.append(str(kid[out]))
        del kid[out]
        n -= 1
    return seq
while True:
    n, p, m = map(int, input().split())
    if n==0: break
    ans.append(josephus(n, p, m))
for a in ans: print(','.join(a))

"""info
Created on Thu Nov  4 15:58:39 2021
@author: Asus
http://cs101.openjudge.cn/practice/03253/
03253:约瑟夫问题No.2
总时间限制: 1000ms 内存限制: 65536kB
描述
n 个小孩围坐成一圈，并按顺时针编号为1,2,…,n，从编号为 p 的小孩顺时针依次报数，由1报到m ，当报到 m 时，该小孩从圈中出去，然后下一个再从1报数，当报到 m 时再出去。如此反复，直至所有的小孩都从圈中出去。请按出去的先后顺序输出小孩的编号。
输入
每行是用空格分开的三个整数，第一个是n,第二个是p,第三个是m (0 < m,n < 300)。最后一行是:
0 0 0
输出
按出圈的顺序输出编号，编号之间以逗号间隔。
样例输入
8 3 4
0 0 0
样例输出
6,2,7,4,3,5,1,8
提示
可以利用模拟方法解题.
与 http://net.pku.edu.cn/~course/cs101/book2/pp_list.txt
中的 poj 2746 Joseph issue极为相似。
"""