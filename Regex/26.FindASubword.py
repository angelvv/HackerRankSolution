# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lines = '\n'.join(input() for _ in range(int(input()))) # has to be joined into one entry
queries = [input() for _ in range(int(input()))]
for query in queries:
    print(len(re.findall(r'\w(%s)\w' % query, lines))) # use string formating to reference variable
