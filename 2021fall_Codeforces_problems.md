



# Problems in Codeforces.com

2021 fall, Complied by Hongfei Yan

**How to find the problems?**
Visit http://codeforces.com/, click 'PROBLEMSET', then click green checkmark (order=BY_SOLVED_DESC). That is, click http://codeforces.com/problemset?order=BY_SOLVED_DESC.

**What is Codeforces? What kind of a site/resource is it?**
Codeforces is a project joining people interested in and taking part in programming contests. On one hand, Codeforces is a social network dedicated to programming and programming contests. On the other hand, it is a platform where contests are held regularly, the participant's skills are reflected by their rating and the former contests can be used to prepare. 



如果想查看某个题目的其他人提交的代码，例如查看580C 可以访问

http://codeforces.com/problemset/status/580/problem/C

# Basic Programming Exercises

#. title, algorithm, difficulty, link

## 10A. Power Consumption Calculation

Implementation, 900, https://codeforces.com/problemset/problem/10/A

****

Tom is interested in power consumption of his favourite laptop. His laptop has three modes. In normal mode laptop consumes P~1~ watt per minute. T~1~ minutes after Tom moved the mouse or touched the keyboard for the last time, a screensaver starts and power consumption changes to P~2~ watt per minute. Finally, after T~2~ minutes from the start of the screensaver, laptop switches to the "sleep" mode and consumes P~3~ watt per minute. If Tom moves the mouse or touches the keyboard when the laptop is in the second or in the third mode, it switches to the first (normal) mode. Tom's work with the laptop can be divided into *n* time periods [l~1~, r~1~], [l~2~, r~2~], ..., [l~n~, r~n~]. During each interval Tom continuously moves the mouse and presses buttons on the keyboard. Between the periods Tom stays away from the laptop. Find out the total amount of power consumed by the laptop during the period [l~1~, r~n~].

**Input**

The first line contains 6 integer numbers *n*, P~1~, P~2~, P~3~, T~1~, T~2~ (1 ≤ *n* ≤ 100, 0 ≤ P~1~, P~2~, P~3~ ≤ 100, 1 ≤ T~1~, T~2~ ≤ 60). The following *n*lines contain description of Tom's work. Each *i*-th of these lines contains two space-separated integers l~i~ and r~i~ (0 ≤ l~i~ < r~i~ ≤ 1440, r~i~ < l~i~ + 1 for *i* < *n*), which stand for the start and the end of the *i*-th period of work.

**Output**

Output the answer to the problem.

**Examples**

input

```
1 3 2 1 5 10
0 10
```

output

```
30
```

input

```
2 8 4 2 5 10
20 30
50 100
```

output

```
570
```



```Python
n,p1,p2,p3,t1,t2 = map(int, input().split())
 
tp = []     # time periods
for _ in range(n):
    tp.append([int(x) for x in input().split()])
 
res = 0
 
for i in range(len(tp)-1):
    res += p1*(tp[i][1] - tp[i][0])
    if (tp[i+1][0] - tp[i][1]) <= t1:
        res += p1*(tp[i+1][0] - tp[i][1])
        continue
    else:
        res += p1*t1
        tmp = tp[i+1][0] - tp[i][1] - t1
        if tmp <= t2:
            res += p2*tmp
            continue
        else:
            res += p2*t2
            tmp = tmp - t2
            res += p3*tmp
 
res += p1*(tp[-1][1] - tp[-1][0])
 
print(res) 
```



## 266B. Queue at the School

Constructive algorithm, graph matchings, implementation, shortest paths, 800, https://codeforces.com/problemset/problem/266/B


During the break the schoolchildren, boys and girls, formed a queue of *n* people in the canteen. Initially the children stood in the order they entered the canteen. However, after a while the boys started feeling awkward for standing in front of the girls in the queue and they started letting the girls move forward each second. 

Let's describe the process more precisely. Let's say that the positions in the queue are sequentially numbered by integers from 1 to *n*, at that the person in the position number 1 is served first. Then, if at time *x* a boy stands on the *i*-th position and a girl stands on the (*i* + 1)-th position, then at time *x* + 1 the *i*-th position will have a girl and the (*i* + 1)-th position will have a boy. The time is given in seconds.

You've got the initial position of the children, at the initial moment of time. Determine the way the queue is going to look after *t* seconds.

**Input**

The first line contains two integers *n* and *t* (1 ≤ *n*, *t* ≤ 50), which represent the number of children in the queue and the time after which the queue will transform into the arrangement you need to find. 

The next line contains string *s*, which represents the schoolchildren's initial arrangement. If the *i*-th position in the queue contains a boy, then the *i*-th character of string *s* equals "B", otherwise the *i*-th character equals "G".

**Output**

Print string *a*, which describes the arrangement after *t* seconds. If the *i*-th position has a boy after the needed time, then the *i*-th character *a* must equal "B", otherwise it must equal "G".

**Examples**

input

```
5 1
BGGBG
```

output

```
GBGGB
```

input

```
5 2
BGGBG
```

output

```
GGBGB
```

input

```
4 1
GGGB
```

output

```
GGGB
```



```Python
n,t = map(int, input().split())
lis = list(input())
 
while t>0:
    j = 0
    while j < n-1:
        if lis[j]=='B' and lis[j+1]=='G':
            lis[j], lis[j+1] = 'G', 'B'
            j += 1
        j += 1
        
    t -= 1
    
print(''.join(lis))
```



# OPTIONAL PROBLEMS



## 14xxA. Xxx

games, greedy, 1400, https://codeforces.com/problemset/problem/1425/A

Lately, Mr. Chanek frequently plays the game **Arena of Greed**. As the name implies, the game's goal is to find the greediest of them all, who will then be crowned king of Compfestnesia.

Both players will try to maximize the number of coins they have. Mr. Chanek asks your help to find the maximum number of coins he can get at the end of the game if both he and the opponent plays optimally.

**Input**

The first line contains a single integer T (1≤T≤10^5^) denotes the number of test cases.

The next T lines each contain a single integer N (1≤N≤10^18^).

**Output**

T lines, each line is the answer requested by Mr. Chanek.

Example

input

```
2
5
6
```

output

```
2
4
```



2021fall-cs101，xxx。

解题思路：简单。

```python
 
coins = []
for _ in range(int(input())):
    coins.append(int(input()))
 
for i in coins:
    if i==1:
        ans.append(1)
        #print(1)
    else:
        solve(i)
 
print('\n'.join(map(str, ans)))
```







# References:

[1]. Hongfei Yan, 2020fall_Codeforces_problems.pdf

[2]. PKU-cs101 student assignments, fall 2021.

[3]. https://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/
