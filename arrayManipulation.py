#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    array = [0] * n
    for query in queries:
        # for i in range(query[0], query[1] + 1):
        #     array[i - 1] += query[2]
        
    return max(array)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = [10, [[1, 2, 100], [2, 5, 100], [3, 4, 100]]]

    n = int(nm[0])

    m = nm[1]

    result = arrayManipulation(n, m)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
