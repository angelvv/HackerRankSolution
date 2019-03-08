def minion_game(string):
    # your code goes here    
    vowels = 'AEIOU'
    cCount = vCount = 0

    # Alternative elegent solution
    for i in range(len(string)):
        if string[i] in vowels:
            vCount += (len(string)-i)
        else:
            cCount += (len(string)-i)

    """ Failed testcase 4, also time out
    cList = [string[n:] for n, a in enumerate(string) if a not in vowels]
    vList = [string[n:] for n, a in enumerate(string) if a in vowels]
    cAll = []
    vAll = []

    for word in cList:
        for i in range(1,len(word)+1):
            cAll.append(word[:i])
    for word in vList:
        for i in range(1,len(word)+1):
            vAll.append(word[:i])
    cSet = set(cAll)
    vSet = set(vAll)
    
    for word in cSet:
        cCount += sum([1 for i in range(len(string)) if word==string[i:i+len(word)]])
    for word in vSet:
        vCount += sum([1 for i in range(len(string)) if word==string[i:i+len(word)]])
    """

    if cCount > vCount:
        print('Stuart', cCount)
    elif vCount > cCount:
        print('Kevin', vCount)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)