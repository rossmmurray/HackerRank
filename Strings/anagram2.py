#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    aCount = Counter(a)
    bCount = Counter(b)
    amb = aCount - bCount
    bma = bCount - aCount
    total = amb + bma
    return sum(total.values())

if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)
