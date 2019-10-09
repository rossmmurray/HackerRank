def rotLeft(a, d):
    return a[d:] + a[:d]



if __name__ == "__main__":
    res = rotLeft([1, 2, 3, 4, 5], 4)
    print(res)