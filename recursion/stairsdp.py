
def steps(n):
    res = [0 for i in range(0, n + 1)]
    res[0] = 1
    res[1] = 1
    for i in range(2, n + 1):
        res[i] = res[i - 1] + res[i - 2]
    return res[n]


tests = [1, 2, 3, 4, 5, 10, 33]
for test in tests:
    print(steps(test))
