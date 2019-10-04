
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    # sorts in place
    ar.sort()  

    i = 0
    pairsTotal = 0
    while i < (n - 1):
        if ar[i] == ar[i + 1]:
            pairsTotal += 1
            i += 2
        else:
            i += 1

    return pairsTotal

if __name__ == '__main__':
    res = sockMerchant(10, [6,7,8,8,4,1,9,2,2,2])
    print(res)

