def swap_case(s):
    string = ''
    for n,letter in enumerate(s):
        if letter == letter.upper():
            string = string + letter.lower()
            #s[n] = letter.lower() # string is immutable
        elif letter == letter.lower():
            string = string + letter.upper()
    return string
    #return s.swapcase() # Python already has this function

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)