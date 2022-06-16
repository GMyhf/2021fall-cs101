# -*- coding: utf-8 -*-
extra=[0,5,3,1]
while 1:
    a,b,c,d,e,f = map(int,input().split())
    if a+b+c+d+e+f==0: break
    box = f + e + d - (-c//4)
    can_b = 5*d + extra[c%4]
    if b>can_b: box += -((can_b-b)//9)
    can_a = 36*box - (36*f + 25*e + 16*d + 9*c + 4*b)
    if a>can_a: box += -((can_a-a)//36)
    print(box)

"""info # mock 211014 # without [] append is ok
Created on Thu Oct 14 15:49:13 2021
@author: Asus
http://cs101.openjudge.cn/practice/01017/
01017:装箱问题
总时间限制: 1000ms 内存限制: 65536kB
描述
一个工厂制造的产品形状都是长方体，它们的高度都是h，长和宽都相等，一共有六个型号，他们的长宽分别为1*1, 2*2, 3*3, 4*4, 5*5, 6*6。这些产品通常使用一个 6*6*h 的长方体包裹包装然后邮寄给客户。因为邮费很贵，所以工厂要想方设法的减小每个订单运送时的包裹数量。他们很需要有一个好的程序帮他们解决这个问题从而节省费用。现在这个程序由你来设计。
输入
输入文件包括几行，每一行代表一个订单。每个订单里的一行包括六个整数，中间用空格隔开，分别为1*1至6*6这六种产品的数量。输入文件将以6个0组成的一行结尾。
输出
除了输入的最后一行6个0以外，输入文件里每一行对应着输出文件的一行，每一行输出一个整数代表对应的订单所需的最小包裹数。
样例输入
0 0 4 0 0 1 
7 5 1 0 0 0 
0 0 0 0 0 0 
样例输出
2 
1
"""