# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    name, url = input().split(' ')
    if re.match(r'<[a-z][a-z_\d\.-]+@[a-z]+\.[a-z]{1,3}>', url, re.I):
        print(name, url)
# if put _ after -, it means to exclude _