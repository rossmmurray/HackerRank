def hourglassSum(arr):
    row = 0
    column = 0
    height = len(arr)
    width = len(arr[0])
    totals = []
    while True:

        # calculate current hourglass
        top = arr[row][column:column + 3]
        middle = arr[row + 1][column + 1]
        bottom = arr[row + 2][column:column + 3]
        total = sum(top) + middle + sum(bottom)
        totals.append(total)

        # if third last column, go onto new row (unless last row)
        if column == width - 3:
            if row == height - 3:
                break
            column = 0
            row += 1
        else:
            column += 1

    return max(totals)



if __name__ == "__main__":
    numbersString = """-9 -9 -9  1 1 1 
        0 -9  0  4 3 2
        -9 -9 -9  1 2 3
        0  0  8  6 6 0
        0  0  0 -2 0 0
        0 0 1 2 4 0"""
    # res = re.split("\s", numbersString)
    rows = numbersString.split("\n")
    inputList = []
    for rowString in rows:
        rowList = rowString.split()
        rowListInts = [int(val) for val in rowList]
        inputList.append(rowListInts)
    # res = map(lambda x: int(x), res)
    # print(inputList)
    res = hourglassSum(inputList)
    print(res)
    # print(len(res))