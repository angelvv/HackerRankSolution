# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = [int(x) for x in input().split(' ')]

mean = sum(X)/N
variance = sum([((x-mean)**2) for x in X])

"""Alternatively
variance = 0
for i in range(N):
    variance += (X[i]-mean)**2
"""

std = round((variance/N)**0.5,1)

print(std)
