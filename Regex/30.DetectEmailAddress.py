# Enter your code here. Read input from STDIN. Print output to STDOUT
""" email address format
1. It should be of format : <local-part>@<domain-part>
2. Local-part can contain Alphanumeric-character or .(dot)
3. Domain-part can contain Alphanumeric-character or .(dot)
"""

import re
lines = '\n'.join(input() for _ in range(int(input())))
pattern = r'[\w\.]+@\w+(?:\.\w+)+' # ?: signify non-capturing group
print(';'.join(sorted(set(re.findall(pattern, lines)))))
