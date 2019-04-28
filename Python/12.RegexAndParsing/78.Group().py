# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
m = re.search(r'([a-zA-Z0-9])\1',s) # doesn't include _ so \w doesn't work
print(m.group(1) if m else -1)
