# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
A = list(map(int, input().split()))
print(int((sum(set(A))*K-sum(A)) / (K-1)))
