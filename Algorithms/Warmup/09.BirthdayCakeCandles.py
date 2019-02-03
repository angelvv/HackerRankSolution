#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    ar.sort(reverse=True) #large to small
    maxv = ar[0]
    count = 0
    for i in ar:
        if i == maxv:
            count += 1
    return(count)

#    return(len([i for i in ar if i==max(ar)])) # failed case 4 b/c of runtime, can't handle n>1000

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
