#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the countTriplets function below.
def countTriplets(arr, r):

    pairTargets = Counter()
    tripleTargets = Counter()
    count = 0

    for val in arr:
        if val in tripleTargets:
            count += tripleTargets[val]

        if val in pairTargets:
            tripleTargets[val*r] += pairTargets[val]

        pairTargets[val*r] += 1

    return count


if __name__ == '__main__':
    r = 5
    arr = list(map(int, '1 5 5 25 125'.rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)
