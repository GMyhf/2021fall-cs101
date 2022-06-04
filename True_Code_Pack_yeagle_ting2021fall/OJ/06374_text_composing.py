# -*- coding: utf-8 -*-
n, text = int(input()), input().split()
ans = []
temp = text[0]+' '
leng = len(temp)
for i in range(1, n):
    leng += len(text[i])
    if leng <= 80:
        temp += text[i]+' '
        leng += 1
    elif leng > 80:
        ans.append(temp.rstrip())
        temp = text[i]+' '
        leng = len(temp)
else: ans.append(temp.rstrip())
print('\n'.join(ans))

# code below is buggy at some special data, maybe it's close to AC...
n, text = input(), input()
leng = len(text)
ans, left, right = [], 0, 79
while right < leng:
    while text[right] != ' ': right -= 1
    temp = text[left:right].strip()
    ans.append(temp)
    left = right
    right += 79
else: ans.append(text[left:].strip())
print('\n'.join(ans))

"""info
Created on Sun Dec 19 09:42:06 2021
@author: Asus
http://cs101.openjudge.cn/practice/06374/
06374:文字排版
总时间限制: 1000ms 内存限制: 65536kB
描述
给一段英文短文，单词之间以空格分隔（每个单词包括其前后紧邻的标点符号）。请将短文重新排版，要求如下：
每行不超过80个字符；每个单词居于同一行上；在同一行的单词之间以一个空格分隔；行首和行尾都没有空格。
输入
第一行是一个整数n，表示英文短文中单词的数目. 其后是n个以空格分隔的英文单词（单词包括其前后紧邻的标点符号，且每个单词长度都不大于40个字母）。
输出
排版后的多行文本，每行文本字符数最多80个字符，单词之间以一个空格分隔，每行文本首尾都没有空格。
样例输入
84
One sweltering day, I was scooping ice cream into cones and told my four children they could "buy" a cone from me for a hug. Almost immediately, the kids lined up to make their purchases. The three youngest each gave me a quick hug, grabbed their cones and raced back outside. But when my teenage son at the end of the line finally got his turn to "buy" his ice cream, he gave me two hugs. "Keep the changes," he said with a smile. 
样例输出
One sweltering day, I was scooping ice cream into cones and told my four
children they could "buy" a cone from me for a hug. Almost immediately, the kids
lined up to make their purchases. The three youngest each gave me a quick hug,
grabbed their cones and raced back outside. But when my teenage son at the end
of the line finally got his turn to "buy" his ice cream, he gave me two hugs.
"Keep the changes," he said with a smile.
"""