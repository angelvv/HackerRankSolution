# Enter your code here. Read input from STDIN. Print output to STDOUT
d1,m1,y1 = [int(x) for x in input().split(" ")] # return date
d0,m0,y0 = [int(x) for x in input().split(" ")] # due date

if y1>y0:
    fine = 10000
elif y1==y0 and m1>m0:
    fine = 500 * (m1-m0)
elif y1==y0 and m1==m0 and d1>d0:
    fine = 15 * (d1-d0)
else:
    fine = 0

print(fine)

"""
# Alternatively, tuple comparison!
if (y1, m1, d1) <= (y0, m0, d0):
    print(0)
elif (y1, m1) == (y0, m0):
    print(15 * (d1 - d0))
elif y1 == y0:
    print(500 * (m1 - m0))
else:
    print(10000)
"""