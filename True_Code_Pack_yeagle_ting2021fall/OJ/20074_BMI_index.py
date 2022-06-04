# -*- coding: utf-8 -*-
memo = {'M':0, 'F':0}
for _ in range(int(input())):
    h, w, s = input().split()
    h, w = int(h)/100, int(w)
    need = 0
    while True:
        bmi = w/(h**2)
        if bmi < 18.5: w += 8
        elif bmi > 25: w -= 5
        else: break
        need += 1
    memo[s] = max(memo[s], need)
print(memo['M'], memo['F'])

"""info
Created on Sat Dec 18 11:40:35 2021
@author: Asus
http://cs101.openjudge.cn/practice/20074/
20074:BMI指数
总时间限制: 1000ms 内存限制: 65536kB
描述
约翰是一个健身俱乐部的教练，他负责管理n个学生的体重，所以他需要把每位学生的体重控制在正常的范围之内。如果某位学生的体重偏瘦，他一个月可增重8kg；如果某位学生的体重正常，就维持原先的体重；如果某位学生的体重偏胖，他一个月可减轻体重的5kg。并且约翰安排男女分班上课，所以需要分别计算出男，女最多要开几个月的课。（以全部人都进入正常范围为标准）
输入
总共有n+1行，第一行为学生数n（1<=n<=12），从第二行开始是学生的信息，身高h（150<=h<=190），体重w（45<=w<=100），性别s（男为M，女为F）
输出
输出男生班和女生班分别最多需要多少个月，两个数字之间用空格隔开
样例输入
Sample input1：
2
170 75 M 
165 45 F
Sample output1：
1 1
样例输出
Sample input2：
2
180 65 M
187 53 M
Sample output2：
2 0
提示
WHO规定的BMI指数：偏瘦：<18.5，正常：18.5-24.9，超重：>25
BMI公式为：BMI=体重（单位为kg）/(身高*身高)（单位为m）
"""