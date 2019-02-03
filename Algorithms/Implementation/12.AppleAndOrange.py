#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum(s <= (a + x) <= t for x in apples))
    print(sum(s <= (b + x) <= t for x in oranges))

    """ For unknown reason, this only passes testcase 0, but fails testcase 1-11
    print(len([x for x in apples if s <= (x+a) <= t ])) # can do s<=x+a<=t for shorter list
    print(len([x for x in oranges if s <= (x+a) <= t ]))
    """
    """Less elegant solution
    appleLocs = [a + x for x in apples]
    orangesLocs = [b + x for x in oranges]
    appleCount = 0
    orangeCount = 0
    for i in appleLocs:
        if i>=s and i<=t:
            appleCount += 1
    for i in orangesLocs:
        if i>=s and i<=t:
            orangeCount += 1

    print(appleCount)
    print(orangeCount)
    """

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
