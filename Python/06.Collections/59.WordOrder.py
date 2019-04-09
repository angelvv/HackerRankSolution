# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = int(input())
d = OrderedDict()
for _ in range(N):
    item = input()
    d[item] = d.get(item, 0) + 1
    """
    if item in d:
        d[item] += 1
    else:
        d[item] = 1
    """
print(len(d.items()))
print(*d.values())

""" Elegant alternative, combine Counter and OrderedDict
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
"""
# method resolution order (mro) https://stackoverflow.com/questions/35446015/how-ordered-counter-recipe-works/35448557#35448557