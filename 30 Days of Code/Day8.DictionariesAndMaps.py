# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
"""
phoneBook = dict()
for i in range(N):
    key, value = input().split(" ")
    phoneBook[key] = value
"""
# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
phoneBook = dict(input().split() for _ in range(N))
"""
#Alternatively, using dictionary comprehension
name_numbers = [input().split() for _ in range(n)]
phoneBook = {k:v for k,v in name_numbers}
"""
while (1):
    try: #don't know how many queries are there
        key = input()
        if key in phoneBook:
            print(key+'='+phoneBook[key])
        else:
            print('Not found')
    except:
        break
