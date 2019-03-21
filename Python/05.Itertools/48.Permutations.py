# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
word,n = input().split()
#word = sorted(list(word)) 
word = sorted(word) #automatically convert HACK to list then sort ['A','C','H','K']
n = int(n)
print(*[''.join(x) for x in permutations(word, n)],sep='\n')
