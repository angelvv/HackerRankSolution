# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    s = input()
    print('YES' if re.match(r'[7-9]\d{9}$', s) else 'NO')
