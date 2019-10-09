#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magDict = {}
    for word in magazine:
        if word in magDict:
            magDict[word] += 1
        else:
            magDict[word] = 1
    for word in note:
        try:
            magDict[word] -= 1
            if magDict[word] < 0:
                print('No')
                return 1
        except KeyError:
            print('No')
            return 1
    print('Yes')
    return 0


    print(magDict)
    # for word in note:
    #     try:
    #         index = magazine.index(word)
    #         magazine.pop(index)
    #     except ValueError:
    #         print('No')
    #         return 1
    # print('Yes')
    # return 0


if __name__ == '__main__':
    # mn = input().split()

    # m = int(mn[0])

    # n = int(mn[1])

    magazine = 'Some test input stuff stuff blah'.rstrip().split()

    note = 'test Some input blah'.rstrip().split()

    res = checkMagazine(magazine, note)
