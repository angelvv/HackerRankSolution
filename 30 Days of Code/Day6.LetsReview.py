# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
for i in range(N):
    S = input()
    print(S[::2] + ' ' + S[1::2])
    #print(S[::2], S[1::2]) #compilation error
