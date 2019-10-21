
def steps(n):
    if n < 2:
        return 1
    return steps(n-1) + steps(n-2)

tests = [1, 2, 3, 4, 5, 10, 33]
for test in tests:
    print(steps(test))