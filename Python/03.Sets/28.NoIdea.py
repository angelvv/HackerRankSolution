# Enter your code here. Read input from STDIN. Print output to STDOUT
m,n = list(map(int, input().split(' ')))
Array = input().split() # don't convert to set
A = set(input().split())
B = set(input().split())

print(sum((i in A) - (i in B) for i in Array))

# duplicate in Array should be count multiplt times, don't use intersection
