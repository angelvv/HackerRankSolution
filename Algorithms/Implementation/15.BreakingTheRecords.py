#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    minScore = maxScore = scores[0]
    minBreak = maxBreak = 0
    for score in scores[1:]:
        if score > maxScore:
            maxScore = score
            maxBreak += 1
        elif score < minScore:
            minScore = score
            minBreak += 1
    return maxBreak, minBreak

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
