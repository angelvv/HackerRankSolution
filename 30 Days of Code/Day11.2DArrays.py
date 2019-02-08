#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    maxGlass = []# maxGlass=0 doesn't work for negative values
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            hourGlass = sum(arr[i][j:j+3]) +\
             arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            maxGlass.append(hourGlass)

    print(max(maxGlass))
"""
# oneliner:
    a = arr
    print(max(a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2] for i in range(4) for j in range(4)))
"""