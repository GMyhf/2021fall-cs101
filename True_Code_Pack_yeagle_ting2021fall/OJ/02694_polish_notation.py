# -*- coding: utf-8 -*-
# actually rpn is reversed polish notation
# and this one is polish notation (non-reversed)

# ordinary recursion
statement = input().split()
i = -1
def rpn():
    global i, statement
    i += 1
    item = statement[i]
    if item == '+':
        return rpn() + rpn()
    elif item == '-':
        return rpn() - rpn()
    elif item == '*':
        return rpn() * rpn()
    elif item == '/':
        return rpn() / rpn()
    else:
        return float(item)
print('%.6f'%rpn())

# beware of %f, need high accuracy
statement = input().split()
def rpn():
    item = statement.pop(0)
    if item in '+-*/':
        return eval('%.8f%s%.8f'%(rpn(), item, rpn()))
    else:
        return float(item)
print('%.6f'%rpn())

# using string format to be no worry, refer to classmate Li-WenLiang
statement = input().split()
def rpn():
    item = statement.pop(0)
    if item in '+-*/':
        return str(eval(rpn()+item+rpn()))
    else:
        return item
print('%.6f'%float(rpn()))

"""info
Created on Tue Dec 14 08:18:40 2021
@author: Asus
http://cs101.openjudge.cn/practice/02694/
02694:逆波兰表达式    # changed name
总时间限制: 1000ms 内存限制: 65536kB
描述
逆波兰表达式是一种把运算符前置的算术表达式，例如普通的表达式2 + 3的逆波兰表示法为+ 2 3。逆波兰表达式的优点是运算符之间不必有优先级关系，也不必用括号改变运算次序，例如(2 + 3) * 4的逆波兰表示法为* + 2 3 4。本题求解逆波兰表达式的值，其中运算符包括+ - * /四个。
输入
输入为一行，其中运算符和运算数之间都用空格分隔，运算数是浮点数。
输出
输出为一行，表达式的值。
可直接用printf("%f\n", v)输出表达式的值v。
样例输入
* + 11.0 12.0 + 24.0 35.0
样例输出
1357.000000
提示
可使用atof(str)把字符串转换为一个double类型的浮点数。atof定义在math.h中。
此题可使用函数递归调用的方法求解。
"""