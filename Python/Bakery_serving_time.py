# Source: HackerRank
# Author: Pavan Kumar Paluri

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.

def jimOrders(orders):
    # Append the customer number-1 here right away with enumerate
    orders = list(enumerate(orders))
    orders = sorted(orders, key=lambda x: x[1][0]+x[1][1])
    list_final = [i[0]+1 for i in orders]
    return list_final

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
