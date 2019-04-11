# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
lines = '\n'.join(input() for _ in range(int(input())))
pattern = r'https?:\/\/(?:www2?\.)?([\w\.\-]+\.[A-Za-z0-9]+)' # need to escape / (?:www\.)?
print(';'.join(sorted(set(re.findall(pattern, lines)))))