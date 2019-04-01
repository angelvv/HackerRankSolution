"""
It must begin with either an underscore, _ (ASCII value 95), or a period, . (ASCII value 46).
The first character must be immediately followed by one or more digits in the range 0 through 9.
After some number of digits, there must be 0 or more English letters (uppercase and/or lowercase).
It may be terminated with an optional _ (ASCII value ). Note that if it's not terminated with an underscore, then there should be no characters after the sequence of 0 or more English letters.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r'^[_\.][0-9]+[a-zA-Z]*_?$'
lines = [input() for _ in range(int(input()))]
print('\n'.join('VALID' if re.search(pattern, line) else 'INVALID' for line in lines))

""" Alternative
for line in lines:
    if re.search(pattern, line):
        print('VALID')
    else:
        print('INVALID')
"""