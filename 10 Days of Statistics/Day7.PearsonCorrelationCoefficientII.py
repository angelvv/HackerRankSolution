# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
x = [float(x) for x in input().split()]
y = [float(x) for x in input().split()]

xindex = [(sorted(x).index(k))+1 for k in x]
yindex = [(sorted(y).index(k))+1 for k in y]

# to handle repeated entries
#xindex = [(sorted(x).index(k))+1 for j in x for k in sorted(x) if j ==k]
#yindex = [(sorted(y).index(k))+1 for j in y for k in sorted(y) if j ==k]

diff = sum([(x-y)**2 for x, y in zip(xindex, yindex)])
print(round(1- (6*diff)/(n*(n**2-1)), 3))


"""
N = int(input())
X = [float(x) for x in input().split()]
Y = [float(x) for x in input().split()]

def rank_simple(vector):
    vectorI = vector.sort()
    index = [vectorI.index(vector[i]) for i in range(len(vector))]
    return index
    # from online, doesn't work
    #return [vector.index(x) for x in sorted(range(len(vector)), key=vector.__getitem__)]
    #sorted(range(len(vector)), key=vector.__getitem__)
print(X)
print(Y)
rankX = rank_simple(X)
print(rankX)
rankY = rank_simple(Y)
print(rankY)
R = 1 - 6*sum((rankX[i] - rankY[i])**2 for i in range(len(X))) / (N*(N**-1))

print('%0.3f' %R) 
"""