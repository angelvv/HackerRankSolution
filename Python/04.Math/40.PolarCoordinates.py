# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
num = complex(input())
print(abs(num))
print(cmath.phase(num))

# or one-liner
#print(*cmath.polar(complex(input())), sep='\n')