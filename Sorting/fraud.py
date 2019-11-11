#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import insort, bisect_left

# Complete the activityNotifications function below.

def getMedian(sortedInput):
    if len(sortedInput) % 2 == 0:
        medianHigh = len(sortedInput) // 2
        medianLow = medianHigh - 1
        return (sortedInput[medianHigh] + sortedInput[medianLow]) / 2
    else:
        medianIndex = (len(sortedInput) - 1) // 2
        return sortedInput[medianIndex]


def activityNotifications(expenditure, d):
    i = d
    notifyCount = 0
    trail = expenditure[i - d:i]
    trail.sort()

    while True:
        print(trail)

        # calculate if notification is needed on day i
        median = getMedian(trail)
        if expenditure[i] >= median * 2:
            notifyCount += 1

        if i == len(expenditure) - 1:
            break
        
        # trail remains sorted with delete and special insert
        # trail.remove(expenditure[i-d])  
        del trail[bisect_left(trail,expenditure[i-d])]
        insort(trail, expenditure[i])

        i += 1

    return notifyCount


if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)
    print(result)
