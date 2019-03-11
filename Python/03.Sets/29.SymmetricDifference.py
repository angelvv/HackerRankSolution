# Enter your code here. Read input from STDIN. Print output to STDOUT
m = input()
M = set(map(int, input().split()))
n = input()
N = set(map(int, input().split()))

print(*sorted(M.union(N) - M.intersection(N)), sep='\n')
