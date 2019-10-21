

def solution(A):
    # write your code in Python 3.6

    leftSum = 0
    rightSum = sum(A[1:])

    if leftSum == rightSum:
        return 0

    for p in range(1, len(A)):
        
        # calc left sum
        leftSum = leftSum + A[p - 1]

        # calc right sum
        rightSum = rightSum - A[p]

        if leftSum == rightSum:
            return p
        
    return -1


if __name__ == "__main__":
    res = solution([-1, 3, -4, 5, 1, -6, 2, 1])
    print(res)
    print(solution([]))