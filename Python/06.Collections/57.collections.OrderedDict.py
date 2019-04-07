# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.
from collections import OrderedDict
sale = OrderedDict()
for _ in range(int(input())):
    item,space,price = input().rpartition(' ') 
    # "rpartition" look for space from right side and split the string
    sale[item] = sale.get(item,0) + int(price)
    # "dict.get" If the key exists in the dict, then the value for that key is returned. If it does not exist, then the default value specified as the second argument to get() is returned. 
"""
for _ in range(int(input())):
    line = input().split()
    name,price = (' '.join(line[:-1]), int(line[-1]))
    if name in sale: sale[name] += price
    else: sale[name] = price
"""
for item in sale:
    print(item, sale[item])
