# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
n, m = list(map(int, input().split()))

for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    item = input()
    if item in d: print(*d[item])
    else: print(-1)

""" Less elegant alternative
l = [input() for _ in range(n)]
lookup = [input() for _ in range(m)]
for ind, item in enumerate(l):
    d[item].append(ind+1)
for item in lookup:
    if d[item]: # another way to check if value exist
        print(*d[item])
    else:        
        print(-1)
"""