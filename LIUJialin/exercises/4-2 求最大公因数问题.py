# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:01:12 2021

@author: 乘一x1
"""

def f(a,b):
    if a%b == 0:
        return b
    elif b > a%b:
        return f(b,a%b)
    else:
        return f(a%b,b)
while True:
    try:
        a,b = [int(x) for x in input().split(" ")]
        if a>b:
            print (f(a,b))
        else:
                print (f(b,a))
    except EOFError:
                    break