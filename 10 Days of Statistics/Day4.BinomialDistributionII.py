# Enter your code here. Read input from STDIN. Print output to STDOUT
p, n = list(map(float, input().split())) # or =[float(x) for x in input().split()]
p = p/100

def factorial(n):
    return 1 if n==0 else n * factorial(n-1)

def nChoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def binomial(n, k, p):
    return nChoosek(n, k) * (p**k) * ((1 - p)**(n - k))

pNoMoreThan2 = binomial(n, 0, p) + binomial(n, 1, p) + binomial(n, 2, p)
pAtLeast2 = 1 - binomial(n, 0, p) - binomial(n, 1, p)
print(round(pNoMoreThan2, 3))
print(round(pAtLeast2, 3))