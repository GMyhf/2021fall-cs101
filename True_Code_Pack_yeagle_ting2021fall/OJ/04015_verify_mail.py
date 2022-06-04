# -*- coding: utf-8 -*-
while True:
    try:
        mail=input()
        r1  = mail.count('@')==1
        r2a = mail[0] != '@' and mail[-1] != '@'
        r2b = mail[0] != '.' and mail[-1] != '.'
        r3  = mail.rfind('@') < mail.rfind('.')
        r4a = '@.' not in mail
        r4b = '.@' not in mail
        if r1 and r2a and r2b and r3 and r4a and r4b:
            print("YES")
        else : print("NO")
    except EOFError: break

#re_procode
import re
ans=[] ; frmt='[^@\.]+(\.[^@\.]+)*@[^@\.]+(\.[^@\.]+)+$'
while True:
    try:
        if re.match(frmt,input()): ans.append('YES')
        else: ans.append('NO')
    except EOFError: break
for a in ans: print(a)

"""info
Created on Tue Sep 28 17:20:32 2021
@author: Asus
http://cs101.openjudge.cn/practice/03087/
03087:邮箱验证
总时间限制: 1000ms 内存限制: 65536kB
描述
POJ 注册的时候需要用户输入邮箱，验证邮箱的规则包括：
1)有且仅有一个'@'符号
2)'@'和'.'不能出现在字符串的首和尾
3)'@'之后至少要有一个'.'，并且'@'不能和'.'直接相连
满足以上3条的字符串为合法邮箱，否则不合法，
编写程序验证输入是否合法
输入
输入包含若干行，每一行为一个代验证的邮箱地址，长度小于100
输出
每一行输入对应一行输出
如果验证合法，输出 YES
如果验证非法：输出 NO
样例输入
    .a@b.com
    pku@edu.cn
    cs101@gmail.com
    cs101@gmail
样例输出
    NO
    YES
    YES
    NO
"""