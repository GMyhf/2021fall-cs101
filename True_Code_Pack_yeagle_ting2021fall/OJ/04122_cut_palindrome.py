# -*- coding: utf-8 -*-
# maybe dangerous, close to TLE
ans = []
def palindrome(li:int, ri:int, s:str):
    while li < ri:
        if s[li] != s[ri]: return False
        li += 1
        ri -= 1
    return True
for _ in range(int(input())):
    word = input()
    leng = len(word)
    dp = [0]*(leng+1)
    for k in range(1, leng+1):
        dp[k] = k-1
    for i in range(1, leng+1):
        if palindrome(0, i-1, word):
            dp[i] = 0
            continue
        else:
            for j in range(1, i):
                if palindrome(j, i-1, word):
                    dp[i] = min(dp[i], dp[j]+1)
    ans.append(dp[leng])
print('\n'.join(map(str, ans)))

# refer to https://blog.csdn.net/curson_/article/details/52012303
# translated from C++

"""info
Created on Sat Dec 18 10:08:42 2021
@author: Asus
http://cs101.openjudge.cn/practice/04122/
04122:切割回文
总时间限制: 1000ms 内存限制: 65536kB
描述
阿福最近对回文串产生了非常浓厚的兴趣。
如果一个字符串从左往右看和从右往左看完全相同的话，那么就认为这个串是一个回文串。例如，“abcaacba”是一个回文串，“abcaaba”则不是一个回文串。
阿福现在强迫症发作，看到什么字符串都想要把它变成回文的。阿福可以通过切割字符串，使得切割完之后得到的子串都是回文的。
现在阿福想知道他最少切割多少次就可以达到目的。例如，对于字符串“abaacca”，最少切割一次，就可以得到“aba”和“acca”这两个回文子串。
输入
输入的第一行是一个整数 T (T <= 20) ，表示一共有 T 组数据。
接下来的 T 行，每一行都包含了一个长度不超过的 1000 的字符串，且字符串只包含了小写字母。
输出
对于每组数据，输出一行。该行包含一个整数，表示阿福最少切割的次数，使得切割完得到的子串都是回文的。
样例输入
3
abaacca
abcd
abcba
样例输出
1
3
0
提示
对于第一组样例，阿福最少切割 1 次，将原串切割为“aba”和“acca”两个回文子串。
对于第二组样例，阿福最少切割 3 次，将原串切割为“a”、“b”、“c”、“d”这四个回文子串。
对于第三组样例，阿福不需要切割，原串本身就是一个回文串。
repeated:
http://cs101.openjudge.cn/practice/08471/
08471:切割回文
"""