#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    queue = q
    bribeNumbers = []
    while True:
        changeFlag = False
        for i in range(len(queue) - 1):

            # swap if next one is closer
            if queue[i] != i + 1 and (queue[i + 1] not in bribeNumbers) and abs(queue[i + 1] - (i + 1)) < abs(queue[i] - (i + 1)):
                bribeNumbers.append(queue[i + 1])
                queue[i], queue[i + 1] = queue[i + 1], queue[i]
                changeFlag = True

        # if no change in swipe through, end
        if queue == list(range(6))[1:]:
            return len(bribeNumbers)
        else:
            if changeFlag == False:
                return 'too chaotic'

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
