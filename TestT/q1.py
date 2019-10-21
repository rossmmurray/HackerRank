from math import sqrt

def solution(A, B):
    squareCount = 0
    for i in range(A, B + 1):

        # modulo 1 checks for whole number
        if sqrt(i) % 1 == 0:
            print(i)
            squareCount += 1
            
    return squareCount


if __name__ == "__main__":
    res = solution(4, 17)
    print(res)