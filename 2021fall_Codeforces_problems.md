



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



## 208A. Dubstep

strings, 900, https://codeforces.com/problemset/problem/208/A

Vasya works as a DJ in the best Berland nightclub, and he often uses dubstep music in his performance. Recently, he has decided to take a couple of old songs and make dubstep remixes from them.

Let's assume that a song consists of some number of words. To make the dubstep remix of this song, Vasya inserts a certain number of words "WUB" before the first word of the song (the number may be zero), after the last word (the number may be zero), and between words (at least one between any pair of neighbouring words), and then the boy glues together all the words, including "WUB", in one string and plays the song at the club.

For example, a song with words "I AM X" can transform into a dubstep remix as "WUBWUBIWUBAMWUBWUBX" and cannot transform into "WUBWUBIAMWUBX".

Recently, Petya has heard Vasya's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Vasya remixed. Help Petya restore the original song.

**Input**

The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters. It is guaranteed that before Vasya remixed the song, no word contained substring "WUB" in it; Vasya didn't change the word order. It is also guaranteed that initially the song had at least one word.

**Output**

Print the words of the initial song that Vasya used to make a dubsteb remix. Separate the words with a space.

Examples

input

```
WUBWUBABCWUB
```

output

```
ABC 
```

input

```
WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB
```

output

```
WE ARE THE CHAMPIONS MY FRIEND 
```

Note

In the first sample: "WUBWUBABCWUB" = "WUB" + "WUB" + "ABC" + "WUB". That means that the song originally consisted of a single word "ABC", and all words "WUB" were added by Vasya.

In the second sample Vasya added a single word "WUB" between all neighbouring words, in the beginning and in the end, except for words "ARE" and "THE" — between them Vasya added two "WUB".

```python
# http://codeforces.com/problemset/problem/208/A

s = [ i for i in input().split('WUB') if i!='' ]
print(*s)

'''
Print a list of space-separated elements in Python 3
https://stackoverflow.com/questions/22556449/print-a-list-of-space-separated-elements-in-python-3

You can apply the list as separate arguments:

print(*L)
and let print() take care of converting each element to a string. 
You can, as always, control the separator by setting the sep keyword argument:

>>> L = [1, 2, 3, 4, 5]
>>> print(*L)
1 2 3 4 5
>>> print(*L, sep=', ')
1, 2, 3, 4, 5
>>> print(*L, sep=' -> ')
1 -> 2 -> 3 -> 4 -> 5

'''
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



## 363B. Fence

brute force, dp, 1100, https://codeforces.com/contest/363/problem/B

There is a fence in front of Polycarpus's home. The fence consists of *n* planks of the same width which go one after another from left to right. The height of the *i*-th plank is h~i~ meters, distinct planks can have distinct heights.

![image-20211022200233170](https://i.loli.net/2021/10/22/AVrthYwbugnWMzo.png)

​																Fence for *n* = 7 and *h* = [1, 2, 6, 1, 1, 7, 1]

Polycarpus has bought a posh piano and is thinking about how to get it into the house. In order to carry out his plan, he needs to take exactly *k* consecutive planks from the fence. Higher planks are harder to tear off the fence, so Polycarpus wants to find such *k* consecutive planks that the sum of their heights is minimal possible.

Write the program that finds the indexes of *k* consecutive planks with minimal total height. Pay attention, the fence is not around Polycarpus's home, it is in front of home (in other words, the fence isn't cyclic).

**Input**

The first line of the input contains integers *n* and *k* (1 ≤ *n* ≤ 1.5·10^5^, 1 ≤ *k* ≤ *n*) — the number of planks in the fence and the width of the hole for the piano. The second line contains the sequence of integers h~1~, *h*2, ..., h~n~ (1 ≤ h~i~ ≤ 100), where h~i~ is the height of the *i*-th plank of the fence.

**Output**

Print such integer *j* that the sum of the heights of planks *j*, *j* + 1, ..., *j* + *k* - 1 is the minimum possible. If there are multiple such *j*'s, print any of them.

**Examples**

input

```
7 3
1 2 6 1 1 7 1
```

output

```
3
```

Note

In the sample, your task is to find three consecutive planks with the minimum sum of heights. In the given case three planks with indexes 3, 4 and 5 have the required attribute, their total height is 8.



```python
n,k = map(int, input().split())
h = [int(x) for x in input().split()]
for i in range(1,n):
    h[i] += h[i-1] 
z = 0

m = k*100
h.append(0) 
for i in range(n-k+1):
    if m >= h[i+k-1] - h[i-1]:
        m = h[i+k-1] - h[i-1]
        z = i+1
        
print(z)
```







# References:

[1]. Hongfei Yan, 2020fall_Codeforces_problems.pdf

[2]. PKU-cs101 student assignments, fall 2021.

[3]. https://csrgxtu.github.io/2015/03/20/Writing-Mathematic-Fomulars-in-Markdown/
