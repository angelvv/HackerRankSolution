# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N, title = [int(input()), input().split()]
Students = namedtuple('Students', title)
mark = [int(Students._make(input().split()).MARKS) for _ in range(N)]
#"_make" read the split string and map them to our expected sequence
print(sum(mark)/N)
