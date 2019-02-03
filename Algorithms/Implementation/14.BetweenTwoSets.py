#!/bin/python3

import os
import sys

#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    #
    # Write your code here.
    #
    maxA = max(a)
    minB = min(b)
    count = 0
    for number in range(maxA,minB+1):
        cond1 = all(number % A == 0 for A in a) #a list of boolean, all 1 to be 1
        cond2 = all(B % number == 0 for B in b)
        count += cond1*cond2
    return count

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
