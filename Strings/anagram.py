#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = sorted(list(a))
    b = sorted(list(b))
    delCount = 0

    while True:

        # if we have come to the end of one list
        if len(a) == 0:
             delCount += len(b)
             break
        if len(b) == 0:
             delCount += len(a)
             break
        
        # check if a letter should be deleted
        if a[0] < b[0]:
            a.pop(0)
            delCount += 1
        elif a[0] > b[0]:
            b.pop(0)
            delCount += 1
        else:
            a.pop(0)
            b.pop(0)

    return delCount

if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)
    print(res)
