def LeftRotateByN(l, d):
    n = len(l)
    reverse(l, 0, d - 1)
    reverse(l, d, n - 1)
    reverse(l, 0, n - 1)

    return l


def reverse(l, b, e):
    while b < e:
        l[b], l[e] = l[e], l[b]
        b = b+1
        e = e-1


print(LeftRotateByN([10, 20, 30, 40], 3))
