# Enter your code here. Read input from STDIN. Print output to STDOUT
list = [int(input()) for _ in range(int(input()))]
import math
def isPrime(i):
    if i <= 1: # case 6,9
        return('Not prime')
    elif i == 2: # case 5
        return('Prime')

    for n in range(2,max(2,math.ceil(i**(1/2)))+1):
        if i%n == 0:
            return('Not prime')            
    return('Prime')

for i in list:
    print(isPrime(i))
