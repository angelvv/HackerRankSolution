# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = int(input())
l = input().split()
k = int(input())
l_combination = list(combinations(l,k))
print(sum([1 for each in l_combination if 'a' in each])/len(l_combination))
