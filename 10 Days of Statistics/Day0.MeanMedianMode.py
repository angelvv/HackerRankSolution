# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
rawData = input()
array = [int(elem) for elem in rawData.split(' ')]

# mean
mean = sum(array)/N

# median
sortedArray = sorted(array)
if N % 2 == 0:
    median = (sortedArray[int(N/2-1)] + sortedArray[int(N/2)]) / 2
else:
    median = sortedArray[int((N-1)/2)]

# mode
mode = max(sorted(set(array)), key=sortedArray.count) #set doesn't keep the original order
# get the element with max count (ie.key) in an array

""" Alternatively, use a dictionary as a hash table
myDict = dict()
maxCount, maxCountElem = 0, 0
for elem in sortedArray:
    if elem in myDict.keys():
        myDict[elem] += 1
    else:
        myDict[elem] = 1
    if myDict[elem] > maxCount:
        maxCount = myDict[elem]
        maxCountElem = elem
mode = maxCountElem
"""

# print outputs
print(round(mean,1))
print(round(median,1))
print(mode)
