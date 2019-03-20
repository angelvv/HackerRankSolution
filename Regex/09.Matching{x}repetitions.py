"""
 must be of length equal to 45.
The first  characters should consist of letters(both lowercase and uppercase), or of even digits.
The last  characters should consist of odd digits or whitespace characters.
"""
Regex_Pattern = r'^[a-zA-Z02468]{40}[13579\s]{5}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())