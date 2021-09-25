# CS101 Week 2 Questions and Answers

2021 fall, Complied by Hongfei Yan



## Q: why numbering should start at zero

2021/9/25 11:46

 工院-21-韩萱：为什么列表元素索引是实际位置减一这种明显有悖于日常逻辑的语法？

19-李卓然：其实 绝大部分编程语言里面 都是这样的，虽然有悖日常逻辑但是程序猿会比较喜欢。

TA-张以宁：从底层原理解释一下，在c语言里，数组在内存空间里用连续的一段空间存放（可以想象为一排格子），而数组名变量本质就是第一个格子的位置（地址），a[0]就是取第0个格子里的东西，即第1个元素，a[1]是取第0个，加上1个偏移量的格子位置，也就是存放的第2个元素。



https://www.howtogeek.com/149225/why-do-computers-count-from-zero/

<img src="https://tva1.sinaimg.cn/large/008i3skNly1gusv7uzx7uj60u00ymdk702.jpg" alt="image-20210925141318472" style="zoom: 50%;" />



<img src="https://tva1.sinaimg.cn/large/008i3skNly1gusv7zrknaj60w10u043t02.jpg" alt="image-20210925141427214" style="zoom: 33%;" />



## Q: 《从入门到实践》看到第几章才可以做作业

2021/9/25 08:49，21-物院-张瑜

A: 

针对零基础同学提醒：1）只需要基本语法掌握后（int, float, str, bool, dict, list, set，及if, for, while），2）就直接开始刷 Codeforces上面的题目。排序，从最简单的开始，刷60～100个。3）如果有问题，看题解，或者微信群里问。

<img src="https://tva1.sinaimg.cn/large/008i3skNly1gusv7iyzp7j60u00uadjr02.jpg" alt="image-20210925143603819" style="zoom: 33%;" />

运行原理需要看CSAP的第一章。内存结构图掌握就可以，分几个段，code segment, heap segment, stack segment。

<img src="https://tva1.sinaimg.cn/large/008i3skNly1gusv7ogz84j60u010644902.jpg" alt="image-20210925143741404" style="zoom: 50%;" />



21-工院-梁成锐：这本书里很多偏应用的例子，看完几个基本的语法其实就可以做题了。看了2到7章基本就可以。省时间的话每一章看看前几小节就可以。



## Q: 若列表a=b,为啥a.sort()会改变b的值啊？

2021/9/24 15:55，化学院-徐若涵

A:

19-信管-刘佳霖：
我理解的话因为a=b其实ab在程序内部指向的是同一个东西，其中一个变了另一个也会变化。想要不这样的话可以import copy b = copy.deepcopy(a)，这样ab就是指向无关的两个东西了。

唐浴歌-经济学院：
首先需要理解b=一个常数值的意义是什么。根据计算机系统的思维，其实是对这个程序而言，b能够调用一个存储器的值，这个值就是后面的常数。a=b是一个链接，也就是说a的值是b赋予的，那么a的值也是调用这个存储器的常数，赋予之后a、b暂时是绑定的，有一个共用的值。
		用数学理解就是，假设这个常数值是c，c→b，由于a=b，所以c→a。
		对于一个正常的全局运算比如a+=f(a)，或者sorted(a)，这里的意思其实是将右侧a的函数计算后return出来，创建了存储器的另外一个值了，假设是d，覆盖掉原来的a的值的地址，这样a就是一个新的a了，a的值是d→a。a、b不再有共用的值了。
		.sort()是直接编辑上述的c，因此c变了，依附于c的a、b都会变。

21-化院-胡天然：
这个是shallow copy。列表是一大堆指针组成的，你在b=a[:]的时候，只是复制了最外层的指针，而如果这些指针指向的变量本身亦是可变的，是不会被复制的。

<img src="https://tva1.sinaimg.cn/large/008i3skNly1gusv89lfuxj60ho0lnabn02.jpg" alt="image-20210925142608114" style="zoom: 50%;" />

​		也许画个图更清楚……

<img src="https://tva1.sinaimg.cn/large/008i3skNly1gusv8dsghej60u012sq7b02.jpg" alt="image-20210925142714789" style="zoom:50%;" />



​		顺便解释一下当你更改变量的值的时候，到底发生了什么。在这件事上python和c/c++之类的语言还是有一定区别的。

<img src="https://tva1.sinaimg.cn/large/008i3skNly1gusv8mnorzj612t0rs77o02.jpg" alt="image-20210925142743167" style="zoom:50%;" />



## Q：考试可以用numpy pandas sympy等高等常用库吗？

​		不能，OJ平台只有python内建标准库。

​		标准库的资料：build-in模块都可以用。查看方法，dir(__builtins__)



# 附录：

## [1]. 基本语法

![image-20210925143215927](https://tva1.sinaimg.cn/large/008i3skNly1gusv1d7xqjj612u0u0dpm02.jpg)

## [2]. 标准函数

Built-in Functions, https://docs.python.org/3/library/functions.html

<img src="https://tva1.sinaimg.cn/large/008i3skNly1gusv8xjy9wj61150u0gr002.jpg" alt="image-20210925143312039" style="zoom: 33%;" />