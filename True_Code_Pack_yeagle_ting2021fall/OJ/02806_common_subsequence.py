# -*- coding: utf-8 -*-
ans=[]
while True:
    try:
        x,y = input().split()
        if not (set(x) & set(y)):
            ans += ['0'] ; continue
        Lx = len(x) ; Ly = len(y)
        seq = set()
        for k in range(Lx):
            com = 0 ; pre_j = 0
            for i in range(k,Lx):
                for j in range(pre_j,Ly):
                    if x[i]==y[j]:
                        pre_j = j+1
                        com += 1 ; break
            seq.add(com)
        for k in range(Ly):
            com = 0 ; pre_j = 0
            for i in range(k,Ly):
                for j in range(pre_j,Lx):
                    if y[i]==x[j]:
                        pre_j = j+1
                        com += 1 ; break
            seq.add(com)
        ans += [str(max(seq))]
    except EOFError: break
print('\n'.join(ans))

''' code below got something wrong and I failed to fix it...
ans=[]
while True:
    try:
        x,y = input().split()
        if not (set(x) & set(y)):
            ans += ['0'] ; continue
        Lx = len(x) ; Ly = len(y)
        dx = 0 ; pre_j = 0
        for i in range(Lx):
            for j in range(pre_j,Ly):
                if x[i]==y[j]:
                    pre_j = j+1
                    dx += 1 ; break
        dy = 0 ; pre_q = 0
        for p in range(Ly):
            for q in range(pre_q,Lx):
                if y[p]==x[q]:
                    pre_q = q+1
                    dy+=1 ; break
        ans += [str(max(dx,dy))]
    except EOFError: break
print('\n'.join(ans))
'''

# wait, this should be easier...
# refer to https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/

# the recursive method (very time-consuming)
def lcs_rec(X, Y, m, n):
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcs_rec(X, Y, m-1, n-1);
    else:
       return max(lcs_rec(X, Y, m, n-1), lcs_rec(X, Y, m-1, n))
# below is driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs_rec(X, Y, len(X), len(Y)))

# to submit on OJ: (but this is TLE...)
def lcs_rec(X, Y, m, n):
    if m == 0 or n == 0:
       return 0
    elif X[m-1] == Y[n-1]:
       return 1 + lcs_rec(X, Y, m-1, n-1);
    else:
       return max(lcs_rec(X, Y, m, n-1), lcs_rec(X, Y, m-1, n))
ans = []
while True:
    try: x, y = input().split()
    except EOFError: break
    ans.append(lcs_rec(x, y, len(x), len(y)))
print('\n'.join(map(str, ans)))


# the dp method
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n + 1) for i in range(m + 1)]
    """Following steps build L[m + 1][n + 1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
# below is driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs_dp(X, Y))

# to actually AC on OJ:
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)
    L = [[None]*(n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[m][n]
ans = []
while True:
    try: x, y = input().split()
    except EOFError: break
    ans.append(lcs_dp(x, y))
print('\n'.join(map(str, ans)))



"""info    # same with 01458:Common Subsequence (English version)
Created on Thu Nov  4 13:26:53 2021
@author: Asus

http://cs101.openjudge.cn/practice/02806/
02806:公共子序列
总时间限制: 1000ms 内存限制: 65536kB
描述
我们称序列Z = < z1, z2, ..., zk >是序列X = < x1, x2, ..., xm >的子序列当且仅当存在 严格上升 的序列< i1, i2, ..., ik >，使得对j = 1, 2, ... ,k, 有xij = zj。比如Z = < a, b, f, c > 是X = < a, b, c, f, b, c >的子序列。
现在给出两个序列X和Y，你的任务是找到X和Y的最大公共子序列，也就是说要找到一个最长的序列Z，使得Z既是X的子序列也是Y的子序列。
输入
输入包括多组测试数据。每组数据包括一行，给出两个长度不超过200的字符串，表示两个序列。两个字符串之间由若干个空格隔开。
输出
对每组输入数据，输出一行，给出两个序列的最大公共子序列的长度。
样例输入
abcfbc         abfcab
programming    contest 
abcd           mnp
样例输出
4
2
0

http://cs101.openjudge.cn/practice/01458/
01458:Common Subsequence
总时间限制: 1000ms 内存限制: 65536kB
描述
A subsequence of a given sequence is the given sequence with some elements (possible none) left out. Given a sequence X = < x1, x2, ..., xm > another sequence Z = < z1, z2, ..., zk > is a subsequence of X if there exists a strictly increasing sequence < i1, i2, ..., ik > of indices of X such that for all j = 1,2,...,k, xij = zj. For example, Z = < a, b, f, c > is a subsequence of X = < a, b, c, f, b, c > with index sequence < 1, 2, 4, 6 >. Given two sequences X and Y the problem is to find the length of the maximum-length common subsequence of X and Y.
输入
The program input is from the std input. Each data set in the input contains two strings representing the given sequences. The sequences are separated by any number of white spaces. The input data are correct.
输出
For each set of data the program prints on the standard output the length of the maximum-length common subsequence from the beginning of a separate line.
样例输入
abcfbc         abfcab
programming    contest 
abcd           mnp
样例输出
4
2
0
"""