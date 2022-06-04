# -*- coding: utf-8 -*-
"""template info
@author: Asus - yeagle_ting
--- various classic problems
"""

# !!! recursion is calling function that calls itself, or using stack to treat data

# 02746:　josephus problem, http://cs101.openjudge.cn/practice/02746/
ans = []
def josephus(n, m):
    if n == 1: return 0
    return (josephus(n-1, m) +m) % n
while True:
    n, m = map(int, input().split())
    if n == 0: break
    ans.append(josephus(n, m)+1)
print('\n'.join(map(str, ans)))



# 02753: fibonacci_sequence, http://cs101.openjudge.cn/practice/02753/
def fib(n):
    if n<3: return 1
    memo = [1,1]+[0]*(n-2)
    for i in range(2,n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1]
ans = []
for _ in range(int(input())):
    ans.append(str(fib(int(input()))))
print('\n'.join(ans))

# build fibonacci upto biggest n, then do index (without def)
ns = [int(input()) for _ in range(int(input()))]
nx = max(ns) ; memo = [1,1]
if nx>2:
    memo += [0]*(nx-2)
    for i in range(2,nx):
        memo[i] = memo[i-1] + memo[i-2]
ans = [str(memo[n-1]) for n in ns]
print('\n'.join(ans))



# 04147: hanoi_problem, http://cs101.openjudge.cn/practice/04147/
# refer to GMyhf's code
def hanoi_print(disk, ori, new):
    print('%d:%s->%s'%(disk, ori, new))
def hanoi(n, ini, mid, end):
    if n == 1:
        hanoi_print(1, ini, end)
    else:
        hanoi(n-1, ini, end, mid)
        hanoi_print(n, ini, end)
        hanoi(n-1, mid, ini, end)
n, a, b, c = input().split()
hanoi(int(n), a, b, c)



# 02694: polish notation, http://cs101.openjudge.cn/practice/02694/
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



# 03704: bracket matching, http://cs101.openjudge.cn/practice/03704/
# using stack to 'mock recursion'
out = []
while True:
    try: line = input()
    except EOFError: break
    stack, check = [], []
    for i in range(len(line)):
        if line[i] == '(':
            stack.append(i)
            check += ' '
        elif line[i] == ')':
            if stack:
                check += ' '
                stack.pop()
            else:
                check += '?'
        else:
            check += ' '
    while stack:
        check[stack[-1]] = '$'
        stack.pop()
    out += [line, ''.join(check)]
print('\n'.join(out))