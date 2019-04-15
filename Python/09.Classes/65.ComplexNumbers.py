import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary        

    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary+no.imaginary)

    def __sub__(self, no):
        return Complex(self.real-no.real, self.imaginary-no.imaginary)

    def __mul__(self, no):
        return Complex(self.real*no.real-self.imaginary*no.imaginary, self.real*no.imaginary + self.imaginary*no.real)

    def __truediv__(self, no):
        try: 
            return self.__mul__(Complex(no.real, -1*no.imaginary)).__mul__(Complex(1.0/(no.mod().real)**2, 0))
        except ZeroDivisionError as e:
            print(e)
            return None
    
    def mod(self):
        return Complex(pow(self.real**2+self.imaginary**2, 0.5), 0)

    def __str__(self):
        return '{0:.2f}{1:+.2f}i'.format(self.real, self.imaginary)
        # 0,1 are index of input
        
""" Alternatively use built in function:
class Complex(complex):
    def mod(self):
        return abs(self)
"""

if __name__ == '__main__':