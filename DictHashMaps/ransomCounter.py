#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    magDict = Counter(magazine)
    noteDict = Counter(note)
    res = 'Yes' if (noteDict - magDict) == {} else 'No'
    print(res)
 


if __name__ == '__main__':
    # mn = input().split()

    # m = int(mn[0])

    # n = int(mn[1])

    magazine = 'Some test input stuff stuff blah dajkldja'.rstrip().split()

    note = 'test Some input blah'.rstrip().split()

    checkMagazine(magazine, note)
