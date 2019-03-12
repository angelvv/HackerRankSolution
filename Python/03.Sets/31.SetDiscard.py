n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    eval('s.{}({})'.format(*input().split()+['']))
# add [''] at the end so that ['remove', '5'] + [''] = ['remove', '5', ''] and ['pop'] + [''] = ['pop', '']. Since format string uses only first 2 positional arguments , in first case '' will be ignored.
print(sum(s))