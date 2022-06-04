# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 09:30:33 2021

@author: 乘一x1
"""

pos = -1
def Exp():
    global pos
    global calculateList
    pos = pos +1
    chr = calculateList[pos]
    if (chr == "+"):
        return Exp() + Exp()
    elif (chr == "-"):
        return Exp() - Exp()
    elif (chr == "*"):
        return Exp() * Exp()

    elif (chr == "/"):
        return Exp() / Exp()
    else:
        return float(chr)

calculateList = input().split()
result = Exp()
print("{:.6f}".format(result))