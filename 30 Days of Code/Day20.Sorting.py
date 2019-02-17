#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
nSwap = 0
for i in range(n):
    nnSwap = 0
    for j in range(n-1-i):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            nnSwap += 1
    nSwap += nnSwap
    if nnSwap == 0:
        break

print('Array is sorted in %d swaps.' %nSwap)
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[-1]))
        
