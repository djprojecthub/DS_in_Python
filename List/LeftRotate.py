def LeftRotate(l):
    first = l[0]
    length = len(l)
    for i in range(1, length):
        l[i - 1] = l[i]

    l[length - 1] = first

    return l


print(LeftRotate([10, 20, 30, 40]))
