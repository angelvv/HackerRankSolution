# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


""" Less elegent solution
n,m = [int(x) for x in input().split(' ')]
p = '.|.' #pattern
# upper half
for i in range(n//2):
    print((p*(2*i+1)).center(m, '-'))
# middle
print('WELCOME'.center(m, '-'))
# lower half
for i in range(n//2-1,-1,-1):
    print((p*(2*i+1)).center(m, '-'))
"""