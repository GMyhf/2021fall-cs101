# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:32:02 2021

@author: 乘一x1
"""

feet = int(input())
if feet % 2 !=0:
        print("0 0")
elif feet %4 == 0:
        print(feet//4,feet//2)
else:
        print(feet//4+feet%4//2,feet//2)        