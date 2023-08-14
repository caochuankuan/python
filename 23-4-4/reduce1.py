from functools import reduce


def addnums(x, y):
    return x + y


r = reduce(addnums, range(1, 101))
print(r)
