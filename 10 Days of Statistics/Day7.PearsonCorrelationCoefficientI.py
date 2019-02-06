# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
N = int(input())
X = [float(x) for x in input().split()]
Y = [float(x) for x in input().split()]

def meanstd(list):
    N = len(list)
    mean = sum(list)/N
    std  = (sum([(i - mean)**2 for i in list]) / N)**0.5
    return mean, std

meanX, stdX = meanstd(X)
meanY, stdY = meanstd(Y)

covariance = sum([(X[i]-meanX)*(Y[i]-meanY) for i in range(N)])/N
pearsonCorr = covariance / (stdX*stdY)

print('%0.3f' %pearsonCorr)