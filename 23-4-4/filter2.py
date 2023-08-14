import math


def sqr_int(x):
    return math.sqrt(x) % 1 == 0


r_list = filter(sqr_int, range(1, 101))
print(list(r_list))