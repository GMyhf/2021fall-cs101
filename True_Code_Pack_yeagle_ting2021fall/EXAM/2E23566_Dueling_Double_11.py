# -*- coding: utf-8 -*-
n, m = map(int, input().split())
total = 0
shop, sale = {}, {}
for _ in range(n):
    s, p = map(int, input().split())
    try: shop[s].append(p)
    except: shop[s] = [p]
    total += p
x = total//200
if x: total -= 30*x
for i in range(1, m+1):
    q, x = map(int, input().split('-'))
    sale[i] = (q, x)
for s in shop:
    if sum(shop[s]) >= sale[s][0]:
        total -= sale[s][1]
print(total)

"""info    # AC
FINAL EXAM on 2021.12.23 (Thu)
Sample Input1:
2 2
1 100
2 100
100-20
200-50

Sample Output1:
150


"""