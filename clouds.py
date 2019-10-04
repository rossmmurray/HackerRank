def jumpingOnClouds(c):
    i = 0
    steps = 0
    while True:
        try:
            i += 2 if (len(c) != i + 2 and c[i + 2] == 0) else 1
            steps += 1
        except:
            return steps


    


if __name__ == "__main__":
    res = jumpingOnClouds([0, 0, 0, 1, 0, 0])
    print(res)