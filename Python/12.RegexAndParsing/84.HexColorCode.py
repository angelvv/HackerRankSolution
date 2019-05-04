# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    a = re.findall(r'(?<!^)(#(?:[a-f\d]{3,6}))\W', input(), flags=re.I)
    if a:
        print('\n'.join(a))

#(?<!^) not capturing the start of line
