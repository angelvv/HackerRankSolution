# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
limit, n, mean, std = [float(input()) for i in range(4)]

def cdf(mean,std,x):
    cdf = 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))
    return(cdf)

p = cdf(mean*n,std*(n**0.5),limit)
print('%0.4f' %p)
