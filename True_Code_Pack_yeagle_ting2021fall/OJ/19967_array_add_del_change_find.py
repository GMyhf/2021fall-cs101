# -*- coding: utf-8 -*-
a, out = [], []
for _ in range(int(input())):
    task = input().split()
    op = task[0]
    if op == '?':
        if task[1] in a:
            out.append(str(a.index(task[1])))
        else:
            out.append('Failed')
    else:
        indx = int(task[1])
        if op == '+':
            a.insert(indx, task[2])
        elif op == '-':
            del a[indx]
        elif op == '*':
            a[indx] = task[2]       
print('\n'.join(out))

"""info
Created on Wed Dec 22 21:09:51 2021
@author: Asus
http://cs101.openjudge.cn/practice/19967/
19967:数组增删改查
总时间限制: 1000ms 内存限制: 65536kB
描述
“增删改查”是数据库的几种基本操作，现在我们用数组DataBase[]来模拟一个数据库，来实现这几种功能。
1. 增：+ p v（将数据v插入到DataBase[p]位置上，保证p不会超过数据库末尾元素位置）
2. 删：- p  （将DataBase[p]位置的元素删除，保证p不会超过数据库末尾元素位置）
3. 改：* p v（将DataBase[p]位置的数据修改为v，保证p不会超过数据库末尾元素位置）
4. 查：? v  （查找DataBase中是否有值为v的元素，若查找成功输出其首次出现时的下标，否则输出“Failed”）
输入
第1行1个整数N（N<=1000），表示共有N次操作
第2~N+1行，每行1次操作
输出
对于每一次查找操作，给出结果；如果查找失败，输出“Failed”；
每个结果独自占一行
样例输入
6
+ 0 1
+ 0 2
? 2
* 1 3
- 1
? 1
样例输出
0
Failed
"""