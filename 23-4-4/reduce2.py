from functools import reduce


def tran(x, y):
    return x * 10 + y


print(reduce(tran, [1, 2, 3, 4, 5, 6]))
