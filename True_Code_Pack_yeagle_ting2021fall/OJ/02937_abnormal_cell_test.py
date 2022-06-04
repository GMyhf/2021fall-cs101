# -*- coding: utf-8 -*-
n = int(input())
cell = [[*map(int, input().split())] for _ in range(n)]
ans=0
for i in range(1,n-1):
    for j in range(1,n-1):
        xx = cell[i][j]
        up = cell[i-1][j] -xx
        do = cell[i+1][j] -xx
        le = cell[i][j-1] -xx
        ri = cell[i][j+1] -xx
        if all((up>49, do>49, le>49, ri>49)):
            ans += 1
print(ans)

"""info
Created on Mon Nov 22 22:55:49 2021
@author: Asus
http://cs101.openjudge.cn/practice/02937/
02937:异常细胞检测
总时间限制: 1000ms 内存限制: 65536kB
描述
我们拍摄的一张CT照片用一个二维数组来存储，假设数组中的每个点代表一个细胞。每个细胞的颜色用0到255之间（包括0和255）的一个整数表示。我们定义一个细胞是异常细胞，如果这个细胞的颜色值比它上下左右4个细胞的颜色值都小50以上（包括50）。数组边缘上的细胞我们不检测。现在我们的任务是，给定一个存储CT照片的二维数组，写程序统计照片中异常细胞的数目。
输入
第一行包含一个整数N（100>=N>2）.
下面有 N 行，每行有 N 个0~255之间的整数，整数之间用空格隔开。
输出
输出只有一行，包含一个整数，为异常细胞的数目。
样例输入
4
70 70 70 70
70 10 70 70
70 70 20 70
70 70 70 70 
样例输出
2
"""