#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    lastKeptChar = s[0]
    delCount = 0
    for i in range(1, len(s)):
        if lastKeptChar == s[i]:
            delCount += 1
        else:
            lastKeptChar = s[i]
    return delCount

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(result)
