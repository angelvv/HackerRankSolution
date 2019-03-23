# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
word, n = input().split()
word = sorted(word)
n = int(n)
print(*[''.join(x) for x in combinations_with_replacement(word,n)], sep='\n')
