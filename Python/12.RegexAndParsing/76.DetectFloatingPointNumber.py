# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern = r'^[+-]?[0-9]*\.[0-9]+$'
for _ in range(int(input())):
    a = input()
    try:
        float(a)
        print(bool(re.search(pattern, a)))
    except:
        print('False')
    
