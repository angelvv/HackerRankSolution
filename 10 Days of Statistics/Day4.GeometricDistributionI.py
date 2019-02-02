# Enter your code here. Read input from STDIN. Print output to STDOUT
num, denom = [int(x) for x in input().split()]
p = num/denom
N = int(input())

def geometric(p,n):
    return((p-1)**(n-1) * p)

pFirstDefect = geometric(p, N)
print(round(pFirstDefect,3))
