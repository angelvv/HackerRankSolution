# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for _ in range(int(input())):
    eval('d.{}({})'.format(*input().split()+['']))
    #inp=input().split()
    #getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
print(*d)