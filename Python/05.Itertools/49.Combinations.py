# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
word,n = input().split()
word = sorted(word) #automatically convert HACK to list then sort ['A','C','H','K']
n = int(n)
for i in range(1,n+1):
    print(*[''.join(x) for x in combinations(word,i)], sep = '\n')
