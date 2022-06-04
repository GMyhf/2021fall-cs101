# -*- coding: utf-8 -*-
ans=[] ; dic={}
while True:
    try:
        eng, frg = input().split()
        dic[frg] = eng
    except: break
while True:
    try:
        x = input()
        if x in dic:
            ans += [dic[x]]
        else:
            ans += ['eh']
    except EOFError: break
print('\n'.join(ans))

"""info
Created on Mon Nov 22 22:39:38 2021
@author: Asus
http://cs101.openjudge.cn/practice/02503/
02503:Babelfish
总时间限制: 3000ms 内存限制: 65536kB
描述
You have just moved from Waterloo to a big city. The people here speak an incomprehensible dialect of a foreign language. Fortunately, you have a dictionary to help you understand them.
输入
Input consists of up to 100,000 dictionary entries, followed by a blank line, followed by a message of up to 100,000 words. Each dictionary entry is a line containing an English word, followed by a space and a foreign language word. No foreign word appears more than once in the dictionary. The message is a sequence of words in the foreign language, one word on each line. Each word in the input is a sequence of at most 10 lowercase letters.
输出
Output is the message translated to English, one word per line. Foreign words not in the dictionary should be translated as "eh".
样例输入
dog ogday
cat atcay
pig igpay
froot ootfray
loops oopslay

atcay
ittenkay
oopslay
样例输出
cat
eh
loops
提示
Huge input and output,scanf and printf are recommended.
"""