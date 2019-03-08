import string

def print_rangoli(size):
    # your code goes here
    alist = string.ascii_lowercase
    #a = ord('a') # get the ascii number
    #alist = list(map(chr, range(a, a+size)))
    L = []
    for i in range(size):
        sublist = alist[i:size]
        L.append('-'.join(sublist[::-1]+sublist[1:]).center(4*size-3, '-'))
    
    print(*L[::-1], sep = '\n')
    print(*L[1:], sep = '\n')


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)