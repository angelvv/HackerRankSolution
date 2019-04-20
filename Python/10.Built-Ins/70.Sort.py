#!/bin/python3
from operator import itemgetter


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [[int(i) for i in input().split()] for _ in range(N)]
    k = int(input())
 
    for i in sorted(arr, key=itemgetter(k)):
        print(*i)

    #sarr = sorted(arr, key=itemgetter(k))
    #[print(*x, sep=' ') for x in sarr]