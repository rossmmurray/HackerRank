
def threeFive(n):

    runningSum = 0
    # loop up to n
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            runningSum += i
            print(i)
    return runningSum


if __name__ == "__main__":
    res = threeFive(1000)
    print(res)