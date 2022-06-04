# -*- coding: utf-8 -*-

def fib(n):
    if n<3: return 1
    memo = [1,1]+[0]*(n-2)
    for i in range(2,n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n-1]
print(fib(int(input())+1))


"""info    # AC
FINAL EXAM on 2021.12.23 (Thu)



"""