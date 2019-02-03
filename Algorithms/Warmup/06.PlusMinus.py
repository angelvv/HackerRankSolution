#!/bin/python3

import math
import os
import random
import re
import sys
# from decimal import *

# Complete the plusMinus function below.
def plusMinus(arr):
    # getcontext().prec = 6
    length = len(arr)
    
    print("%.6f" % (sum(n>0 for n in arr)/length))
    print("%.6f" % (sum(n<0 for n in arr)/length))
    print("%.6f" % (sum(n==0 for n in arr)/length))
    #print(round(sum(n==0 for n in arr)/length,6)) # not work for 0.5 though

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
