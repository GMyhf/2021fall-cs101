# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:31:23 2021

@author: 乘一x1
"""

a = int(input())
if a%4 != 0 or (a%100== 0 and a%400 !=0):
    print("N")
else:
    print("Y")