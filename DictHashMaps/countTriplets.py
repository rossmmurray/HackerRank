#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the countTriplets function below.
def countTriplets(arr, r):
    count = 0
    for i, iVal in list(enumerate(arr))[:-2]:
        for j, jVal in list(enumerate(arr))[i + 1:-1]:
            if iVal * r == jVal:
                for _k, kVal in list(enumerate(arr))[j + 1:]:
                    if jVal * r == kVal:
                        count += 1
    return count


if __name__ == '__main__':
    r = 5
    arr = list(map(int, '1 5 5 25 125'.rstrip().split()))

    ans = countTriplets(arr, r)
    print(ans)
