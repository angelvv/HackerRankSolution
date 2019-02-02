# Enter your code here. Read input from STDIN. Print output to STDOUT
num, denom = [int(x) for x in input().split()]
p = num/denom
N = int(input())

p0Defect = (1-p)**N
pDefect = 1 - p0Defect
print(round(pDefect, 3))
