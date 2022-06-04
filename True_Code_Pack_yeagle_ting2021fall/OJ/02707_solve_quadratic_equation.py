# -*- coding: utf-8 -*-
ans = []
for _ in range(int(input())):
    a, b, c = map(float, input().split())
    if b == 0: b = -b
    disc = b**2 - 4*a*c
    if disc == 0:
        x = (-b) / (2*a)
        ans.append('x1=x2=%.5f'%x)
    elif disc > 0:
        x1 = (-b + disc**0.5) / (2*a)
        x2 = (-b - disc**0.5) / (2*a)
        ans.append('x1=%.5f;x2=%.5f'%(x1, x2))
    else:
        real = - b/(2*a)
        cplx = ((-disc)**0.5) / (2*a)
        x1 = '%.5f+%.5fi'%(real, cplx)
        x2 = '%.5f-%.5fi'%(real, cplx)
        ans.append('x1=%s;x2=%s'%(x1, x2))
print('\n'.join(ans))

"""info
Created on Sat Dec 18 12:00:50 2021
@author: Asus
http://cs101.openjudge.cn/practice/02707/
02707:求一元二次方程的根
总时间限制: 1000ms 内存限制: 65536kB
描述
利用公式x1 = (-b + sqrt(b*b-4*a*c))/(2*a), x2 = (-b - sqrt(b*b-4*a*c))/(2*a)求一元二次方程ax2 + bx + c =0的根，其中a不等于0。
输入
第一行是待解方程的数目n。
其余n行每行含三个浮点数a, b, c（它们之间用空格隔开），分别表示方程ax2 + bx + c =0的系数。
输出
输出共有n行，每行是一个方程的根：
若是两个实根，则输出：x1=...;x2 = ...
若两个实根相等，则输出：x1=x2=...
若是两个虚根，则输出：x1=实部+虚部i; x2=实部-虚部i
所有实数部分要求精确到小数点后5位，数字、符号之间没有空格。
x1和x2的顺序：x1的实部>Re的实部||(x1的实部==x2的实部&&x1的虚部>=x2的虚部)
样例输入
3
1.0 3.0 1.0
2.0 -4.0 2.0
1.0 2.0 8.0
样例输出
x1=-0.38197;x2=-2.61803
x1=x2=1.00000
x1=-1.00000+2.64575i;x2=-1.00000-2.64575i
提示
1、需要严格按照题目描述的顺序求解x1、x2。
2、方程的根以及其它中间变量用double类型变量表示。
3、函数sqrt()在头文件math.h中。
4、要输出浮点数、双精度数小数点后5位数字，可以用下面这种形式：
printf("%.5f", num);
注意，在使用Java做此题时，可能会出现x1或x2等于-0的情形，此时，需要把负号去掉
"""