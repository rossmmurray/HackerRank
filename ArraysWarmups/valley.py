def countingValleys(n, s):
    dirVals = list(map(lambda x: 1 if x == 'U' else - 1, s))
    currentLevel = 0
    valleyCount = 0
    for direction in dirVals:
        if currentLevel == 0 and direction == -1:
            valleyCount += 1
        currentLevel += direction
    return valleyCount


if __name__ == "__main__":
    res = countingValleys(6, ['U','U', 'D', 'D', 'D', 'U'])
    print(res)