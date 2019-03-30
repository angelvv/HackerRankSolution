# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

lines = [input() for _ in range(int(input()))]
pattern = r'<\s*(\w+)' # tag can be a number
searchGroup = []
for line in lines:
    searchObj = re.findall(pattern,line)
    searchGroup.extend(searchObj)
print(';'.join(sorted(set(searchGroup))))
