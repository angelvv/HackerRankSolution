from fractions import Fraction
from functools import reduce

# Note that inputs are Fraction objects
def product(fracs):
    #print(fracs) # [Fraction(1, 2), Fraction(3, 4), Fraction(5, 3)]
    t = reduce(lambda x,y: x*y, fracs)
    #print(t) # 5/8
    # complete this line with a reduce statement
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)