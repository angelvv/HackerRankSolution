regex_pattern = r"^.{3}\..{3}\..{3}\..{3}$"	# Do not delete 'r'.
# instruction should add: string should contain nothing else in the beginning and at the end

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())