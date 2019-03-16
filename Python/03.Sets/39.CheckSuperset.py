# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
N = int(input())
B = set(input().split())
C = set(input().split())
# '>' checks if A is a strict superset, can also use B.issuperset(A)
print(all([A > B, A > C]))
