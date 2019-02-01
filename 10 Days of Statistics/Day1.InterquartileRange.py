# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as st

n = int(input())
X = [int(x) for x in input().split()]
F = [int(x) for x in input().split()]

S = []
for i in range(n):
    S += [X[i]] * F[i]
N = sum(F)
S.sort()

if n%2 != 0:
    q1 = st.median(S[:N//2]) # floor division
    q3 = st.median(S[N//2+1:])
else:
    q1 = st.median(S[:N//2])
    q3 = st.median(S[N//2:])

interquartile = round(float(q3-q1), 1)
print(interquartile)