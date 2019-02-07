#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    n2 =[]
    count=0
    maxCount=0
    while n > 0:
        n2.insert(0,n%2)
        if n%2 == 1:
            count+=1
            n-=1
            if count > maxCount:
                maxCount = count
        else:
            count=0
        n=n/2
    print(maxCount)