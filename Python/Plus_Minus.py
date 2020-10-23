 # Plus Minus Problem
 # HackerRank 
 # Problem: https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
 
 # solution
 #!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
# Complete the plusMinus function below.

# helper function
def approximate(red:str):
    if len(red) < 8:
        for i in range(0, 8-len(red)):
            red = red+"0"
    return red 
def plusMinus(arr):
    for i,num in enumerate(arr):
        if num < 0:
            arr[i] = -1
        elif num > 0:
            arr[i] = 1
        else:
            arr[i] = 0
    h_map = Counter(arr)
    res_1 = str(round(h_map[1]/len(arr), 6))
    res_m_1 = str(round(h_map[-1]/len(arr), 6))
    res_0 = str(round(h_map[0]/len(arr), 6))
    print(approximate(res_1))
    print(approximate(res_m_1))
    print(approximate(res_0))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
