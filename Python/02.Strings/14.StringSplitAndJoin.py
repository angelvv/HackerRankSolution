def split_and_join(line):
    # write your code here
    return('-'.join(line.split()))
    # another way to do this
    #return(line.replace(" ","-"))
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)