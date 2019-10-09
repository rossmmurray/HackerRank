a = [1, 3, 5]
b = a
b[:] = [x + 2 for x in a]
print(a)
print(b)