"""
S consists of 8 digits.
S may have "" separator such that string  gets divided in  parts, with each part having exactly two digits. (Eg. 12-34-56-78)
"""

Regex_Pattern = r"^\d{2}(-?)\d{2}\1\d{2}\1\d{2}$"	# Do not delete 'r'.
# if there is first '-' then there has to be 2nd and 3rd '-'
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())