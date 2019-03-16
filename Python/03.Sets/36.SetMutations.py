# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
A = set(map(int, input().split()))
for i in range(int(input())):
    eval('A.{}({})'.format(input().split()[0], set(map(int, input().split()))))

print(sum(A))