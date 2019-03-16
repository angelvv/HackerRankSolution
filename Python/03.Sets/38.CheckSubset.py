# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    nA, A = [input(), set(input().split())]
    nB, B = [input(), set(input().split())]
    print(A.issubset(B))