"""
S should consist of only lowercase and uppercase letters (no numbers or symbols).
S should end in s.
"""

Regex_Pattern = r'^[a-zA-Z]*s$'	# Do not delete 'r'.
# don't use \w because \w match numbers as well
import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())