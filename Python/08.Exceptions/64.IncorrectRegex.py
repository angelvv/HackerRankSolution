# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    l = input()
    try:
        re.compile(l)
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
