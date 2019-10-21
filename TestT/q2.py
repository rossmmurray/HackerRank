from collections import Counter

def solution(A):

    # calculate occurrences of each value
    aCount = Counter(A)

    # assumes Counter keeps the order of array values
    # find first unique value
    for val in aCount:
        if aCount[val] == 1:
            return val
    
    # no uniqu value found
    return -1

if __name__ == "__main__":
    res = solution([1, 4, 3, 3, 1, 2] )
    print(res)