def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    # Use Pyformat https://pyformat.info/
    for i in range(1,number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w))

    """
    # Use string method
    for i in range(1,number+1):
        print(str(i).rjust(w), str(oct(i)[2:]).rjust(w), str(hex(i)[2:].upper()).rjust(w), str              (bin(i)[2:]).rjust(w)) # don't need sep=' '
    """

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)