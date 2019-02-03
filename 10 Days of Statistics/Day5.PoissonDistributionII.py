# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
meanA, meanB = [float(x) for x in input().split(" ")]

#E(C) = E(160+40X**2)
#    = 160+40*E(X**2)
#    = 160+40*(Var(X) + E(X)**2)
#    = 160+40*(meanA + meanA**2)


costA = 160 + 40*(meanA + meanA**2)
costB = 128 + 40*(meanB + meanB**2)

print('{:0.3f}'.format(costA))
print('{:0.3f}'.format(costB))

#round would not add 0 at the end to make it 3 decimal
#print(round(costA,3))
#print(round(costB,3))