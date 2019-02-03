# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean, std = [float(x) for x in input().split()]
X1 = float(input())
X2, X3 = [float(x) for x in input().split()]

def cdf(mean,std,x):
    cdf = 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
    return(cdf)

A1 = cdf(mean,std,X1)
A2 = cdf(mean,std,X3) - cdf(mean,std,X2)
print('{:0.3f}'.format(A1))
print('{:0.3f}'.format(A2))
