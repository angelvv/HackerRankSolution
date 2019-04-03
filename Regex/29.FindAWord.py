# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lines = '\n'.join(input() for _ in range(int(input())))
words = [input() for _ in range(int(input()))]
for word in words:
    print(len(re.findall(r'(?<![a-zA-Z_])%s(?![a-zA-Z_])' %word, lines)))
