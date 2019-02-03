# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
mean, std = [float(x) for x in input().split(" ")]
X1 = float(input())
threshold = float(input())

def cdf(mean,std,x):
    output = 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
    return(output)

A1 = (1 - cdf(mean,std,X1))*100
A2 = (1 - cdf(mean,std,threshold))*100
A3 = (cdf(mean,std,threshold))*100

print('{:0.2f}'.format(A1))
print('{:0.2f}'.format(A2))
print('{:0.2f}'.format(A3))