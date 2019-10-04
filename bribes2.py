#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0

    # check for impossible sequence
    for index, number in enumerate(q):
        if number > index + 3:
            print('Too chaotic')
            return 'Too chaotic'
    
    # bubble sort
    for i in range(len(q) - 1):
        swapped = False
        for j in range(len(q) - 1 - i):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                bribes += 1
                swapped = True

        # early exit
        if not swapped:
            break
    
    print(bribes)
    return bribes


if __name__ == '__main__':
    arrayString1 = '2 1 5 3 4' 
    arrayString2 = '2 5 1 3 4'
    arrayString3 = '5 1 2 3 7 8 6 4'
    arrayString4 = '1 2 5 3 7 8 6 4'
    # res = minimumBribes([2, 1, 5, 3, 4])
    queue = list(map(int, arrayString1.split()))
    res = minimumBribes(queue)
    print(res)
