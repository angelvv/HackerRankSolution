#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n , k = map(int , input().split())
        print(k-1 if ((k-1) | k) <= n else k-2)

    """ Terminated due to timeout
    for t_itr in range(t):
        #XOR = []
        
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        maxit = 0
        for i in range(1,n):
            for j in range(i+1,n+1):
                if i&j < k and i&j > maxit:
                    maxit = i&j
        #print(XOR)
        print(maxit)
    """
    

