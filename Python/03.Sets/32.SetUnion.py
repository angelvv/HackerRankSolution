# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
A = set(input().split())
m = input()
B = set(input().split())
print(len(A|B))
