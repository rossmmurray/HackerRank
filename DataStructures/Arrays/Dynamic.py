#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):

    # list of n empty lists
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    lastAnswers = []

    for query in queries:
        seq = (query[1] ^ lastAnswer) % n
        if query[0] == 1:
            seqList[seq].append(query[2])
        else:
            index = query[2] % len(seqList[seq])
            lastAnswer = seqList[seq][index]
            lastAnswers.append(lastAnswer)
    return lastAnswers

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))

