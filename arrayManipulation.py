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
        for i, _val in enumerate(array):
            if query[0] <= i + 1 <= query[1]:
                array[i] += query[2]
        # array = [x + query[2] for x in array]
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
