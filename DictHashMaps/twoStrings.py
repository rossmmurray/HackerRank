# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for letter in s1:
        if letter in s2:
            return 'YES'
    return 'NO'


if __name__ == '__main__':
    s1 = 'hi'
    s2 = 'world'
    result = twoStrings(s1, s2)
    print(result)
