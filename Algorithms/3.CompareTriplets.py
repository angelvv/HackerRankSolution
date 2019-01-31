#!/bin/python3
#Angel

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    aLarger = len([n for n in range(len(a)) if a[n]>b[n]])
    bLarger = len([n for n in range(len(a)) if a[n]<b[n]])
    return [aLarger, bLarger]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
