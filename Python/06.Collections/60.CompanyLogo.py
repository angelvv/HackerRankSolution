#!/bin/python3

import math
import os
import random
import re
import sys
import operator

if __name__ == '__main__':
    from collections import Counter
    d = Counter(sorted(input())) # to make sure alphabetical
    [print(*each) for each in d.most_common(3)]