# Enter your code here. Read input from STDIN. Print output to STDOUT
country = set()
for n in range(int(input())):
    country.add(input())
print(len(country))

# One-liner
#print len({input() for x in range(int(input()))}) 