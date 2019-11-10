from collections import Counter


def freqQuery(inputArray):
    count = Counter()
    freq = Counter()
    output = []

    for query in inputArray:
        operation = query[0]
        inputVal = query[1]

        if operation == 1:
            freq[count[inputVal]] -= 1
            count[inputVal] += 1
            freq[count[inputVal]] += 1

        elif operation == 2:
            if count[inputVal] > 0:
                freq[count[inputVal]] -= 1
                count[inputVal] -= 1
                freq[count[inputVal]] += 1

        elif operation == 3:
            if freq[inputVal] > 0:
                output.append(1)
            else:
                output.append(0)
                
    return output

if __name__ == '__main__':
    inputArray = [(3, 4), (2, 1003), (1, 16), (3, 1)]
    inputArray2 = [(3,5), (3, 3), (1, 1000)]
    result = freqQuery(inputArray2)
    print(result)
