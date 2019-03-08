#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
"""
# Use built-in function
import string 
def solve(s):
    return(string.capwords(s, ' '))
"""

def solve(s):
    splitted = s.split(' ')
    capped = [word.capitalize() for word in splitted] # also correct
    #capped = [a[0].upper()+a[1:].lower() for a in splitted] # Only capitalize first letter, other letters should be lower case (testcase 1 failed)
    print(capped)
    return(' '.join(capped))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
