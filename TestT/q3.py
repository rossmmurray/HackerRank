

def solution(A):
    # I think the inital sum is wrong
    
    rowLength = len(A[0])
    columnLength = len(A)
    sums = []

    initialRowSum = sum(A[-1])
    initialColumnSum =0

    # calc initialColumnSum
    for val in A[1:]:
        initialColumnSum += val[-1]
        
    initialSum = initialRowSum + initialColumnSum
    sums.append(initialSum)
    currentSum = initialSum

    for q in range(columnLength -1, 1, -1):
        for p in range(0, rowLength -1):
            
            # minus rice from an old square and add rice from a new one
            currentSum -= A[p][q]
            currentSum += A[p - 1][q - 1]
            sums.append(currentSum)

    return max(sums)



if __name__ == "__main__":
    res = solution([[2, 2, 4, 2], [0, 3, 0, 1], [1, 2, 2, 1], [4, 1, 2, 2]] )
    print(res)