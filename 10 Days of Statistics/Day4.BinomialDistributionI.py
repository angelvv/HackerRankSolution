# Enter your code here. Read input from STDIN. Print output to STDOUT
boy,girl = list(map(float, input().split())) # or =[float(x) for x in input().split()]
pBoy = boy/(boy+girl)

# hard code calculation
p0Boy = (1-pBoy)**6
p1Boy = 6 * pBoy * (1-pBoy)**5
p2Boy = 6*5/2 * (pBoy**2) * ((1-pBoy)**4)
pAtLeast3Boy = 1 - p0Boy - p1Boy - p2Boy

"""#Alternatively
def factorial(n):
    return 1 if n==0 else n * factorial(n-1)

def nChoosek(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

def binomial(n, k, p):
    return nChoosek(n, k) * (p**k) * ((1 - p)**(n - k))

pAtLeast3Boy = 1 - binomial(6, 0, pBoy) - binomial(6, 1, pBoy) - binomial(6, 2, pBoy)
"""

print(round(pAtLeast3Boy,3))
