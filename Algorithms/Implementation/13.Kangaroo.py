#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (v1 > v2)*(x1 < x2) and (x2 - x1) % (v1 - v2) == 0:
        return 'YES'
    # 2nd condition is optional since the testcases all assume Kangaroo 2 starts further the right of Kangaroo 1, but I want to account for all situations here
    elif (v1 < v2)*(x1 > x2) and (x1 - x2) % (v2 - v1) == 0:
        return 'YES'
    else:
        return 'NO'
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
