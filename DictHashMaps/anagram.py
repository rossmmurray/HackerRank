#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0

    # loop through each size of substring
    for size in range(len(s) - 1):
        sizeSubstrings = []

        # find all substrings of size "size" and add to list
        for i in range(len(s) - size):
            substring = s[i:i + size + 1]
            sizeSubstrings.append(Counter(substring))
        
        # compare all counter objects
        for a, b in combinations(sizeSubstrings, 2):
            count += 1 if a == b else 0
    return count

if __name__ == '__main__':
        s = 'abba' 
        result = sherlockAndAnagrams(s)
        print(result)
