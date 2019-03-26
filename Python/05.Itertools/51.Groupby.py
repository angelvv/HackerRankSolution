# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
string = input()
print(*[(len(list(group)), int(letter)) for letter, group in groupby(string)], sep=' ')
# group is ['1'] ['2', '2', '2'] ['3'] ['1', '1']