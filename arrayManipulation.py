#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import accumulate

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    delta = [0] * (n + 2)
    for query in queries:
        delta[query[0]] += query[2]
        delta[query[1] + 1] -= query[2]
    return max(accumulate(delta))

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = [10, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]]

    n = int(nm[0])

    m = nm[1]

    result = arrayManipulation(n, m)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
