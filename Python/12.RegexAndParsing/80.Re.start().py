# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
p = input()
m = list(re.finditer(r'(?=(%s))' %p, s))

if m:
    print(*[(a.start(1),a.end(1)-1) for a in m],sep = '\n')
else:
    print('(-1, -1)')
