#Problem        : Base Arithmetic
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

numberMap = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
'9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
baseTenSum = 0

# find bases
for number in data :
    highest = 0
    
    # find and set the base for the current number
    for digit in number:
        if numberMap[digit] > highest:
            highest = numberMap[digit]
    base = highest + 1
    
    # transform to base 10 (reverse because first loc has highest value)
    number = number[::-1]
    baseTenValue = 0
    for loc, digit in enumerate(number):
        baseTenValue += (base ** loc) * numberMap[digit]
    
    # add base 10 sums together
    baseTenSum += baseTenValue


print(baseTenSum)
