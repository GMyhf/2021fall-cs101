# -*- coding: utf-8 -*-
a = input().split('.')
b = input().split('.')
x = a
for i in range(len(a)):
    if int(a[i]) > int(b[i]): x=a ; break
    elif int(a[i]) < int(b[i]): x=b ; break
    else: pass
print('.'.join(x))

"""info #必须用int比较...
Created on Mon Oct  4 09:10:15 2021
@author: Asus
http://cs101.openjudge.cn/practice/12557/
12557:比较版本(string)
总时间限制: 1000ms 内存限制: 65536kB
描述
版本号是版本的标识号。可以假设版号只含数字和字符'.'，字符'.'代表的不是小数点，只是用来分隔每个数字。比如，2.5表示的是"the fifth second-level revision of the second first-level revision"，而不是 "two and a half" 或者 "half way to version three"。例如，按版本先后顺序排序，有0.1 < 1.1 < 1.2 < 1.10 < 13.37。
现在的任务是，比较两个版本的版本号，输出较新的版本号。
输入
输入为两行。
分别为两个版本号，不含空格。
输出
输出较新版本的版本号。
样例输入
1.0.2
1.1.2
样例输出
1.1.2
"""