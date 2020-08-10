#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sumXor function below.
'''
# Simple - Naive Approach
def sumXor(n):
    counter  =0
    for i in range(n+1):
        if i+n == i^n:
            counter += 1
            print((i,n))
    return counter
'''

#  Advanced Approach using the concept :
# A + B = A^B + (A&B)
# SO A&B == 0 is what we need 
def sumXor(n):
    if n ==0:
        return 1
    counter_0 = 0
    bin_n = bin(n)
    print(bin_n)
    for char in bin_n:
        if char == '0':
            counter_0 += 1
    print(counter_0)

    return 1<<counter_0-1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
