def repeatedString(s, n):
    valueAs = list(map(lambda letter: 1 if letter == 'a' else 0, s))
    remainder = n % len(s)
    return (n // len(s)) * sum(valueAs) + sum(valueAs[:remainder])


if __name__ == "__main__":
    res = repeatedString('aba', 10)
    print(res)