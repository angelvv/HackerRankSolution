# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = [float(x) for x in input().split(' ')]
W = [float(x) for x in input().split(' ')]

WeightedSum = 0
for i, elem in enumerate(X):
    WeightedSum += elem * W[i]
WeightedMean = round(WeightedSum/sum(W),1)
print(WeightedMean)
