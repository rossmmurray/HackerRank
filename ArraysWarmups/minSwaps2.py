def minimumSwaps(arr):
    swaps = 0
    i = 0

    # loop through array
    while i < len(arr):

        # if number not in correct place, swap it
        if arr[i] == i + 1:
            i += 1
        else:
            # tempNum is required because is changes midway through swap
            tempNum = arr[i]
            arr[i], arr[tempNum - 1] = arr[tempNum - 1], arr[i]
            swaps += 1

    return swaps


if __name__ == "__main__":

    f = open("minSwapVals.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        numList = contents.split()
        intList = list(map(int, numList))
        res = minimumSwaps(intList)
        print(intList[:33])

    # inputArray = [1, 3, 5, 2, 4, 6, 7]
    # res = minimumSwaps(inputArray)
    print(res)
    

