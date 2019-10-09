#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for word in note:
        try:
            index = magazine.index(word)
            magazine.pop(index)
        except ValueError:
            print('No')
            return 1
    print('Yes')
    return 0


if __name__ == '__main__':
    # mn = input().split()

    # m = int(mn[0])

    # n = int(mn[1])

    magazine = 'Some test input stuff blah'.rstrip().split()

    note = 'test Some input blah'.rstrip().split()

    res = checkMagazine(magazine, note)
    print(res)
