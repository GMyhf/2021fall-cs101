# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 22:47:51 2021
@author: Asus

STANDARD DATA TYPE:
    unchangeable： Number, String, Tuple
    changeable： List, Dictionary, Set
    
NUMBERS:
    int,  1, only one type
    bool,  True / False
    float,  1.23, 3E-2
    complex, 1 + 2j, 1.1 + 2.2j
"""
''' showing words&num
a=x="noob"; b="bruh"; c="C Ya~"; d="doge>.<"; e="E!"
def show_some_words(n1,n2,n3,s1,s2):
    print("It's " + n1 + " here, this one\nshows\nthree lines with a " + s1)
    print("I can connect " + n2, end="")
    print("    and " + n3 + ", then a empty line below, so, " + s2)
    return "No more words, sorry."

order1 = show_some_words(a,d,x,b,c)
print(order1)

num ='0123456789'  # 0=first,here the 0 character is "0"
def show_some_nums():
    print(num[0])              # output num, first character
    print(num[2:])             # output num, after *third*
    print(num[1:5])            # output num, from *second to fourth*
    print(num[0:-1])           # output num, from *first to thelastbutone*
    print(num[1:5:2])          # output num, from *second to fourth* & skip one each time
    print(num*2)               # output num twice
    print(num + ' hello')      # connect strings
    return "No more nums, sorry."

show_some_nums()
'''
''' find max num
def max_num(x,y,z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z

print(max_num(0,-9,3.142))
'''