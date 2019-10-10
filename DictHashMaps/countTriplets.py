#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the countTriplets function below.
def countTriplets(arr, r):

    # done with binomial n choose k formula and simplified
    if r == 1:
        l = len(arr)
        return l * (l - 1) * (l - 2) // 6
    
    # for when r != 1
    # FYI it doesn't matter if it's sorted
    count = 0
    arrCount = Counter(arr)
    for i in arrCount:
        # check if there is a next element which satisfied i * r, then i * r * r
        # tempArrCount is used since the arrCount[i] stuff would create new zeros
        tempArrCount = arrCount.copy()
        iCount = tempArrCount[i]

        jCount = tempArrCount[i * r]
        kCount = tempArrCount[i * r * r]
        count += iCount * jCount * kCount

    return count


if __name__ == '__main__':
    r = 1
    arr = list(map(int, '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'.rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)
