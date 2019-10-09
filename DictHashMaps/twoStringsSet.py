# Complete the twoStrings function below.
def twoStrings(s1, s2):
    return 'YES' if set(s1) & set(s2) else 'NO'


if __name__ == '__main__':
    s1 = 'hello'
    s2 = 'world'
    result = twoStrings(s1, s2)
    print(result)
