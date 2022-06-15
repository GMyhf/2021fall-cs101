"""
algorithm_analysis.py

updated on Jun. 15, 2022 by Hongfei Yan


Description:

A utility program to plot algorithmic time complexity of a function.

Author: Mahesh Venkitachalam

Website: electronut.in
http://electronut.in/plotting-algorithmic-time-complexity-of-a-function-using-python/
"""
 
import matplotlib.pyplot as plt
#import numpy as np
import timeit
import math
from functools import partial
import random
 

def Constant(N):
    """
    O(1) function
    """
    _ = 1

def Logarithmic(N):
    _ = [i for i in range( int(math.log2(N)) )]
 
def Linear(N):
    """
    O(n) function
    """
    _ = [i for i in range(N)]

def N_Log_N(N):
	_ = [i for i in range(N* int(math.log2(N)))]
    #for i in range(N)
    #    for i in range( int(math.log2(N)) )
    #        x = 1
 
def Quadratic(N):
	"""
	O(n^2) function
	"""
	_ = [i for i in range(int(math.pow(N, 2)))]
    #for i in range(N):
	#	for j in range(N):
	#		x = 1
 
def Cubic(N):
	"""
	O(n^3) function
	"""
	_ = [i for i in range(int(math.pow(N, 3)))]
    
	#for i in range(N):
	#	for j in range(N):
	#		for k in range(N):
	#			x = 1


def Exponential(N):
	_ = [i for i in range(int(math.pow(2, N)))]

def fshuffle(N):
    # O(N)
    random.shuffle(list(range(N)))
 
def fsort(N):
    x = list(range(N))
    random.shuffle(x)
    x.sort()
 
def plotTC(fn, nMin, nMax, nInc, nTests):
    """
    Run timer and plot time complexity
    """
    x = []
    y = []
    for i in range(nMin, nMax, nInc):
        N = i
        testNTimer = timeit.Timer(partial(fn, N))
        t = testNTimer.timeit(number=nTests)
        x.append(i)
        y.append(math.log2(t))

    #plt.plot(x, y, 'o', label=fn.__name__)
    plt.plot(x, y, label=fn.__name__)
    #plt.scatter(x, y)
    #plt.text(x, y, fn.__name__)

    #plt.scatter(x, y, label=fn.__name__)
    plt.legend(loc='best')
 

def main():
    print('Analyzing Algorithms...')
 
    upbound = 100
    step = 1
    seven_functions = [Constant,Logarithmic,Linear,N_Log_N,Quadratic,Cubic,Exponential]
    for i in seven_functions[:-1]:  # skip Exponential due to too expensive
        plotTC(i, 10, upbound, step, 10)
    
    '''
    plotTC(Constant, 10, upbound, step, 10)
    plotTC(Logarithmic, 10, upbound, step, 10)
    plotTC(Linear, 10, upbound, step, 10)
    plotTC(N_Log_N, 10, upbound, step, 10)
    plotTC(Quadratic, 10, upbound, step, 10)
    plotTC(Cubic, 10, upbound, step, 10)
    plotTC(Exponential, 10, upbound, step, 10)
    '''
    #plotTC(fshuffle, 10, 1000, 1000, 10)
    #plotTC(fsort, 10, 1000, 10, 10)
 
    plt.title("Seven Important Functions")
    plt.show()
 
# call main
if __name__ == '__main__':
    main()