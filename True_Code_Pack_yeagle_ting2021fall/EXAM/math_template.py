# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- basic operation and logic
--- import math
--- others
"""

""" template below for basic operation and logic """

# if calculation included float type, ruesult will be float type
print(1+2+3, 1+2+3.0)

# divide: '/' return float, '//' return int (floor)
print(8/2, 8//2)
print(9/2, 9//2)

# some logic of bool value, bool()
print(True & False, True | False)    # '&' is 'and', '|' is 'or'
print(True + True, True + False, False + False)

print(bool(0), bool(1), bool(123456))
print(bool(''), bool(' '), bool('a'))
print(int(True), int(False))    # 1 0

# any() & all() take one argument, make it iterable
print(any([False, False, True]))
print(any([False, False, False]))
print(all([False, False, True]))
print(all([True, True, True]))
print(any('0 0 0'), any(''))

these_are_False = ['', 0, None, [], {}, set(), ()]
print(any(these_are_False))
these_are_True = ['x', 1, 3.14, [''], {1:2}, {0}, (9,)]
print(all(these_are_True))





""" template below for import math """
import math
# PLEASE remember to put this in first line of code (if used)
# on Openjudge, DON'T import if unused, may raise Error
# help(math) will show eveything, below is what I found good to know

# ceil, floor, int
print(math.ceil(1.123))    #  2
print(math.ceil(-1.123))   # -1
print(math.floor(1.123))   #  1
print(math.floor(-1.123))  # -2
# int() just take what ever in front of '.'
print(int(1.123))     # 1
print(int(-1.123))    # -1, different with math.floor(-1.123)

# some constant
print(math.e)     # 2.718281828459045
print(math.pi)    # 3.141592653589793
print(math.inf)   # infinite, can put '-', as negative
print( math.inf == float('inf') )    # True

# n!, nCk, nPk
n, k = 4, 2
print(math.factorial(n))  # 4! = 24
print(math.comb(n, k))    # 4C2 = 6
print(math.perm(n, k))    # 4P2 = 12

# 19971: Combination, http://cs101.openjudge.cn/practice/19971/
# refer to code of GMyhf
import math
n_r = {}
for i in range(1001):
    n_r[i] = math.factorial(i)
def nCr(n:int, r:int):
    return n_r[n] // n_r[r] // n_r[n-r]
ans = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans.append(nCr(b, a))
print('\n'.join(map(str, ans)))

# various kind of log, all return float type
print(math.log(math.e))       # default base e
print(math.log(49, 7))        # set base to 7
print(math.log2(8))           # base 2
print(math.log10(10000))      # base 10

# others
array = [5, 3, 4, 6]
print(math.prod(array))              # 1*5*3*4*6 = 360
print(math.prod(array, start=2))     # 2*5*3*4*6 = 720
print(math.prod(array, start=0.1))   # 0.1*5*3*4*6 = 36.0

print(math.gcd(6, 8))    # 2
print(math.gcd(6, 9))    # 3
print(math.gcd(3, 7))    # 1
# gcd(x, y) == gcd(y, x)
# 03248: greatest common divisor, http://cs101.openjudge.cn/practice/03248/

# creating a lcm using gcd (need to import math):
def lcm(x:int, y:int): return x*y // math.gcd(x, y)





""" template below for other examples """

# 02707: solve quadractic equation, http://cs101.openjudge.cn/practice/02707/
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



# 12065: solve equation, http://cs101.openjudge.cn/practice/12065/
def f(x): return x**3 - 5*x**2 + 10*x - 80    # original equation
def f1(x): return 3*x**2 - 10*x + 10          # derivative function
x, xn = 0, 1
while abs(x-xn) > 1e-10:
    xn = x
    x = x - f(x)/f1(x)
print('%.9f'%x)



# 18155: combination multiply, http://cs101.openjudge.cn/practice/18155/
# refer to code of WenGang 2018-fallcs101, brute force with special import
from functools import reduce
from itertools import combinations
t = int(input())
s = [*map(int, input().split())]
multiply = []
for i in range(1, len(s) +1):
    for j in combinations(s, i):
        multiply.append(reduce(lambda x, y : x*y, j))
if t in multiply:
    print('YES')
else:
    print('NO')
# this can be solved by dfs too



# 21532: math password, http://cs101.openjudge.cn/practice/21532/
n = int(input())
for i in range(6, n+1):
    if n%i == 0:
        print(n//i)
        break