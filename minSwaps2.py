def minimumSwaps(arr):
    swaps = 0
    minVal = min(arr)
    maxVal = max(arr)

    for i in range(minVal, maxVal):

        # find current number
        iLoc = arr.index(i + 1)

        # if number not in correct place, swap it
        if iLoc != i:
            arr[iLoc], arr[i] = arr[i], arr[iLoc]
            swaps += 1
            arr[i]
            print(i+1)

    return swaps

if __name__ == "__main__":
    f = open("minSwapVals.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        numList = contents.split()
        intList = list(map(int, numList))
        res = minimumSwaps(intList)
        print(res)
    # inputArray = [1, 3, 5, 2, 4, 6, 7]
    # res = minimumSwaps(inputArray)
    # print(res)