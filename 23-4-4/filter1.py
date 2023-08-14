def aa(n):
    return n % 2 == 0


a1 = filter(aa, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(a1))


def aaa(n):
    return n % 2 == 1


a2 = filter(aaa, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(a2))
