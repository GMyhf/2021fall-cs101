# -*- coding: utf-8 -*-
N = int(input())
ans=[]
for _ in range(N): 
    s=input()
    real=s.count('###')/2
    link=s.count('### ###')
    ans.append(int(real-link))
print(sum(ans))

#change_little_but_much_better_code
ans = []
for _ in range(int(input())): 
    s = input()
    real = s.count('###')//2
    link = s.count('### ###')
    ans.append(real-link)
print(sum(ans))

"""info
Created on Wed Oct  6 08:53:18 2021
@author: Asus
http://cs101.openjudge.cn/practice/19949/
19949:提取实体v0.3 (string)
总时间限制: 1000ms 内存限制: 65536kB
描述
一个句子里面一些特殊的单词被称作实体，实体是存在于现实世界中并且可以与其他物体区分开来的物体，如“John has an apple .”这句话中，“John”和“apple”都是实体。
现在我们有很多个人工标注好实体的英文文档，每篇文档有很多个句子，每个句子中，每个实体的每单词都添加了“###”前缀，并且添加了“###”后缀，表明两个“###”之间的部分是实体或者是实体的一部分。例如：
1）两个“###”之间是实体：
“###John### has an ###apple### ”中有两个实体，是John和apple
2）两个“###”之间是实体的一部分，即是，连续的几个被“###”前后包裹的单词被认为是同一个实体：
“###Shelley### ###Berkley### , a Democratic representative”中有一个实体，是Shelley Berkley
“###Dominic### ###J.### ###Baranello### , an enduring power in Democratic Party”中有一个实体，是Dominic J. Baranello
请你帮助统计每篇文档里有多少个实体，暂时不考虑句子间的实体有重复的情况。
输入
第一行为1个整数N，代表文档里的句子数目。
接下来N行，每行代表一个英文句子，每个句子有多少单词是未知的，词与词之间用空格分隔。
输出
1个整数，代表该篇文档里的实体数目。
Sample1 Input:
1
###John### has an ###apple### .
Sample1 Output:
2
解释： 文档中只有一个句子，该句子中有两个实体“John”和“apple”，所以输出是2 。
Sample2 Input:
1
###Shelley### ###Berkley### , a Democratic representative of Nevada Mrs. ###Babbitt### 's daughter lives in ###Las### ###Vegas### testified about the case in July at a Congressional hearing into the recovery of art stolen during World War II .
Sample2 Output:
3
解释： 文档中仍然只有一个句子，但是现在有三个实体，“Shelley Berkley”，“Babitt”和“Las Vegas”
提示
2020/11/14增加说明：注意输出不是每行的实体数，是整篇文档的实体数。
"""