# Delete these comments for submission:
# can't use str or * or anything related to string
# eg. print(*(list(range(1,i+1))+list(range(1,i+1))[-2::-1]),sep='')
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i -1)//9)**2)