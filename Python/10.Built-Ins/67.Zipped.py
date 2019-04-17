# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = list(map(int,input().split()))
s = []
for _ in range(X):
    s.append(list(map(float, input().split())))
avg = [round(sum(x)/X,1) for x in zip(*s)]
print(*avg, sep='\n')
