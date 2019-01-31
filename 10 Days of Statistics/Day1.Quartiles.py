# Enter your code here. Read input from STDIN. Print output to STDOUT
N0 = int(input())
X = [int(x) for x in input().split(' ')]


def median(array):
    N = len(array)
    if N % 2 == 0:
        med = (array[int(N/2-1)] + array[int(N/2)]) / 2
    else:
        med = array[int((N-1)/2)]
    return med

sortedArray = sorted(X)
if N0 % 2 == 0:
    Q1 = median(sortedArray[:int(N0/2)])
    Q3 = median(sortedArray[int(N0/2):])
else:
    Q1 = median(sortedArray[:int((N0-1)/2)])
    Q3 = median(sortedArray[int((N0+1)/2):])

Q2 = median(sortedArray)
print(int(Q1))
print(int(Q2))
print(int(Q3))