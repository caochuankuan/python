from functools import reduce

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str_int(s):
    def fn(x, y):
        return x * 10 + y

    def char_num(s):
        return digits[s]

    return reduce(fn, map(char_num, s))


print(str_int(['3', '5', '9']))
