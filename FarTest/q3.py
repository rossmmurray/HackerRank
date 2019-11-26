#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'decodeString' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER numberOfRows
#  2. STRING encodedString
#

def arrDecoded(numberOfRows, encodedString):

    # put array into 2d array splitting by len(encodedString) / noRows (assume division has no remainder)
    splitIndex = len(encodedString) // numberOfRows
    rowedString = []
    for i in range(numberOfRows):
        rowedString.append(encodedString[i * splitIndex : (i + 1) * splitIndex ])

    # loop through height and width of 2d array
    arrDecoded = []
    firstCol = 0
    row = 0
    while firstCol < len(rowedString[0]):
        row = 0
        col = firstCol
        while row < len(rowedString):
            if col >= len(rowedString[0]):
                break

            # change underscores to spaces
            if rowedString[row][col] == '_':
                arrDecoded.append(' ')
            else:
                arrDecoded.append(rowedString[row][col])
            
            # diagonal down right
            row += 1
            col += 1

        # move col pointer on row 0 along 1 space
        firstCol += 1

    stringDecoded = ''.join(arrDecoded)
    return stringDecoded


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numberOfRows = int(input().strip())

    encodedString = input()

    result = arrDecoded(numberOfRows, encodedString)
    print(result)

    fptr.write(result + '\n')

    fptr.close()
