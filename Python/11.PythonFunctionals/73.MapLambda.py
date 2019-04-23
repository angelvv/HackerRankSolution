cube = lambda x:x**3 # complete the lambda function 
""" Alternative less elegent solution
def fibhelper(n):
    if n == 1:
        F = 0
    elif n == 2:
        F = 1
    else:
        F = fibhelper(n-1) + fibhelper(n-2)
    return F

def fibonacci(n):
    # return a list of fibonacci numbers
    lst = []
    lst = [fibhelper(i+1) for i in range(n)]
    return lst
"""

def fibonacci(n):
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[-1] + lis[-2])
     return(lis[0:n])


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))