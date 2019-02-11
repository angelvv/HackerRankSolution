#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    ms = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year <= 1917 and year % 4 == 0:
        ms[1] = 29
    elif year > 1918 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        ms[1] = 29
    elif year == 1918:
        ms[1] = 15 #14th-28th
    remain = 256
    for i,n in enumerate(ms):
        remain -= ms[i]
        if remain <= ms [i+1]:
            mm = i+2;
            dd = remain;
            return('%02d.%02d.%4d' %(dd,mm,year))

"""Or hard code it just for this day
def solve(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year%400 == 0) or ((year%4 ==0) & (year%100 != 0))):
        return '12.09.%s' %year
    else:
        return '13.09.%s' %year
"""



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
