# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
N = input()
l = input().split()
sizeDict = Counter(l)

sale = 0
for _ in range(int(input())):
    size,price = input().split()
    if sizeDict[size] > 0:
        sale += int(price)
        sizeDict[size] -= 1
print(sale)