#!/bin/python3

import re
import sys


# regular expression practice https://rubular.com/r/UAgzl9NxQv

if __name__ == '__main__':
    N = int(input())

    """ # Use regular expression
    emails = [input().split() for _ in range(N)]
    names = sorted(entry[0] for entry in emails if re.search('@gmail\.com$', entry[1]))
    print(*names, sep='\n') # print with newline separator
    """

# Alternatively, use endswith
    names = []
    for _ in range(N):
        entry = input().split(' ')
        if entry[1].endswith('@gmail.com'):
            names.append(entry[0])
    print(*sorted(names), sep='\n')
