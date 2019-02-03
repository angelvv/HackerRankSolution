# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean = float(input())
k = int(input())
def poisson(k,mean):
    p = mean**k * math.e**(-mean) /math.factorial(k)
    return(round(p,3))

print(poisson(k,mean))