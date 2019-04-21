# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
l = list(map(int, input().split()))
print(all(x>0 for x in l) and any(int(str(x)[::-1])==x for x in l))
