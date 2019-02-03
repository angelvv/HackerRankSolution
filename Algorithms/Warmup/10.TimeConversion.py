#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    hh, mm, ss = map(int, s[:-2].split(':'))
    pm = s[-2:]
    h = hh%12 + (pm == 'PM') * 12

    return(('%02d:%02d:%02d') % (h, mm, ss))    
    
    """Alternatively: note 12:30:00PM should output 12:30:00
    if int(s[:2]) == 12:
        if s[-2] == 'A':
            return('00:00:00')
        elif s[-2] == 'P':
            return('12:00:00')
    elif s[-2] == 'A':
        return s[:-2]
    elif s[-2] == 'P':
        return(str(int(s[:2])+12) + s[2:-2])
    """

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
